from __future__ import annotations

from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine, select

from app import main as main_module
from app.db.session import get_session
from app.main import app
from app.models.entities import Event
from app.workers import tasks


def _session_override(engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def _build_session_override(engine):
    def _override() -> Generator[Session, None, None]:
        yield from _session_override(engine)

    return _override


def test_api_event_to_worker_notification_flow(monkeypatch) -> None:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    app.dependency_overrides[get_session] = _build_session_override(engine)
    monkeypatch.setattr(tasks, "get_engine", lambda: engine)

    delivered: list[str] = []
    tasks.set_bot_notifier(delivered.append)

    from app.api import events as events_module

    def _inline_send_task(task_name: str, kwargs: dict | None = None):
        assert task_name == "courier.notify"
        tasks.notify_event.run(**(kwargs or {}))

    monkeypatch.setattr(events_module.celery_app, "send_task", _inline_send_task)
    monkeypatch.setattr(main_module, "_check_database", lambda: True)
    monkeypatch.setattr(main_module, "_check_redis", lambda: True)
    monkeypatch.setattr(main_module, "_check_worker", lambda: True)

    client = TestClient(app)
    response = client.post(
        "/events",
        headers={"X-API-SECRET": "dev-shared-secret"},
        json={"source": "cron", "event_type": "job.failed", "payload": {}, "status": "error"},
    )

    assert response.status_code == 201
    with Session(engine) as session:
        stored = session.exec(select(Event)).one()
    assert stored.status == "notified"
    assert len(delivered) == 1
    assert "job.failed" in delivered[0]

    app.dependency_overrides.clear()
