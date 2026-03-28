from __future__ import annotations

from sqlmodel import SQLModel

from app.db.session import get_engine
from app.models import entities  # noqa: F401


def init_db(engine=None) -> None:
    SQLModel.metadata.create_all(engine or get_engine())
