from __future__ import annotations

from telegram.ext import Application, CommandHandler

from app.bot.handlers import help_cmd, last_errors, ping, run_cmd, status_cmd
from app.core.observability import configure_logging, init_sentry_if_enabled
from app.core.settings import Settings, get_settings
from app.db.session import get_engine
from app.db.users import upsert_telegram_user
from sqlmodel import Session


def seed_users_from_settings(engine, settings: Settings) -> None:
    from app.db.init_db import init_db

    init_db(engine)
    admin_ids = set(settings.telegram_admin_user_ids)
    with Session(engine) as session:
        for uid in admin_ids:
            upsert_telegram_user(session, uid, role="admin")
        for uid in settings.telegram_allowed_user_ids:
            if uid not in admin_ids:
                upsert_telegram_user(session, uid, role="user")


def build_bot_application() -> Application:
    settings = get_settings()
    configure_logging()
    init_sentry_if_enabled(settings)
    application = Application.builder().token(settings.telegram_bot_token).build()

    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("status", status_cmd))
    application.add_handler(CommandHandler("last_errors", last_errors))
    application.add_handler(CommandHandler("run", run_cmd))

    seed_users_from_settings(get_engine(), settings)

    return application
