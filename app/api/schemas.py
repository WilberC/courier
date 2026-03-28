from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class EventIn(BaseModel):
    source: str = Field(min_length=1, max_length=120)
    event_type: str = Field(min_length=1, max_length=120)
    payload: dict[str, Any] = Field(default_factory=dict)
    status: str = Field(default="received", max_length=40)


class EventOut(BaseModel):
    id: int
    source: str
    event_type: str
    status: str
    created_at: datetime
