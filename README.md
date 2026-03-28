# Courier Bot

Courier Bot is a command-and-notification bot that lets you trigger actions and receive updates from your scripts, services, and automations in one chat interface.

## Project Goal

Build a bot that can:
- Notify you when important events happen (errors, completed jobs, warnings, deployments)
- Execute actions on request (run scripts, fetch data, trigger workflows)
- Return useful data quickly through chat commands

## Chosen Tech Stack

This stack is optimized for fast development, simplicity, and a clean path to scale.

- Runtime: **Python 3.12**
- API Framework: **FastAPI**
- Bot Framework: **python-telegram-bot**
- ORM: **SQLModel (SQLAlchemy)**
- Queue/Async Jobs: **Celery + Redis**
- Database: **SQLite**
- Scheduling: **APScheduler**
- Observability: **Sentry + structured logging (Loguru/stdlib JSON logs)**
- Packaging/Deps: **uv**
- Deployment: **Docker + Docker Compose**

## Why This Stack

- **Python** is excellent for automation, scripting, and integrations.
- **FastAPI** gives clean endpoints for external services/scripts to push events.
- **Telegram bot** is simple to use on mobile and desktop for commands and alerts.
- **SQLModel/SQLAlchemy** gives clean ORM models and easy migrations.
- **Celery + Redis** handles background actions without blocking the bot.
- **SQLite** is enough for this project because it stores a small amount of operational data.
- **Docker Compose** makes local development and deployment predictable.

## High-Level Architecture

1. External script/service sends event to `POST /events`
2. API validates payload and stores event in SQLite
3. Event is queued in Celery
4. Worker formats and sends message through Telegram bot
5. User can request actions/data via chat commands (e.g. `/status`, `/run backup`)
6. Bot calls API/action handlers and returns results

## Example Use Cases

- Send alert when a cron job fails
- Ask bot for current system health
- Trigger deploy script from chat with confirmation
- Receive daily summary of completed tasks

## Suggested Initial Commands

- `/ping` - health check
- `/status` - system/app status summary
- `/last_errors` - latest failures
- `/run <task>` - trigger whitelisted task
- `/help` - available commands

## Security Notes

- Restrict bot access to allowed Telegram user IDs/chat IDs
- Use signed tokens for `POST /events`
- Keep action runners whitelisted (never execute raw user input)
- Add role-based command permissions for sensitive actions

## Environment Variables

```env
APP_ENV=development
APP_PORT=8000

DATABASE_URL=sqlite:///./courier.db
REDIS_URL=redis://redis:6379/0

TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_ALLOWED_USER_IDS=123456789,987654321

SENTRY_DSN=
API_SHARED_SECRET=change_me
```

## Local Setup (uv)

```bash
# install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# initialize project metadata (if not initialized yet)
uv init

# add dependencies
uv add fastapi uvicorn python-telegram-bot sqlmodel sqlalchemy celery redis apscheduler sentry-sdk

# optional dev dependencies
uv add --dev pytest ruff

# run the API
uv run uvicorn app.main:app --reload --port 8000
```

## Development Roadmap

1. Scaffold FastAPI service and health endpoint
2. Add Telegram bot commands (`/ping`, `/status`)
3. Add event ingestion endpoint (`POST /events`)
4. Add Celery worker for async notifications
5. Persist events and command history with ORM models (SQLite first)
6. Add authentication/authorization rules
7. Add Docker Compose and CI tests

## Recommended Folder Structure

```text
courier/
  app/
    api/
    bot/
    workers/
    services/
    models/
    core/
  scripts/
  tests/
  docker/
  README.md
```

## Definition of Done (MVP)

- Bot receives and replies to core commands
- API accepts external events and notifies via bot
- At least one action command executes a safe script
- Logs and errors are visible and traceable
- Runs locally with Docker Compose
- SQLite keeps the system simple with low maintenance

## Next Step

Start by implementing:
1. `/ping` command in the bot
2. `POST /events` endpoint
3. Redis queue + worker that sends Telegram notifications
