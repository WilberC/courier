from __future__ import annotations

import hashlib
import secrets
from datetime import datetime, timezone

from sqlmodel import Session, select

from app.models.entities import APIKey, User


def _hash_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode()).hexdigest()


def create_key(session: Session, user_id: int, name: str) -> tuple[APIKey, str]:
    raw_key = secrets.token_hex(32)
    key = APIKey(
        user_id=user_id,
        name=name,
        key_prefix=raw_key[:8],
        key_hash=_hash_key(raw_key),
    )
    session.add(key)
    session.commit()
    session.refresh(key)
    return key, raw_key


def validate_key(session: Session, raw_key: str) -> User | None:
    h = _hash_key(raw_key)
    api_key = session.exec(
        select(APIKey).where(APIKey.key_hash == h, APIKey.is_active == True)  # noqa: E712
    ).first()
    if api_key is None:
        return None
    api_key.last_used_at = datetime.now(timezone.utc)
    session.add(api_key)
    session.commit()
    return session.get(User, api_key.user_id)


def revoke_key(session: Session, key_id: int) -> bool:
    key = session.get(APIKey, key_id)
    if key is None:
        return False
    key.is_active = False
    session.add(key)
    session.commit()
    return True


def list_user_keys(session: Session, user_id: int) -> list[APIKey]:
    return list(session.exec(select(APIKey).where(APIKey.user_id == user_id)).all())
