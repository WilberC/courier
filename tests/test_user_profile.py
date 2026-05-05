from __future__ import annotations

from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine, select

from app.db.users import (
    get_actions_config,
    get_bot_config,
    get_by_id,
    get_by_telegram_id,
    get_events_config,
    get_notifications_config,
    list_users,
    update_module_config,
    upsert_telegram_user,
)
from app.models.entities import User
from app.schemas.user_config import (
    ActionsModuleConfig,
    BotModuleConfig,
    EventsModuleConfig,
    NotificationsModuleConfig,
)


def _engine():
    return create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


def test_upsert_creates_new_user() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42, username="alice", first_name="Alice", role="user")

    assert user.id is not None
    assert user.telegram_user_id == 42
    assert user.username == "alice"
    assert user.role == "user"
    assert user.last_seen_at is not None


def test_upsert_updates_existing_user_last_seen() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        first = upsert_telegram_user(session, 42)
        first_seen = first.last_seen_at

    with Session(engine) as session:
        second = upsert_telegram_user(session, 42)

    assert second.last_seen_at >= first_seen
    with Session(engine) as session:
        count = len(session.exec(select(User)).all())
    assert count == 1


def test_upsert_never_downgrades_role() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        upsert_telegram_user(session, 42, role="admin")
        user = upsert_telegram_user(session, 42, role="user")

    assert user.role == "admin"


def test_upsert_upgrades_role_to_admin() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        upsert_telegram_user(session, 42, role="user")
        user = upsert_telegram_user(session, 42, role="admin")

    assert user.role == "admin"


def test_get_by_telegram_id_returns_none_for_unknown() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        result = get_by_telegram_id(session, 9999)

    assert result is None


def test_get_by_id_returns_user() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        created = upsert_telegram_user(session, 42)
        found = get_by_id(session, created.id)

    assert found is not None
    assert found.telegram_user_id == 42


def test_list_users_returns_active_only_by_default() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        upsert_telegram_user(session, 1)
        u2 = upsert_telegram_user(session, 2)
        u2.is_active = False
        session.add(u2)
        session.commit()
        active = list_users(session)

    assert len(active) == 1
    assert active[0].telegram_user_id == 1


def test_list_users_all_when_active_only_false() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        upsert_telegram_user(session, 1)
        u2 = upsert_telegram_user(session, 2)
        u2.is_active = False
        session.add(u2)
        session.commit()
        all_users = list_users(session, active_only=False)

    assert len(all_users) == 2


def test_update_module_config_persists_events_config() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42)
        updated = update_module_config(
            session, user.id, "events", {"allowed_sources": ["backup", "cron"]}
        )
        cfg = get_events_config(updated)

    assert cfg.allowed_sources == ["backup", "cron"]


def test_update_module_config_raises_for_unknown_user() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    import pytest

    with Session(engine) as session:
        with pytest.raises(ValueError, match="not found"):
            update_module_config(session, 9999, "events", {})


def test_default_bot_config_allows_all_commands() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42)
        cfg = get_bot_config(user)

    assert cfg.allowed_commands == []
    assert cfg.timezone == "UTC"
    assert cfg.language == "en"


def test_default_events_config() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42)
        cfg = get_events_config(user)

    assert cfg.allowed_sources == []
    assert cfg.rate_limit_override is None


def test_default_actions_config() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42)
        cfg = get_actions_config(user)

    assert cfg.allowed_actions == []
    assert cfg.timeout_override is None


def test_default_notifications_config() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42)
        cfg = get_notifications_config(user)

    assert cfg.notify_on_error is True
    assert cfg.notify_on_success is False
    assert cfg.notify_on_action_complete is True
    assert cfg.event_sources_filter == []


def test_bot_config_update_persists() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = upsert_telegram_user(session, 42)
        updated = update_module_config(
            session, user.id, "bot", {"allowed_commands": ["/ping", "/help"], "timezone": "US/Eastern"}
        )
        cfg = get_bot_config(updated)

    assert cfg.allowed_commands == ["/ping", "/help"]
    assert cfg.timezone == "US/Eastern"
