from app.workers.celery_app import celery_app
from app.workers.tasks import ping


def test_celery_app_uses_expected_default_queue() -> None:
    assert celery_app.conf.task_default_queue == "courier"


def test_worker_ping_task_returns_expected_payload() -> None:
    payload = ping()

    assert payload["status"] == "ok"
    assert payload["service"] == "worker"
    assert "timestamp" in payload
