from celery import Celery

from app.core.observability import configure_logging, init_sentry_if_enabled
from app.core.settings import get_settings

settings = get_settings()
configure_logging()
init_sentry_if_enabled(settings)

celery_app = Celery(
    "courier",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_default_queue="courier",
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)

celery_app.autodiscover_tasks(["app.workers"])
