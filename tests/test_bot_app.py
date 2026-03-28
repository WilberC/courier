from __future__ import annotations

from app.bot import app as bot_app_module


class _FakeApplication:
    def __init__(self) -> None:
        self.handlers = []

    def add_handler(self, handler) -> None:
        self.handlers.append(handler)


class _FakeBuilder:
    def __init__(self, app: _FakeApplication) -> None:
        self.app = app
        self.token_value = None

    def token(self, value: str):
        self.token_value = value
        return self

    def build(self) -> _FakeApplication:
        return self.app


class _FakeApplicationFactory:
    def __init__(self) -> None:
        self.app = _FakeApplication()
        self.builder_instance = _FakeBuilder(self.app)

    def builder(self) -> _FakeBuilder:
        return self.builder_instance


def test_build_bot_application_registers_handlers(monkeypatch) -> None:
    fake_factory = _FakeApplicationFactory()

    monkeypatch.setattr(bot_app_module, "Application", fake_factory)

    application = bot_app_module.build_bot_application()

    assert application is fake_factory.app
    assert fake_factory.builder_instance.token_value is not None
    assert len(application.handlers) == 5
