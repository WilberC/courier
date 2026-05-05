from __future__ import annotations

import json
import logging
import uuid

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlmodel import Session

from app.api.auth import require_api_key
from app.api.rate_limit import FixedWindowRateLimiter
from app.api.schemas import EventIn, EventOut
from app.core.settings import get_settings
from app.db.session import get_session
from app.db.users import get_events_config
from app.models.entities import Event, User
from app.workers.celery_app import celery_app

router = APIRouter(tags=["events"])
logger = logging.getLogger(__name__)

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
    user: User = Depends(require_api_key),
) -> Event:
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    logger.info("Incoming event request", extra={"request_id": request_id, "status": "started"})

    request_ip = request.client.host if request.client else "unknown"
    if not rate_limiter.allow(request_ip):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    payload_size = len(json.dumps(payload.payload).encode("utf-8"))
    if payload_size > settings.event_max_payload_bytes:
        raise HTTPException(status_code=413, detail="Payload too large")

    clean = _sanitize_event_input(payload)

    events_cfg = get_events_config(user)
    if events_cfg.allowed_sources and clean.source not in events_cfg.allowed_sources:
        raise HTTPException(status_code=403, detail="Event source not allowed for this API key")

    event = Event(
        source=clean.source,
        event_type=clean.event_type,
        payload=clean.payload,
        status=clean.status,
    )
    session.add(event)
    session.commit()
    session.refresh(event)
    logger.info(
        "Event persisted",
        extra={"request_id": request_id, "event_id": event.id, "status": event.status},
    )
    try:
        celery_app.send_task(
            "courier.notify",
            kwargs={
                "message": f"[{event.status}] {event.source}:{event.event_type}",
                "event_id": event.id,
                "request_id": request_id,
            },
        )
    except Exception:  # pragma: no cover - do not fail ingestion on queue issues
        logger.exception(
            "Failed to queue notification for event",
            extra={"request_id": request_id, "event_id": event.id},
        )

    return event
