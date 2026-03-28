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
REDIS_URL=redis://localhost:6379/0

TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_ALLOWED_USER_IDS=123456789,987654321

SENTRY_DSN=
API_SHARED_SECRET=change_me
```

## Prerequisites

- Python **3.12+**
- Docker + Docker Compose
- `uv` (recommended) or `pip` + virtualenv

## Install

### Option A (Recommended): uv

```bash
# install uv (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# install dependencies from pyproject.toml
uv sync
```

### Option B: pip + venv

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest ruff
```

## Configuration

```bash
cp .env.example .env
```

Update `.env` with your values:
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_ALLOWED_USER_IDS`
- `API_SHARED_SECRET`

## Run

### Option A (Recommended): Docker Compose (normal run)

```bash
cp .env.example .env
docker compose up --build -d
```

Services:
- API: `http://127.0.0.1:8000`
- Redis: `127.0.0.1:6380`
- Worker: Celery worker connected to Redis

Check logs:

```bash
docker compose logs -f api worker redis
```

Stop:

```bash
docker compose down
```

### Option B: Run API locally (without Docker)

```bash
uv run uvicorn app.main:app --reload --port 8000
```

If you use `pip + venv`, run:

```bash
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

### Health Check

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok","env":"development"}
```

## Development Commands

```bash
# lint
uv run ruff check app tests

# run tests
uv run pytest -q

# quick import/boot sanity check
uv run python -c "from fastapi.testclient import TestClient; from app.main import app; print(TestClient(app).get('/health').json())"
```

## Testing Strategy (TDD Required)

This project uses **TDD by default** for **all phases** (including already implemented modules):
1. Write a failing test first (`RED`)
2. Implement the smallest change to pass (`GREEN`)
3. Refactor safely while tests stay green (`REFACTOR`)

Rules for all new features and fixes:
- Add or update tests before implementing behavior changes
- Do not merge changes with failing tests
- Keep unit + integration coverage for critical paths (API, worker, bot commands, permissions)
- Add missing tests for previously implemented code whenever you touch it

Recommended loop:

```bash
# 1) run a focused test while implementing
uv run pytest -q tests

# 2) run full checks before merge
uv run ruff check app tests
uv run pytest -q
uv run pytest --cov=app --cov-report=term-missing --cov-fail-under=85
```

Docker test run:

```bash
docker compose run --rm api pytest -q
docker compose run --rm api pytest --cov=app --cov-report=term-missing --cov-fail-under=85
```

Coverage gates:
- Global minimum: **85%**
- Critical paths (`app/api`, `app/workers`, `app/core`): target **90%+**

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
