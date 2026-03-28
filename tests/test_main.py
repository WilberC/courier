from fastapi.testclient import TestClient

from app import main as main_module
from app.main import app, startup_validation


def test_startup_validation_runs_without_error() -> None:
    startup_validation()


def test_request_id_is_returned_in_response_headers(monkeypatch) -> None:
    monkeypatch.setattr(main_module, "_check_database", lambda: True)
    monkeypatch.setattr(main_module, "_check_redis", lambda: True)
    monkeypatch.setattr(main_module, "_check_worker", lambda: True)

    client = TestClient(app)
    response = client.get("/health", headers={"X-Request-ID": "req-123"})

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == "req-123"
