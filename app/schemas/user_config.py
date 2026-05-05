from __future__ import annotations

from pydantic import BaseModel


class BotModuleConfig(BaseModel):
    allowed_commands: list[str] = []
    timezone: str = "UTC"
    language: str = "en"


class EventsModuleConfig(BaseModel):
    allowed_sources: list[str] = []
    rate_limit_override: int | None = None


class ActionsModuleConfig(BaseModel):
    allowed_actions: list[str] = []
    timeout_override: int | None = None


class NotificationsModuleConfig(BaseModel):
    notify_on_error: bool = True
    notify_on_success: bool = False
    notify_on_action_complete: bool = True
    event_sources_filter: list[str] = []
