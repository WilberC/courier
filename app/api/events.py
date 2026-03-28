from __future__ import annotations

import json
from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from sqlmodel import Session

from app.api.rate_limit import FixedWindowRateLimiter
from app.api.schemas import EventIn, EventOut
from app.core.settings import get_settings
from app.db.session import get_session
from app.models.entities import Event

router = APIRouter(tags=["events"])

settings = get_settings()
rate_limiter = FixedWindowRateLimiter(limit=max(settings.event_rate_limit_per_minute, 1))


def _sanitize_event_input(data: EventIn) -> EventIn:
    return EventIn(
        source=data.source.strip(),
        event_type=data.event_type.strip().lower(),
        payload=data.payload,
        status=data.status.strip().lower(),
    )


@router.post("/events", response_model=EventOut, status_code=status.HTTP_201_CREATED)
def create_event(
    payload: EventIn,
    request: Request,
    session: Session = Depends(get_session),
    x_api_secret: Optional[str] = Header(default=None, alias="X-API-SECRET"),  # noqa: UP045
) -> Event:
    if x_api_secret != settings.api_shared_secret:
        raise HTTPException(status_code=401, detail="Invalid API shared secret")

    request_ip = request.client.host if request.client else "unknown"
    if not rate_limiter.allow(request_ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    payload_size = len(json.dumps(payload.payload).encode("utf-8"))
    if payload_size > settings.event_max_payload_bytes:
        raise HTTPException(status_code=413, detail="Payload too large")

    clean = _sanitize_event_input(payload)

    event = Event(
        source=clean.source,
        event_type=clean.event_type,
        payload=clean.payload,
        status=clean.status,
    )
    session.add(event)
    session.commit()
    session.refresh(event)

    return event
