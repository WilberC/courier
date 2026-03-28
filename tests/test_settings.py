import pytest

from app.core import settings as settings_module


def _clear_settings_cache() -> None:
    settings_module.get_settings.cache_clear()


def test_get_settings_uses_safe_defaults_in_development(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.delenv("API_SHARED_SECRET", raising=False)
    monkeypatch.delenv("TELEGRAM_ALLOWED_USER_IDS", raising=False)
    _clear_settings_cache()

    settings = settings_module.get_settings()

    assert settings.app_env == "development"
    assert settings.telegram_bot_token == "dev-placeholder-token"
    assert settings.api_shared_secret == "dev-shared-secret"
    assert settings.telegram_allowed_user_ids == [1]


def test_get_settings_validates_production_required_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.delenv("API_SHARED_SECRET", raising=False)
    monkeypatch.delenv("TELEGRAM_ALLOWED_USER_IDS", raising=False)
    _clear_settings_cache()

    with pytest.raises(ValueError) as excinfo:
        settings_module.get_settings()

    message = str(excinfo.value)
    assert "TELEGRAM_BOT_TOKEN" in message
    assert "API_SHARED_SECRET" in message
    assert "TELEGRAM_ALLOWED_USER_IDS" in message


def test_parse_allowed_user_ids_rejects_invalid_values() -> None:
    with pytest.raises(ValueError):
        settings_module._parse_allowed_user_ids("1,abc,3")


def test_validate_required_rejects_empty_database_and_redis_urls() -> None:
    settings = settings_module.Settings(
        app_env="development",
        app_port=8000,
        database_url="",
        redis_url="",
        telegram_bot_token="dev-token",
        telegram_allowed_user_ids=[1],
        api_shared_secret="dev-secret",
    )

    with pytest.raises(ValueError) as excinfo:
        settings.validate_required()

    message = str(excinfo.value)
    assert "DATABASE_URL" in message
    assert "REDIS_URL" in message
