from datetime import UTC, datetime

from app.workers.celery_app import celery_app


@celery_app.task(name="courier.ping")
def ping() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "worker",
        "timestamp": datetime.now(UTC).isoformat(),
    }
