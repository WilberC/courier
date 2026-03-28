from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from sqlalchemy import JSON, Column
from sqlmodel import Field, SQLModel


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # noqa: UP045
    source: str
    event_type: str
    payload: dict[str, Any] = Field(default_factory=dict, sa_column=Column(JSON))
    status: str = Field(default="received", index=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),  # noqa: UP017
        index=True,
    )


class CommandLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # noqa: UP045
    user_id: int = Field(index=True)
    command: str
    result: Optional[str] = None  # noqa: UP045
    status: str = Field(default="ok", index=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),  # noqa: UP017
        index=True,
    )


class ActionRun(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # noqa: UP045
    action_name: str = Field(index=True)
    idempotency_key: Optional[str] = Field(default=None, index=True)  # noqa: UP045
    status: str = Field(default="pending", index=True)
    output: Optional[str] = None  # noqa: UP045
    exit_code: Optional[int] = None  # noqa: UP045
    triggered_by: str = Field(default="system", max_length=80)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),  # noqa: UP017
        index=True,
    )
