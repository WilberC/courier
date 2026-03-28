from __future__ import annotations

from sqlmodel import Session, SQLModel, create_engine, select

from app.models.entities import ActionRun, Event
from app.workers.celery_app import celery_app
from app.workers import tasks


def test_celery_app_uses_expected_default_queue() -> None:
    assert celery_app.conf.task_default_queue == "courier"


def test_worker_ping_task_returns_expected_payload() -> None:
    payload = tasks.ping()

    assert payload["status"] == "ok"
    assert payload["service"] == "worker"
    assert "timestamp" in payload


def test_notify_event_marks_event_as_notified_and_is_idempotent(monkeypatch) -> None:
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    monkeypatch.setattr(tasks, "get_engine", lambda: engine)

    sent: list[str] = []
    tasks.set_bot_notifier(sent.append)

    with Session(engine) as session:
        event = Event(source="cron", event_type="job.failed", payload={}, status="received")
        session.add(event)
        session.commit()
        session.refresh(event)
        event_id = event.id

    first = tasks.notify_event.run(message="failed job", event_id=event_id)
    second = tasks.notify_event.run(message="failed job", event_id=event_id)

    assert first["status"] == "sent"
    assert second["status"] == "skipped"
    assert sent == ["failed job"]

    with Session(engine) as session:
        persisted = session.exec(select(Event).where(Event.id == event_id)).one()
    assert persisted.status == "notified"


def test_execute_action_persists_outcome_and_enqueues_notification(monkeypatch) -> None:
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    monkeypatch.setattr(tasks, "get_engine", lambda: engine)

    notifications: list[str] = []

    class _FakeNotify:
        @staticmethod
        def delay(*, message: str, event_id=None, request_id=None):
            notifications.append(message)

    monkeypatch.setattr(tasks, "notify_event", _FakeNotify())

    result = tasks.execute_action.run(action_name="echo", args=["hello"], triggered_by="tests")

    assert result["status"] == "success"
    assert result["action_name"] == "echo"
    assert result["action_run_id"] > 0
    assert len(notifications) == 1
    assert "status=success" in notifications[0]

    with Session(engine) as session:
        rows = session.exec(select(ActionRun)).all()
    assert len(rows) == 1
    assert rows[0].action_name == "echo"
    assert rows[0].status == "success"
    assert rows[0].triggered_by == "tests"


def test_execute_action_is_idempotent_when_key_reused(monkeypatch) -> None:
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    SQLModel.metadata.create_all(engine)
    monkeypatch.setattr(tasks, "get_engine", lambda: engine)

    class _FakeNotify:
        @staticmethod
        def delay(*, message: str, event_id=None, request_id=None):
            return None

    monkeypatch.setattr(tasks, "notify_event", _FakeNotify())
    idem = "evt-123"

    first = tasks.execute_action.run(
        action_name="echo",
        args=["first"],
        triggered_by="tests",
        idempotency_key=idem,
    )
    second = tasks.execute_action.run(
        action_name="echo",
        args=["second"],
        triggered_by="tests",
        idempotency_key=idem,
    )

    assert first["action_run_id"] == second["action_run_id"]

    with Session(engine) as session:
        rows = session.exec(select(ActionRun)).all()
    assert len(rows) == 1
