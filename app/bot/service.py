from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import logging

from sqlmodel import Session, desc, select

from app.models.entities import ActionRun, CommandLog, Event

TaskSender = Callable[[str], None]
CommandHandler = Callable[[int, list[str]], str]
logger = logging.getLogger(__name__)


@dataclass
class ActionBinding:
    name: str
    executor: Callable[[], str]
    admin_only: bool = True
    description: str = ""


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

        self.command_registry: dict[str, CommandHandler] = {}
        self.action_registry: dict[str, ActionBinding] = {}

        self._register_default_commands()
        self._register_default_actions()

    def register_command(self, command: str, handler: CommandHandler) -> None:
        self.command_registry[command] = handler

    def link_task_action(
        self,
        *,
        action_name: str,
        task_name: str,
        admin_only: bool = True,
        description: str = "",
    ) -> None:
        def _executor() -> str:
            self.task_sender(task_name)
            return f"Task queued: {action_name}"

        self.action_registry[action_name] = ActionBinding(
            name=action_name,
            executor=_executor,
            admin_only=admin_only,
            description=description,
        )

    def process_command(self, *, user_id: int, command: str, args: list[str]) -> str:
        logger.info("Processing bot command", extra={"command": command, "status": "started"})
        if user_id not in self.allowed_user_ids:
            message = "You are not authorized to use this bot."
            self._log_command(user_id=user_id, command=command, result=message, status="denied")
            return message

        handler = self.command_registry.get(command)
        if not handler:
            result = "Unknown command. Use /help"
            self._log_command(user_id=user_id, command=command, result=result, status="unknown")
            return result

        result = handler(user_id, args)
        self._log_command(user_id=user_id, command=command, result=result, status="ok")
        logger.info("Bot command processed", extra={"command": command, "status": "ok"})
        return result

    def _register_default_commands(self) -> None:
        self.register_command("/ping", self._cmd_ping)
        self.register_command("/help", self._cmd_help)
        self.register_command("/status", self._cmd_status)
        self.register_command("/last_errors", self._cmd_last_errors)
        self.register_command("/run", self._cmd_run)

    def _register_default_actions(self) -> None:
        self.link_task_action(
            action_name="ping_worker",
            task_name="courier.ping",
            admin_only=True,
            description="Send a ping task to Celery worker",
        )

    def _cmd_ping(self, _user_id: int, _args: list[str]) -> str:
        return "Pong. Courier bot is running."

    def _cmd_help(self, _user_id: int, _args: list[str]) -> str:
        command_list = ", ".join(sorted(self.command_registry.keys()))
        action_list = ", ".join(sorted(self.action_registry.keys())) or "none"
        return (
            f"Available commands: {command_list}\n"
            f"Run usage: /run <action_name>\n"
            f"Available actions: {action_list}"
        )

    def _cmd_status(self, _user_id: int, _args: list[str]) -> str:
        return self._status_summary()

    def _cmd_last_errors(self, _user_id: int, _args: list[str]) -> str:
        return self._last_errors()

    def _cmd_run(self, user_id: int, args: list[str]) -> str:
        action_name = args[0] if args else ""
        if not action_name:
            return "Missing action name. Usage: /run <action_name>"

        action = self.action_registry.get(action_name)
        if not action:
            allowed = ", ".join(sorted(self.action_registry.keys())) or "none"
            return f"Action not allowed. Allowed actions: {allowed}"

        if action.admin_only and user_id not in self.admin_user_ids:
            return "This command requires admin role."

        return action.executor()

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
