from fastapi import FastAPI

from app.core.settings import get_settings
from app.db.init_db import init_db

settings = get_settings()
app = FastAPI(title="Courier Bot API", version="0.1.0")


@app.on_event("startup")
def startup_validation() -> None:
    settings.validate_required()
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.app_env}
