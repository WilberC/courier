# Courier Bot Implementation Phases

This document tracks everything needed to configure and deliver the project in small, verifiable phases.

## Global Engineering Policy (Applies To All Phases)

### TDD Policy (Mandatory)
- [ ] Use TDD for every change from now on: `RED -> GREEN -> REFACTOR`
- [ ] No code change is complete without automated tests
- [ ] For already-implemented code, add missing tests before or during next related change
- [ ] No merge allowed with failing tests

### Coverage Policy (Mandatory)
- [ ] Track coverage in CI for every pull request
- [ ] Global minimum coverage: **85%**
- [ ] Critical paths minimum coverage: **90%** (`app/api`, `app/workers`, `app/core`)
- [ ] Every bug fix must include a regression test
- [ ] Coverage must not decrease on modified files

## Phase 0 - Project Bootstrap

Note: for this project, the normal local runtime should use Docker Compose so API, worker, and Redis run together consistently.

### Repository Setup Checklist
- [x] Create base folders: `app/`, `tests/`, `scripts/`, `docs/`
- [x] Keep `README.md` and `.gitignore` up to date
- [x] Add `pyproject.toml` using `uv init`
- [x] Define Python version (3.12)
- [x] Add Docker baseline files (`Dockerfile`, `.dockerignore`, `docker-compose.yml`)

### Dependencies Checklist
- [x] Add runtime deps: `fastapi`, `uvicorn`, `python-telegram-bot`, `sqlmodel`, `sqlalchemy`, `celery`, `redis`, `apscheduler`, `sentry-sdk`
- [x] Add dev deps: `pytest`, `ruff`
- [x] Confirm app boots without import errors
- [x] Add coverage tooling: `pytest-cov`

## Phase 1 - Core Configuration

### Environment Variables Checklist
- [x] Create `.env.example` with required keys
- [x] Configure `APP_ENV`
- [x] Configure `APP_PORT`
- [x] Configure `DATABASE_URL` (SQLite)
- [x] Configure `REDIS_URL`
- [x] Configure `TELEGRAM_BOT_TOKEN`
- [x] Configure `TELEGRAM_ALLOWED_USER_IDS`
- [x] Configure `API_SHARED_SECRET`
- [x] Configure optional `SENTRY_DSN`

### App Settings Checklist
- [x] Centralize settings loader in `app/core/settings.py`
- [x] Validate required environment variables at startup
- [x] Add safe defaults for local development

## Phase 2 - Database (SQLite + ORM)

### Data Layer Checklist
- [x] Create ORM models with SQLModel
- [x] Define initial entities:
- [x] `Event` (source, type, payload, status, created_at)
- [x] `CommandLog` (user_id, command, result, created_at)
- [x] `ActionRun` (action_name, status, output, created_at)
- [x] Add DB session management
- [x] Add DB initialization on startup

### Persistence Checklist
- [x] Confirm records are created/read correctly
- [x] Add indexes for common lookups (status, created_at)
- [x] Add retention plan for old logs/events

## Phase 3 - API Service (FastAPI)

### API Checklist
- [x] Create `/health` endpoint
- [x] Create `POST /events` endpoint
- [x] Validate request schema
- [x] Add auth for ingestion endpoint (shared secret)
- [x] Return clear success/error responses

### API Safety Checklist
- [x] Rate limit or throttle inbound events if needed
- [x] Reject oversized payloads
- [x] Sanitize/normalize event metadata

## Phase 4 - Bot Service (Telegram)

### Bot Commands Checklist
- [x] `/ping` command
- [x] `/help` command
- [x] `/status` command
- [x] `/last_errors` command
- [x] `/run <task>` command (whitelisted)

### Access Control Checklist
- [x] Restrict commands to allowed user IDs
- [x] Add role split (admin vs viewer) if needed
- [x] Log each command usage

## Phase 5 - Background Jobs (Celery + Redis)

### Queue Configuration Checklist
- [x] Configure Celery app and Redis broker
- [x] Define notification task(s)
- [x] Define action execution task(s)
- [x] Add retry policy for transient failures

### Worker Behavior Checklist
- [x] Ensure idempotent tasks where possible
- [x] Persist task outcomes to DB
- [x] Notify bot on task success/failure

## Phase 6 - Actions and Script Integration

### Action Runner Checklist
- [x] Build a whitelist registry for allowed actions
- [x] Map action name -> script/function
- [x] Validate command args before execution
- [x] Capture stdout/stderr and exit code
- [x] Apply execution timeout per action

### Safety Checklist
- [x] Never execute raw user input as shell command
- [x] Block dangerous parameters
- [x] Audit-log every action run

## Phase 7 - Observability and Reliability

### Logging Checklist
- [x] Add structured logging
- [x] Include correlation IDs (event ID, task ID)
- [x] Log incoming events, bot commands, task lifecycle

### Error Monitoring Checklist
- [x] Configure Sentry
- [x] Capture API exceptions
- [x] Capture worker exceptions
- [x] Capture bot command exceptions

### Reliability Checklist
- [x] Add graceful shutdown handling
- [x] Add retry/backoff for Telegram API failures
- [x] Add health checks for API/worker/redis

## Phase 8 - Testing and Quality

Goal: implement and enforce the global TDD + coverage policies in automation (CI + local commands).

### Test Checklist
- [x] Unit tests for settings and validators
- [x] Unit tests for bot command handlers
- [x] API tests for `/health` and `POST /events`
- [x] Worker tests for notification/action tasks
- [x] Permission tests (authorized vs unauthorized user)
- [ ] Add regression test for every production bug before applying fix
- [x] Add integration tests for API -> queue -> worker flow

### TDD Workflow Checklist
- [ ] `RED`: write failing test for new behavior
- [ ] `GREEN`: implement minimum code to pass test
- [ ] `REFACTOR`: improve code while keeping tests green
- [ ] Keep tests isolated and deterministic (no flaky external dependencies)
- [ ] Use fixtures/mocks for external services (Telegram, Redis) in unit tests

### Test Execution Checklist
- [ ] Local quick run: `uv run pytest -q`
- [x] Lint + tests gate: `uv run ruff check app tests && uv run pytest -q`
- [x] Coverage run: `uv run pytest --cov=app --cov-report=term-missing --cov-fail-under=85`
- [ ] Docker verification run: `docker compose run --rm api pytest -q`
- [x] CI must block merge on any failing test
- [x] CI must block merge on coverage below threshold

### Code Quality Checklist
- [x] Add Ruff config and run lint checks
- [x] Add basic formatting/lint step to CI
- [ ] Ensure zero failing tests before merge

## Phase 9 - Local Deployment and Operations

### Docker Compose Checklist
- [x] Add API service
- [x] Add worker service
- [x] Add Redis service
- [x] Mount local SQLite volume
- [x] Add restart policies

### Runbook Checklist
- [x] Document how to start all services
- [x] Document how to rotate bot token
- [x] Document backup/restore for SQLite file
- [x] Document common failure recovery steps

## Phase 10 - MVP Exit Criteria

- [ ] Bot responds to core commands reliably
- [x] External scripts can push events successfully
- [x] Events generate notifications through worker
- [x] One safe action can be triggered from chat
- [x] Logs + errors are observable
- [x] System can be started locally in one command
- [ ] All implemented features are covered by tests and passing

## Nice-to-Have (After MVP)

- [ ] Daily/weekly summary notifications
- [ ] Rich dashboards for event/action history
- [ ] Multi-chat or multi-tenant support
- [ ] Optional migration path from SQLite to PostgreSQL
- [ ] Web UI for action approvals
