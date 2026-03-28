# Courier Bot Implementation Phases

This document tracks everything needed to configure and deliver the project in small, verifiable phases.

## Phase 0 - Project Bootstrap

### Repository Setup Checklist
- [ ] Create base folders: `app/`, `tests/`, `scripts/`, `docs/`
- [ ] Keep `README.md` and `.gitignore` up to date
- [ ] Add `pyproject.toml` using `uv init`
- [ ] Define Python version (3.12)

### Dependencies Checklist
- [ ] Add runtime deps: `fastapi`, `uvicorn`, `python-telegram-bot`, `sqlmodel`, `sqlalchemy`, `celery`, `redis`, `apscheduler`, `sentry-sdk`
- [ ] Add dev deps: `pytest`, `ruff`
- [ ] Confirm app boots without import errors

## Phase 1 - Core Configuration

### Environment Variables Checklist
- [ ] Create `.env.example` with required keys
- [ ] Configure `APP_ENV`
- [ ] Configure `APP_PORT`
- [ ] Configure `DATABASE_URL` (SQLite)
- [ ] Configure `REDIS_URL`
- [ ] Configure `TELEGRAM_BOT_TOKEN`
- [ ] Configure `TELEGRAM_ALLOWED_USER_IDS`
- [ ] Configure `API_SHARED_SECRET`
- [ ] Configure optional `SENTRY_DSN`

### App Settings Checklist
- [ ] Centralize settings loader in `app/core/settings.py`
- [ ] Validate required environment variables at startup
- [ ] Add safe defaults for local development

## Phase 2 - Database (SQLite + ORM)

### Data Layer Checklist
- [ ] Create ORM models with SQLModel
- [ ] Define initial entities:
- [ ] `Event` (source, type, payload, status, created_at)
- [ ] `CommandLog` (user_id, command, result, created_at)
- [ ] `ActionRun` (action_name, status, output, created_at)
- [ ] Add DB session management
- [ ] Add DB initialization on startup

### Persistence Checklist
- [ ] Confirm records are created/read correctly
- [ ] Add indexes for common lookups (status, created_at)
- [ ] Add retention plan for old logs/events

## Phase 3 - API Service (FastAPI)

### API Checklist
- [ ] Create `/health` endpoint
- [ ] Create `POST /events` endpoint
- [ ] Validate request schema
- [ ] Add auth for ingestion endpoint (shared secret)
- [ ] Return clear success/error responses

### API Safety Checklist
- [ ] Rate limit or throttle inbound events if needed
- [ ] Reject oversized payloads
- [ ] Sanitize/normalize event metadata

## Phase 4 - Bot Service (Telegram)

### Bot Commands Checklist
- [ ] `/ping` command
- [ ] `/help` command
- [ ] `/status` command
- [ ] `/last_errors` command
- [ ] `/run <task>` command (whitelisted)

### Access Control Checklist
- [ ] Restrict commands to allowed user IDs
- [ ] Add role split (admin vs viewer) if needed
- [ ] Log each command usage

## Phase 5 - Background Jobs (Celery + Redis)

### Queue Configuration Checklist
- [ ] Configure Celery app and Redis broker
- [ ] Define notification task(s)
- [ ] Define action execution task(s)
- [ ] Add retry policy for transient failures

### Worker Behavior Checklist
- [ ] Ensure idempotent tasks where possible
- [ ] Persist task outcomes to DB
- [ ] Notify bot on task success/failure

## Phase 6 - Actions and Script Integration

### Action Runner Checklist
- [ ] Build a whitelist registry for allowed actions
- [ ] Map action name -> script/function
- [ ] Validate command args before execution
- [ ] Capture stdout/stderr and exit code
- [ ] Apply execution timeout per action

### Safety Checklist
- [ ] Never execute raw user input as shell command
- [ ] Block dangerous parameters
- [ ] Audit-log every action run

## Phase 7 - Observability and Reliability

### Logging Checklist
- [ ] Add structured logging
- [ ] Include correlation IDs (event ID, task ID)
- [ ] Log incoming events, bot commands, task lifecycle

### Error Monitoring Checklist
- [ ] Configure Sentry
- [ ] Capture API exceptions
- [ ] Capture worker exceptions
- [ ] Capture bot command exceptions

### Reliability Checklist
- [ ] Add graceful shutdown handling
- [ ] Add retry/backoff for Telegram API failures
- [ ] Add health checks for API/worker/redis

## Phase 8 - Testing and Quality

### Test Checklist
- [ ] Unit tests for settings and validators
- [ ] Unit tests for bot command handlers
- [ ] API tests for `/health` and `POST /events`
- [ ] Worker tests for notification/action tasks
- [ ] Permission tests (authorized vs unauthorized user)

### Code Quality Checklist
- [ ] Add Ruff config and run lint checks
- [ ] Add basic formatting/lint step to CI
- [ ] Ensure zero failing tests before merge

## Phase 9 - Local Deployment and Operations

### Docker Compose Checklist
- [ ] Add API service
- [ ] Add worker service
- [ ] Add Redis service
- [ ] Mount local SQLite volume
- [ ] Add restart policies

### Runbook Checklist
- [ ] Document how to start all services
- [ ] Document how to rotate bot token
- [ ] Document backup/restore for SQLite file
- [ ] Document common failure recovery steps

## Phase 10 - MVP Exit Criteria

- [ ] Bot responds to core commands reliably
- [ ] External scripts can push events successfully
- [ ] Events generate notifications through worker
- [ ] One safe action can be triggered from chat
- [ ] Logs + errors are observable
- [ ] System can be started locally in one command

## Nice-to-Have (After MVP)

- [ ] Daily/weekly summary notifications
- [ ] Rich dashboards for event/action history
- [ ] Multi-chat or multi-tenant support
- [ ] Optional migration path from SQLite to PostgreSQL
- [ ] Web UI for action approvals

