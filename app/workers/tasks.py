from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Callable

from celery.exceptions import Retry
from sqlmodel import Session, select

from app.actions.runner import ActionRunner
from app.db.session import get_engine
from app.models.entities import ActionRun, Event
from app.workers.celery_app import celery_app

UTC = getattr(datetime, "UTC", timezone.utc)  # noqa: UP017
logger = logging.getLogger(__name__)


class NotificationTransientError(RuntimeError):
    pass


action_runner = ActionRunner()


def _action_echo(args: list[str]) -> str:
    return " ".join(args) if args else "echo"


action_runner.register_function_action(
    name="echo",
    function=_action_echo,
    timeout_seconds=10,
)


def _action_health(_args: list[str]) -> str:
    return "ok"


action_runner.register_function_action(
    name="health_check",
    function=_action_health,
    timeout_seconds=10,
)

_bot_notifier: Callable[[str], None] | None = None


def set_bot_notifier(notifier: Callable[[str], None]) -> None:
    global _bot_notifier
    _bot_notifier = notifier


@celery_app.task(name="courier.ping")
def ping() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "worker",
        "timestamp": datetime.now(UTC).isoformat(),
    }


@celery_app.task(
    bind=True,
    name="courier.notify",
    autoretry_for=(NotificationTransientError,),
    retry_backoff=True,
    retry_jitter=True,
    retry_kwargs={"max_retries": 3},
)
def notify_event(
    self,
    *,
    message: str,
    event_id: int | None = None,
    request_id: str | None = None,
) -> dict[str, str | int]:
    task_id = self.request.id
    with Session(get_engine()) as session:
        event: Event | None = None
        if event_id is not None:
            event = session.exec(select(Event).where(Event.id == event_id)).first()
            if event and event.status == "notified":
                logger.info(
                    "Notification skipped (already notified)",
                    extra={
                        "task_id": task_id,
                        "event_id": event_id,
                        "request_id": request_id,
                        "status": "skipped",
                    },
                )
                return {"status": "skipped", "event_id": event_id}

        try:
            _deliver_notification(message=message)
        except NotificationTransientError as exc:
            logger.warning(
                "Notification transient failure",
                extra={
                    "task_id": task_id,
                    "event_id": event_id,
                    "request_id": request_id,
                    "status": "retrying",
                },
            )
            raise self.retry(exc=exc) from exc

        if event:
            event.status = "notified"
            session.add(event)
            session.commit()

        logger.info(
            "Notification sent",
            extra={
                "task_id": task_id,
                "event_id": event_id,
                "request_id": request_id,
                "status": "sent",
            },
        )
        return {"status": "sent", "event_id": event_id or 0}


@celery_app.task(name="courier.execute_action")
def execute_action(
    *,
    action_name: str,
    args: list[str] | None = None,
    triggered_by: str = "bot",
    idempotency_key: str | None = None,
    request_id: str | None = None,
) -> dict[str, str | int]:
    normalized_args = args or []
    logger.info(
        "Starting action execution",
        extra={
            "action_name": action_name,
            "triggered_by": triggered_by,
            "idempotency_key": idempotency_key,
            "request_id": request_id,
        },
    )

    with Session(get_engine()) as session:
        if idempotency_key:
            existing = session.exec(
                select(ActionRun).where(ActionRun.idempotency_key == idempotency_key)
            ).first()
            if existing:
                logger.info(
                    "Action execution deduplicated",
                    extra={"action_name": action_name, "idempotency_key": idempotency_key},
                )
                return {
                    "status": existing.status,
                    "action_name": existing.action_name,
                    "action_run_id": existing.id,
                }

        result = action_runner.run(action_name=action_name, args=normalized_args)
        row = ActionRun(
            action_name=action_name,
            idempotency_key=idempotency_key,
            status=result.status,
            output=result.output,
            exit_code=result.exit_code,
            triggered_by=triggered_by,
        )
        session.add(row)
        session.commit()
        session.refresh(row)

    logger.info(
        "Action execution finished",
        extra={
            "action_name": action_name,
            "status": result.status,
            "action_run_id": row.id,
        },
    )
    _notify_action_result(
        action_name=action_name,
        status=result.status,
        output=result.output,
        request_id=request_id,
    )
    return {"status": result.status, "action_name": action_name, "action_run_id": row.id}


def _deliver_notification(*, message: str) -> None:
    if _bot_notifier is None:
        logger.info("Notification skipped: no bot notifier configured", extra={"message": message})
        return
    try:
        _bot_notifier(message)
    except (ConnectionError, TimeoutError) as exc:
        raise NotificationTransientError(str(exc)) from exc
    except Retry:
        raise
    except Exception as exc:  # pragma: no cover - fallback guard
        raise NotificationTransientError(str(exc)) from exc


def _notify_action_result(
    *,
    action_name: str,
    status: str,
    output: str,
    request_id: str | None = None,
) -> None:
    summary = f"Action {action_name} finished with status={status}. Output: {output[:500]}"
    try:
        notify_event.delay(message=summary, request_id=request_id)
    except Exception:  # pragma: no cover - defensive on disconnected broker
        logger.exception(
            "Failed to queue action result notification",
            extra={"action_name": action_name},
        )
