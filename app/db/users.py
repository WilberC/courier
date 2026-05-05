from __future__ import annotations

from datetime import datetime, timezone

from sqlmodel import Session, select

from app.models.entities import User
from app.schemas.user_config import (
    ActionsModuleConfig,
    BotModuleConfig,
    EventsModuleConfig,
    NotificationsModuleConfig,
)


def get_by_telegram_id(session: Session, telegram_id: int) -> User | None:
    return session.exec(select(User).where(User.telegram_user_id == telegram_id)).first()


def get_by_id(session: Session, user_id: int) -> User | None:
    return session.get(User, user_id)


def upsert_telegram_user(
    session: Session,
    telegram_id: int,
    *,
    username: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    role: str = "user",
) -> User:
    user = get_by_telegram_id(session, telegram_id)
    now = datetime.now(timezone.utc)
    if user is None:
        user = User(
            telegram_user_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=role,
            last_seen_at=now,
        )
    else:
        user.last_seen_at = now
        if username is not None:
            user.username = username
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if role == "admin":
            user.role = "admin"
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_module_config(session: Session, user_id: int, module: str, config: dict) -> User:
    user = get_by_id(session, user_id)
    if user is None:
        raise ValueError(f"User {user_id} not found")
    setattr(user, f"{module}_config", config)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def list_users(session: Session, *, active_only: bool = True) -> list[User]:
    stmt = select(User)
    if active_only:
        stmt = stmt.where(User.is_active == True)  # noqa: E712
    return list(session.exec(stmt).all())


def get_bot_config(user: User) -> BotModuleConfig:
    return BotModuleConfig.model_validate(user.bot_config or {})


def get_events_config(user: User) -> EventsModuleConfig:
    return EventsModuleConfig.model_validate(user.events_config or {})


def get_actions_config(user: User) -> ActionsModuleConfig:
    return ActionsModuleConfig.model_validate(user.actions_config or {})


def get_notifications_config(user: User) -> NotificationsModuleConfig:
    return NotificationsModuleConfig.model_validate(user.notifications_config or {})
