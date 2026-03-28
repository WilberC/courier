from __future__ import annotations

import asyncio
import logging

from sentry_sdk import capture_exception
from telegram import Update
from telegram.error import NetworkError, RetryAfter, TimedOut
from telegram.ext import ContextTypes

from app.bot.service import BotService
from app.core.settings import get_settings
from app.db.session import get_engine
from app.workers.celery_app import celery_app

settings = get_settings()
logger = logging.getLogger(__name__)


def _task_sender(task_name: str) -> None:
    celery_app.send_task(task_name)


service = BotService(
    engine=get_engine(),
    allowed_user_ids=settings.telegram_allowed_user_ids,
    admin_user_ids=settings.telegram_admin_user_ids,
    task_sender=_task_sender,
)


async def _handle(update: Update, context: ContextTypes.DEFAULT_TYPE, command: str) -> None:
    user_id = update.effective_user.id if update.effective_user else -1
    args = getattr(context, "args", [])
    try:
        message = service.process_command(user_id=user_id, command=command, args=args)
        if update.message:
            await _safe_reply(update, message)
    except Exception as exc:
        logger.exception("Bot command handler failure", extra={"command": command})
        capture_exception(exc)
        if update.message:
            await _safe_reply(update, "Unexpected error while processing command.")


async def _safe_reply(update: Update, message: str, max_attempts: int = 3) -> None:
    if not update.message:
        return

    for attempt in range(1, max_attempts + 1):
        try:
            await update.message.reply_text(message)
            return
        except RetryAfter as exc:
            await asyncio.sleep(float(exc.retry_after))
        except (TimedOut, NetworkError):
            if attempt == max_attempts:
                raise
            await asyncio.sleep(0.25 * (2 ** (attempt - 1)))


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _handle(update, context, "/ping")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _handle(update, context, "/help")


async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _handle(update, context, "/status")


async def last_errors(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _handle(update, context, "/last_errors")


async def run_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await _handle(update, context, "/run")
