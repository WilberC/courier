from __future__ import annotations

import asyncio
from types import SimpleNamespace

from telegram.error import TimedOut

from app.bot import handlers


class _FakeMessage:
    def __init__(self) -> None:
        self.replies: list[str] = []

    async def reply_text(self, message: str) -> None:
        self.replies.append(message)


class _FlakyMessage:
    def __init__(self) -> None:
        self.calls = 0
        self.replies: list[str] = []

    async def reply_text(self, message: str) -> None:
        self.calls += 1
        if self.calls == 1:
            raise TimedOut("temporary")
        self.replies.append(message)


class _FakeService:
    def __init__(self, response: str) -> None:
        self.response = response
        self.calls: list[tuple[int, str, list[str]]] = []

    def process_command(self, *, user_id: int, command: str, args: list[str]) -> str:
        self.calls.append((user_id, command, args))
        return self.response


def test_ping_handler_uses_service_and_replies(monkeypatch) -> None:
    fake_service = _FakeService("ok")
    monkeypatch.setattr(handlers, "service", fake_service)

    message = _FakeMessage()
    update = SimpleNamespace(effective_user=SimpleNamespace(id=7), message=message)
    context = SimpleNamespace(args=[])

    asyncio.run(handlers.ping(update, context))

    assert fake_service.calls == [(7, "/ping", [])]
    assert message.replies == ["ok"]


def test_run_handler_passes_args(monkeypatch) -> None:
    fake_service = _FakeService("queued")
    monkeypatch.setattr(handlers, "service", fake_service)

    message = _FakeMessage()
    update = SimpleNamespace(effective_user=SimpleNamespace(id=7), message=message)
    context = SimpleNamespace(args=["ping_worker"])

    asyncio.run(handlers.run_cmd(update, context))

    assert fake_service.calls == [(7, "/run", ["ping_worker"])]


def test_handle_retries_on_telegram_timeout(monkeypatch) -> None:
    fake_service = _FakeService("ok")
    monkeypatch.setattr(handlers, "service", fake_service)

    message = _FlakyMessage()
    update = SimpleNamespace(effective_user=SimpleNamespace(id=7), message=message)
    context = SimpleNamespace(args=[])

    asyncio.run(handlers.ping(update, context))

    assert message.replies == ["ok"]
