from __future__ import annotations

from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine, select

from app.db.api_keys import create_key
from app.db.session import get_session
from app.db.users import upsert_telegram_user
from app.main import app
from app.models.entities import Event


def _make_engine():
    return create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


def _session_override(engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def _build_session_override(engine):
    def _override() -> Generator[Session, None, None]:
        yield from _session_override(engine)

    return _override


def _setup_engine_with_user() -> tuple:
    """Return (engine, raw_api_key) with a seeded user and API key."""
    engine = _make_engine()
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        user = upsert_telegram_user(session, 1, role="admin")
        _, raw_key = create_key(session, user.id, "test-key")
    return engine, raw_key


class _InMemoryRateLimiter:
    def __init__(self, limit: int = 100):
        self.limit = limit
        self.calls: dict[str, int] = {}

    def allow(self, key: str) -> bool:
        current = self.calls.get(key, 0)
        if current >= self.limit:
            return False
        self.calls[key] = current + 1
        return True


from app.api.events import rate_limiter  # noqa: E402


def test_post_events_requires_api_key() -> None:
    client = TestClient(app)

    response = client.post(
        "/events",
        json={"source": "cron", "event_type": "job.done", "payload": {"ok": True}},
    )

    assert response.status_code == 422  # missing required header


def test_post_events_rejects_invalid_api_key() -> None:
    engine = _make_engine()
    SQLModel.metadata.create_all(engine)
    app.dependency_overrides[get_session] = _build_session_override(engine)
    client = TestClient(app)

    response = client.post(
        "/events",
        headers={"X-API-KEY": "invalid-key"},
        json={"source": "cron", "event_type": "job.done", "payload": {"ok": True}},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or revoked API key"
    app.dependency_overrides.clear()


def test_post_events_persists_event_and_returns_created() -> None:
    engine, raw_key = _setup_engine_with_user()
    app.dependency_overrides[get_session] = _build_session_override(engine)
    client = TestClient(app)

    response = client.post(
        "/events",
        headers={"X-API-KEY": raw_key},
        json={
            "source": " cron ",
            "event_type": " JOB.FINISHED ",
            "payload": {"job": "backup"},
            "status": " RECEIVED ",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["source"] == "cron"
    assert body["event_type"] == "job.finished"
    assert body["status"] == "received"

    with Session(engine) as session:
        events = session.exec(select(Event)).all()

    assert len(events) == 1
    assert events[0].event_type == "job.finished"

    app.dependency_overrides.clear()


def test_post_events_enqueues_worker_notification(monkeypatch) -> None:
    from app.api import events as events_module

    engine, raw_key = _setup_engine_with_user()
    app.dependency_overrides[get_session] = _build_session_override(engine)

    queued: list[tuple[str, dict]] = []

    def _fake_send_task(task_name: str, kwargs: dict | None = None):
        queued.append((task_name, kwargs or {}))

    monkeypatch.setattr(events_module.celery_app, "send_task", _fake_send_task)
    events_module.rate_limiter = _InMemoryRateLimiter(limit=5)
    client = TestClient(app)

    response = client.post(
        "/events",
        headers={"X-API-KEY": raw_key},
        json={
            "source": "svc",
            "event_type": "build.done",
            "payload": {"id": 1},
            "status": "received",
        },
    )

    assert response.status_code == 201
    assert len(queued) == 1
    assert queued[0][0] == "courier.notify"
    assert queued[0][1]["event_id"] == response.json()["id"]
    assert "request_id" in queued[0][1]

    monkeypatch.setattr(events_module, "rate_limiter", rate_limiter)
    app.dependency_overrides.clear()


def test_post_events_rejects_oversized_payload() -> None:
    engine, raw_key = _setup_engine_with_user()
    app.dependency_overrides[get_session] = _build_session_override(engine)
    client = TestClient(app)
    large_payload = {"blob": "x" * 40000}

    response = client.post(
        "/events",
        headers={"X-API-KEY": raw_key},
        json={"source": "cron", "event_type": "job.done", "payload": large_payload},
    )

    assert response.status_code == 413
    app.dependency_overrides.clear()


def test_post_events_throttles_when_limit_exceeded(monkeypatch) -> None:
    from app.api import events as events_module

    engine, raw_key = _setup_engine_with_user()
    app.dependency_overrides[get_session] = _build_session_override(engine)

    events_module.rate_limiter = _InMemoryRateLimiter(limit=1)
    client = TestClient(app)

    first = client.post(
        "/events",
        headers={"X-API-KEY": raw_key},
        json={"source": "cron", "event_type": "job.done", "payload": {}},
    )
    second = client.post(
        "/events",
        headers={"X-API-KEY": raw_key},
        json={"source": "cron", "event_type": "job.done", "payload": {}},
    )

    assert first.status_code == 201
    assert second.status_code == 429

    monkeypatch.setattr(events_module, "rate_limiter", rate_limiter)
    app.dependency_overrides.clear()


def test_post_events_rejects_disallowed_source() -> None:
    from app.db.users import update_module_config
    from app.models.entities import User
    from sqlmodel import select as sqlmodel_select

    engine, _ = _setup_engine_with_user()

    with Session(engine) as session:
        user = session.exec(sqlmodel_select(User)).first()
        user_id = user.id
        update_module_config(session, user_id, "events", {"allowed_sources": ["backup"]})
        _, restricted_key = create_key(session, user_id, "restricted")

    app.dependency_overrides[get_session] = _build_session_override(engine)
    client = TestClient(app)

    response = client.post(
        "/events",
        headers={"X-API-KEY": restricted_key},
        json={"source": "monitor", "event_type": "alert", "payload": {}},
    )

    assert response.status_code == 403
    assert "not allowed" in response.json()["detail"]
    app.dependency_overrides.clear()
