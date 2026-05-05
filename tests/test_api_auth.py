from __future__ import annotations

from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.db.api_keys import create_key, list_user_keys, revoke_key, validate_key
from app.db.users import upsert_telegram_user


def _engine():
    return create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )


def _make_user(session: Session, telegram_id: int = 1, role: str = "user"):
    return upsert_telegram_user(session, telegram_id, role=role)


def test_create_key_returns_record_and_raw_key() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session)
        key_record, raw_key = create_key(session, user.id, "my-service")
        # Read values inside session before it closes
        key_id = key_record.id
        key_user_id = key_record.user_id
        key_name = key_record.name
        key_prefix = key_record.key_prefix
        key_is_active = key_record.is_active

    assert key_id is not None
    assert key_user_id is not None
    assert key_name == "my-service"
    assert key_prefix == raw_key[:8]
    assert key_is_active is True
    assert len(raw_key) == 64  # secrets.token_hex(32) = 64 hex chars


def test_validate_key_returns_user_for_valid_key() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session, telegram_id=99, role="admin")
        _, raw_key = create_key(session, user.id, "test")

    with Session(engine) as session:
        found_user = validate_key(session, raw_key)

    assert found_user is not None
    assert found_user.telegram_user_id == 99
    assert found_user.role == "admin"


def test_validate_key_updates_last_used_at() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session)
        user_id = user.id
        key_record, raw_key = create_key(session, user_id, "test")
        assert key_record.last_used_at is None

    with Session(engine) as session:
        validate_key(session, raw_key)
        keys = list_user_keys(session, user_id)
        last_used = keys[0].last_used_at

    assert last_used is not None


def test_validate_key_returns_none_for_invalid_key() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        result = validate_key(session, "not-a-real-key")

    assert result is None


def test_validate_key_returns_none_for_revoked_key() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session)
        key_record, raw_key = create_key(session, user.id, "test")
        revoke_key(session, key_record.id)

    with Session(engine) as session:
        result = validate_key(session, raw_key)

    assert result is None


def test_revoke_key_deactivates_key() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session)
        key_record, _ = create_key(session, user.id, "test")
        ok = revoke_key(session, key_record.id)
        keys = list_user_keys(session, user.id)

    assert ok is True
    assert keys[0].is_active is False


def test_revoke_key_returns_false_for_missing_key() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        ok = revoke_key(session, 9999)

    assert ok is False


def test_list_user_keys_returns_all_keys_for_user() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session)
        create_key(session, user.id, "key-a")
        create_key(session, user.id, "key-b")
        keys = list_user_keys(session, user.id)

    assert len(keys) == 2
    names = {k.name for k in keys}
    assert names == {"key-a", "key-b"}


def test_key_hash_is_not_stored_as_plain_text() -> None:
    engine = _engine()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        user = _make_user(session)
        key_record, raw_key = create_key(session, user.id, "test")

    assert key_record.key_hash != raw_key
    assert len(key_record.key_hash) == 64  # SHA-256 hex = 64 chars
