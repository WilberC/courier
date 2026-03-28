from __future__ import annotations

import pytest

from app.api.rate_limit import FixedWindowRateLimiter
from app.main import app


@pytest.fixture(autouse=True)
def _reset_test_app_state():
    from app.api import events as events_module

    events_module.rate_limiter = FixedWindowRateLimiter(
        limit=max(events_module.settings.event_rate_limit_per_minute, 1)
    )

    yield

    app.dependency_overrides.clear()
    events_module.rate_limiter = FixedWindowRateLimiter(
        limit=max(events_module.settings.event_rate_limit_per_minute, 1)
    )
