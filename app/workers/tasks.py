from datetime import datetime, timezone

from app.workers.celery_app import celery_app

UTC = getattr(datetime, "UTC", timezone.utc)  # noqa: UP017


@celery_app.task(name="courier.ping")
def ping() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "worker",
        "timestamp": datetime.now(UTC).isoformat(),
    }
