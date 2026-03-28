from __future__ import annotations

from datetime import datetime, timedelta, timezone

from sqlmodel import Session, delete

from app.models.entities import ActionRun, CommandLog, Event


def prune_old_records(session: Session, older_than_days: int) -> dict[str, int]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=older_than_days)  # noqa: UP017

    deleted_events = session.exec(
        delete(Event).where(Event.created_at < cutoff)
    )
    deleted_command_logs = session.exec(
        delete(CommandLog).where(CommandLog.created_at < cutoff)
    )
    deleted_action_runs = session.exec(
        delete(ActionRun).where(ActionRun.created_at < cutoff)
    )

    session.commit()

    return {
        "events": deleted_events.rowcount or 0,
        "command_logs": deleted_command_logs.rowcount or 0,
        "action_runs": deleted_action_runs.rowcount or 0,
    }
