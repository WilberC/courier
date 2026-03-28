from __future__ import annotations

from collections.abc import Generator
from functools import lru_cache

from sqlmodel import Session, create_engine

from app.core.settings import get_settings


def _sqlite_connect_args(database_url: str) -> dict[str, bool]:
    if database_url.startswith("sqlite"):
        return {"check_same_thread": False}
    return {}


@lru_cache(maxsize=1)
def get_engine(database_url: str | None = None):
    url = database_url or get_settings().database_url
    return create_engine(url, connect_args=_sqlite_connect_args(url), echo=False)


def get_session() -> Generator[Session, None, None]:
    with Session(get_engine()) as session:
        yield session
