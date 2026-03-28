from __future__ import annotations

from datetime import datetime, timedelta, timezone

from sqlalchemy import text
from sqlmodel import Session, SQLModel, create_engine, select

from app.db.init_db import init_db
from app.db.retention import prune_old_records
from app.models.entities import ActionRun, CommandLog, Event


def _engine_for_test():
    return create_engine("sqlite://", connect_args={"check_same_thread": False})


def test_init_db_creates_required_tables() -> None:
    engine = _engine_for_test()

    init_db(engine)

    with engine.connect() as conn:
        tables = {
            row[0]
            for row in conn.execute(
                text("SELECT name FROM sqlite_master WHERE type='table'")
            ).fetchall()
        }

    assert "event" in tables
    assert "commandlog" in tables
    assert "actionrun" in tables


def test_can_persist_and_read_phase2_entities() -> None:
    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        event = Event(source="cron", event_type="job.finished", payload={"job": "backup"})
        cmd = CommandLog(user_id=123, command="/status", result="ok")
        run = ActionRun(action_name="backup", status="success", output="done")
        session.add(event)
        session.add(cmd)
        session.add(run)
        session.commit()

        persisted_event = session.exec(select(Event)).one()
        persisted_cmd = session.exec(select(CommandLog)).one()
        persisted_run = session.exec(select(ActionRun)).one()

    assert persisted_event.source == "cron"
    assert persisted_event.payload["job"] == "backup"
    assert persisted_cmd.command == "/status"
    assert persisted_run.action_name == "backup"


def test_status_and_created_at_indexes_exist() -> None:
    engine = _engine_for_test()

    init_db(engine)

    with engine.connect() as conn:
        event_indexes = {
            row[1] for row in conn.execute(text("PRAGMA index_list('event')")).fetchall()
        }
        command_indexes = {
            row[1] for row in conn.execute(text("PRAGMA index_list('commandlog')")).fetchall()
        }
        action_indexes = {
            row[1] for row in conn.execute(text("PRAGMA index_list('actionrun')")).fetchall()
        }

    # SQLModel naming is dialect-generated; we assert indexed columns through index names.
    assert any("status" in name for name in event_indexes)
    assert any("created_at" in name for name in event_indexes)
    assert any("status" in name for name in command_indexes)
    assert any("created_at" in name for name in command_indexes)
    assert any("status" in name for name in action_indexes)
    assert any("created_at" in name for name in action_indexes)


def test_retention_prunes_old_logs_events_and_action_runs() -> None:
    engine = _engine_for_test()
    SQLModel.metadata.create_all(engine)

    old_ts = datetime.now(timezone.utc) - timedelta(days=90)  # noqa: UP017
    recent_ts = datetime.now(timezone.utc) - timedelta(days=2)  # noqa: UP017

    with Session(engine) as session:
        session.add(Event(source="cron", event_type="old", payload={}, created_at=old_ts))
        session.add(Event(source="cron", event_type="recent", payload={}, created_at=recent_ts))

        session.add(CommandLog(user_id=1, command="/old", result="x", created_at=old_ts))
        session.add(CommandLog(user_id=1, command="/recent", result="y", created_at=recent_ts))

        session.add(ActionRun(action_name="old", status="failed", output="x", created_at=old_ts))
        session.add(
            ActionRun(
                action_name="recent",
                status="success",
                output="y",
                created_at=recent_ts,
            )
        )
        session.commit()

        deleted = prune_old_records(session, older_than_days=30)

        events = session.exec(select(Event)).all()
        commands = session.exec(select(CommandLog)).all()
        actions = session.exec(select(ActionRun)).all()

    assert deleted["events"] == 1
    assert deleted["command_logs"] == 1
    assert deleted["action_runs"] == 1

    assert len(events) == 1 and events[0].event_type == "recent"
    assert len(commands) == 1 and commands[0].command == "/recent"
    assert len(actions) == 1 and actions[0].action_name == "recent"
