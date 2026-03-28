from __future__ import annotations

from sqlmodel import Session, SQLModel, create_engine, select

from app.bot.service import BotService
from app.models.entities import CommandLog, Event


def _engine_for_test():
    return create_engine("sqlite://", connect_args={"check_same_thread": False})


def test_ping_for_allowed_user_and_command_log_created() -> None:
    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)
    service = BotService(
        engine=engine,
        allowed_user_ids=[100],
        admin_user_ids=[100],
        task_sender=lambda *_: None,
    )

    message = service.process_command(user_id=100, command="/ping", args=[])

    assert "pong" in message.lower()

    with Session(engine) as session:
        logs = session.exec(select(CommandLog)).all()
    assert len(logs) == 1
    assert logs[0].command == "/ping"


def test_unauthorized_user_is_blocked_and_logged() -> None:
    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)
    service = BotService(
        engine=engine,
        allowed_user_ids=[100],
        admin_user_ids=[100],
        task_sender=lambda *_: None,
    )

    message = service.process_command(user_id=200, command="/status", args=[])

    assert "not authorized" in message.lower()

    with Session(engine) as session:
        log = session.exec(select(CommandLog)).one()
    assert log.status == "denied"


def test_run_requires_admin_role() -> None:
    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)
    service = BotService(
        engine=engine,
        allowed_user_ids=[100, 200],
        admin_user_ids=[100],
        task_sender=lambda *_: None,
    )

    message = service.process_command(user_id=200, command="/run", args=["ping_worker"])

    assert "admin" in message.lower()


def test_run_whitelisted_task_is_dispatched() -> None:
    calls: list[str] = []

    def _sender(task_name: str) -> None:
        calls.append(task_name)

    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)
    service = BotService(
        engine=engine,
        allowed_user_ids=[100],
        admin_user_ids=[100],
        task_sender=_sender,
    )

    message = service.process_command(user_id=100, command="/run", args=["ping_worker"])

    assert "queued" in message.lower()
    assert calls == ["courier.ping"]


def test_last_errors_returns_recent_failure_events() -> None:
    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(Event(source="cron", event_type="job.ok", payload={}, status="received"))
        session.add(Event(source="cron", event_type="job.failed", payload={}, status="error"))
        session.commit()

    service = BotService(
        engine=engine,
        allowed_user_ids=[100],
        admin_user_ids=[100],
        task_sender=lambda *_: None,
    )

    message = service.process_command(user_id=100, command="/last_errors", args=[])

    assert "job.failed" in message
