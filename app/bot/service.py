from __future__ import annotations

from collections.abc import Callable

from sqlmodel import Session, desc, select

from app.models.entities import ActionRun, CommandLog, Event

TaskSender = Callable[[str], None]


class BotService:
    def __init__(
        self,
        *,
        engine,
        allowed_user_ids: list[int],
        admin_user_ids: list[int],
        task_sender: TaskSender,
    ):
        self.engine = engine
        self.allowed_user_ids = set(allowed_user_ids)
        self.admin_user_ids = set(admin_user_ids)
        self.task_sender = task_sender

    def process_command(self, *, user_id: int, command: str, args: list[str]) -> str:
        if user_id not in self.allowed_user_ids:
            message = "You are not authorized to use this bot."
            self._log_command(user_id=user_id, command=command, result=message, status="denied")
            return message

        result = self._dispatch_command(user_id=user_id, command=command, args=args)
        self._log_command(user_id=user_id, command=command, result=result, status="ok")
        return result

    def _dispatch_command(self, *, user_id: int, command: str, args: list[str]) -> str:
        if command == "/ping":
            return "Pong. Courier bot is running."
        if command == "/help":
            return (
                "Available commands: /ping, /help, /status, /last_errors, /run <task>\n"
                "Run task is admin-only."
            )
        if command == "/status":
            return self._status_summary()
        if command == "/last_errors":
            return self._last_errors()
        if command == "/run":
            task = args[0] if args else ""
            return self._run_task(user_id=user_id, task_name=task)
        return "Unknown command. Use /help"

    def _status_summary(self) -> str:
        with Session(self.engine) as session:
            events = len(session.exec(select(Event)).all())
            errors = len(
                session.exec(select(Event).where(Event.status.in_(["error", "failed"]))).all()
            )
            command_logs = len(session.exec(select(CommandLog)).all())
            actions = len(session.exec(select(ActionRun)).all())

        return (
            f"Status\n"
            f"- Events: {events}\n"
            f"- Error events: {errors}\n"
            f"- Command logs: {command_logs}\n"
            f"- Action runs: {actions}"
        )

    def _last_errors(self) -> str:
        with Session(self.engine) as session:
            rows = session.exec(
                select(Event)
                .where(Event.status.in_(["error", "failed"]))
                .order_by(desc(Event.created_at))
                .limit(5)
            ).all()

        if not rows:
            return "No recent errors found."

        lines = ["Recent errors:"]
        for row in rows:
            lines.append(f"- {row.event_type} ({row.status})")
        return "\n".join(lines)

    def _run_task(self, *, user_id: int, task_name: str) -> str:
        if user_id not in self.admin_user_ids:
            return "This command requires admin role."

        if task_name != "ping_worker":
            return "Task not allowed. Allowed tasks: ping_worker"

        self.task_sender("courier.ping")
        return "Task queued: ping_worker"

    def _log_command(self, *, user_id: int, command: str, result: str, status: str) -> None:
        with Session(self.engine) as session:
            session.add(CommandLog(user_id=user_id, command=command, result=result, status=status))
            session.commit()


def create_default_bot_service(
    engine,
    allowed_user_ids: list[int],
    admin_user_ids: list[int],
    task_sender: TaskSender,
) -> BotService:
    return BotService(
        engine=engine,
        allowed_user_ids=allowed_user_ids,
        admin_user_ids=admin_user_ids,
        task_sender=task_sender,
    )
