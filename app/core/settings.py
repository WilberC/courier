from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Settings:
    app_env: str
    app_port: int
    database_url: str
    redis_url: str
    telegram_bot_token: str
    telegram_allowed_user_ids: list[int]
    telegram_admin_user_ids: list[int]
    api_shared_secret: str
    event_rate_limit_per_minute: int
    event_max_payload_bytes: int
    sentry_dsn: str | None = None

    @property
    def is_production(self) -> bool:
        return self.app_env.lower() == "production"

    def validate_required(self) -> None:
        missing: list[str] = []

        if self.is_production:
            if not self.telegram_bot_token:
                missing.append("TELEGRAM_BOT_TOKEN")
            if not self.api_shared_secret:
                missing.append("API_SHARED_SECRET")
            if not self.telegram_allowed_user_ids:
                missing.append("TELEGRAM_ALLOWED_USER_IDS")

        if not self.database_url:
            missing.append("DATABASE_URL")
        if not self.redis_url:
            missing.append("REDIS_URL")

        if missing:
            raise ValueError(
                "Missing required environment variables: " + ", ".join(sorted(set(missing)))
            )


def _parse_allowed_user_ids(raw: str) -> list[int]:
    values = [chunk.strip() for chunk in raw.split(",") if chunk.strip()]
    if not values:
        return []
    try:
        return [int(value) for value in values]
    except ValueError as exc:
        raise ValueError(
            "TELEGRAM_ALLOWED_USER_IDS must be a comma-separated list of integers"
        ) from exc


def _parse_positive_int(name: str, raw: str, default: int) -> int:
    value = raw.strip() if raw else ""
    if not value:
        return default
    try:
        parsed = int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if parsed <= 0:
        raise ValueError(f"{name} must be > 0")
    return parsed


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    app_env = os.getenv("APP_ENV", "development")

    # Safe local defaults: easy startup for development, strict checks in production.
    token_default = "dev-placeholder-token" if app_env != "production" else ""
    secret_default = "dev-shared-secret" if app_env != "production" else ""
    allowed_ids_default = "1" if app_env != "production" else ""
    admin_ids_default = allowed_ids_default

    settings = Settings(
        app_env=app_env,
        app_port=int(os.getenv("APP_PORT", "8000")),
        database_url=os.getenv("DATABASE_URL", "sqlite:///./courier.db"),
        redis_url=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        telegram_bot_token=os.getenv("TELEGRAM_BOT_TOKEN", token_default),
        telegram_allowed_user_ids=_parse_allowed_user_ids(
            os.getenv("TELEGRAM_ALLOWED_USER_IDS", allowed_ids_default)
        ),
        telegram_admin_user_ids=_parse_allowed_user_ids(
            os.getenv("TELEGRAM_ADMIN_USER_IDS", admin_ids_default)
        ),
        api_shared_secret=os.getenv("API_SHARED_SECRET", secret_default),
        event_rate_limit_per_minute=_parse_positive_int(
            "EVENT_RATE_LIMIT_PER_MINUTE",
            os.getenv("EVENT_RATE_LIMIT_PER_MINUTE", ""),
            60,
        ),
        event_max_payload_bytes=_parse_positive_int(
            "EVENT_MAX_PAYLOAD_BYTES",
            os.getenv("EVENT_MAX_PAYLOAD_BYTES", ""),
            32768,
        ),
        sentry_dsn=os.getenv("SENTRY_DSN") or None,
    )
    settings.validate_required()
    return settings
