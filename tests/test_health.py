from fastapi.testclient import TestClient

from app import main as main_module
from app.main import app


def test_health_endpoint_returns_ok_status() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] in {"ok", "degraded"}
    assert "env" in response.json()
    assert "dependencies" in response.json()


def test_health_endpoint_reports_healthy_dependencies(monkeypatch) -> None:
    monkeypatch.setattr(main_module, "_check_database", lambda: True)
    monkeypatch.setattr(main_module, "_check_redis", lambda: True)
    monkeypatch.setattr(main_module, "_check_worker", lambda: True)

    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["dependencies"] == {
        "api": True,
        "database": True,
        "redis": True,
        "worker": True,
    }
