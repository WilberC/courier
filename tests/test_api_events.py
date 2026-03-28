from __future__ import annotations

from collections.abc import Generator

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine, select

from app.db.session import get_session
from app.main import app
from app.models.entities import Event


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


# Replaced in tests where needed.
from app.api.events import rate_limiter  # noqa: E402


def _session_override(engine) -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def _build_session_override(engine):
    def _override() -> Generator[Session, None, None]:
        yield from _session_override(engine)

    return _override


def test_post_events_requires_shared_secret() -> None:
    client = TestClient(app)

    response = client.post(
        "/events",
        json={"source": "cron", "event_type": "job.done", "payload": {"ok": True}},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid API shared secret"


def test_post_events_persists_event_and_returns_created() -> None:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    app.dependency_overrides[get_session] = _build_session_override(engine)
    client = TestClient(app)

    response = client.post(
        "/events",
        headers={"X-API-SECRET": "dev-shared-secret"},
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


def test_post_events_rejects_oversized_payload() -> None:
    client = TestClient(app)
    large_payload = {"blob": "x" * 40000}

    response = client.post(
        "/events",
        headers={"X-API-SECRET": "dev-shared-secret"},
        json={"source": "cron", "event_type": "job.done", "payload": large_payload},
    )

    assert response.status_code == 413


def test_post_events_throttles_when_limit_exceeded(monkeypatch) -> None:
    from app.api import events as events_module

    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    app.dependency_overrides[get_session] = _build_session_override(engine)

    events_module.rate_limiter = _InMemoryRateLimiter(limit=1)
    client = TestClient(app)

    first = client.post(
        "/events",
        headers={"X-API-SECRET": "dev-shared-secret"},
        json={"source": "cron", "event_type": "job.done", "payload": {}},
    )
    second = client.post(
        "/events",
        headers={"X-API-SECRET": "dev-shared-secret"},
        json={"source": "cron", "event_type": "job.done", "payload": {}},
    )

    assert first.status_code == 201
    assert second.status_code == 429

    monkeypatch.setattr(events_module, "rate_limiter", rate_limiter)
    app.dependency_overrides.clear()
