from __future__ import annotations

from telegram.ext import Application, CommandHandler

from app.bot.handlers import help_cmd, last_errors, ping, run_cmd, status_cmd
from app.core.settings import get_settings


def build_bot_application() -> Application:
    settings = get_settings()
    application = Application.builder().token(settings.telegram_bot_token).build()

    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("status", status_cmd))
    application.add_handler(CommandHandler("last_errors", last_errors))
    application.add_handler(CommandHandler("run", run_cmd))

    return application
