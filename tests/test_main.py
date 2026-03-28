from app.main import startup_validation


def test_startup_validation_runs_without_error() -> None:
    startup_validation()
