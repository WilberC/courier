from __future__ import annotations

from fastapi import Depends, Header, HTTPException
from sqlmodel import Session

from app.db.api_keys import validate_key
from app.db.session import get_session
from app.models.entities import User


async def require_api_key(
    x_api_key: str = Header(..., alias="X-API-KEY"),
    session: Session = Depends(get_session),
) -> User:
    user = validate_key(session, x_api_key)
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Invalid or revoked API key")
    return user
