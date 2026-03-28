from __future__ import annotations

import logging
import uuid

from fastapi import FastAPI, Request
from redis import Redis
from sentry_sdk import capture_exception
from sqlalchemy import text
from starlette.responses import JSONResponse

from app.api.events import router as events_router
from app.core.observability import configure_logging, init_sentry_if_enabled
from app.core.settings import get_settings
from app.db.init_db import init_db
from app.db.session import get_engine
from app.workers.celery_app import celery_app

settings = get_settings()
app = FastAPI(title="Courier Bot API", version="0.1.0")
app.include_router(events_router)
logger = logging.getLogger(__name__)


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


@app.on_event("startup")
def startup_validation() -> None:
    configure_logging()
    init_sentry_if_enabled(settings)
    settings.validate_required()
    init_db()
    logger.info("API startup completed", extra={"status": "ok"})


@app.on_event("shutdown")
def shutdown_cleanup() -> None:
    logger.info("API shutdown completed", extra={"status": "ok"})


@app.exception_handler(Exception)
async def unhandled_exception_handler(_request: Request, exc: Exception):
    logger.exception("Unhandled API exception")
    capture_exception(exc)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


def _check_database() -> bool:
    try:
        with get_engine().connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        logger.exception("Database health check failed")
        return False


def _check_redis() -> bool:
    try:
        client = Redis.from_url(settings.redis_url, socket_connect_timeout=0.5, socket_timeout=0.5)
        return bool(client.ping())
    except Exception:
        logger.exception("Redis health check failed")
        return False


def _check_worker() -> bool:
    try:
        inspect = celery_app.control.inspect(timeout=0.5)
        response = inspect.ping()
        return bool(response)
    except Exception:
        logger.exception("Worker health check failed")
        return False


@app.get("/health")
def health() -> dict[str, object]:
    dependencies = {
        "api": True,
        "database": _check_database(),
        "redis": _check_redis(),
        "worker": _check_worker(),
    }
    status = "ok" if all(dependencies.values()) else "degraded"
    return {"status": status, "env": settings.app_env, "dependencies": dependencies}
