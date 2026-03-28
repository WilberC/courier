from __future__ import annotations

import logging
import subprocess
from dataclasses import dataclass, field
from typing import Callable

logger = logging.getLogger(__name__)

ActionCallable = Callable[[list[str]], str]

_DANGEROUS_CHUNKS = (";", "|", "&", ">", "<", "`", "$(", "..", "\x00")


@dataclass(frozen=True)
class ActionResult:
    action_name: str
    status: str
    output: str
    exit_code: int | None = None


@dataclass(frozen=True)
class ActionSpec:
    name: str
    timeout_seconds: int = 30
    allowed_args: set[str] = field(default_factory=set)
    command: tuple[str, ...] | None = None
    function: ActionCallable | None = None

    def validate(self) -> None:
        if (self.command is None and self.function is None) or (
            self.command is not None and self.function is not None
        ):
            raise ValueError("ActionSpec must define exactly one executor: command or function")
        if self.timeout_seconds <= 0:
            raise ValueError("ActionSpec.timeout_seconds must be > 0")


class ActionRunner:
    def __init__(self) -> None:
        self._actions: dict[str, ActionSpec] = {}

    def register_command_action(
        self,
        *,
        name: str,
        command: list[str],
        timeout_seconds: int = 30,
        allowed_args: set[str] | None = None,
    ) -> None:
        if not command:
            raise ValueError("command cannot be empty")
        spec = ActionSpec(
            name=name,
            command=tuple(command),
            timeout_seconds=timeout_seconds,
            allowed_args=allowed_args or set(),
        )
        spec.validate()
        self._actions[name] = spec

    def register_function_action(
        self,
        *,
        name: str,
        function: ActionCallable,
        timeout_seconds: int = 30,
        allowed_args: set[str] | None = None,
    ) -> None:
        spec = ActionSpec(
            name=name,
            function=function,
            timeout_seconds=timeout_seconds,
            allowed_args=allowed_args or set(),
        )
        spec.validate()
        self._actions[name] = spec

    def list_actions(self) -> list[str]:
        return sorted(self._actions.keys())

    def run(self, *, action_name: str, args: list[str]) -> ActionResult:
        spec = self._actions.get(action_name)
        if spec is None:
            return ActionResult(
                action_name=action_name,
                status="not_allowed",
                output=f"Action not allowed: {action_name}",
            )

        validation_error = self._validate_args(spec=spec, args=args)
        if validation_error:
            return ActionResult(
                action_name=action_name,
                status="rejected",
                output=validation_error,
            )

        try:
            if spec.function is not None:
                output = spec.function(args)
                return ActionResult(
                    action_name=action_name,
                    status="success",
                    output=output.strip(),
                    exit_code=0,
                )
            return self._run_command(spec=spec, args=args)
        except Exception as exc:  # pragma: no cover - defensive fallback
            logger.exception("Action execution failed", extra={"action_name": action_name})
            return ActionResult(
                action_name=action_name,
                status="error",
                output=f"Unhandled action error: {exc}",
            )

    def _validate_args(self, *, spec: ActionSpec, args: list[str]) -> str | None:
        for arg in args:
            stripped = arg.strip()
            if not stripped:
                return "Empty arguments are not allowed"
            if len(stripped) > 200:
                return "Argument too long"
            if any(chunk in stripped for chunk in _DANGEROUS_CHUNKS):
                return f"Blocked dangerous argument: {arg}"
            if spec.allowed_args and stripped not in spec.allowed_args:
                allowed = ", ".join(sorted(spec.allowed_args))
                return f"Argument not allowed: {arg}. Allowed: {allowed}"
        return None

    def _run_command(self, *, spec: ActionSpec, args: list[str]) -> ActionResult:
        assert spec.command is not None  # nosec B101
        completed = subprocess.run(
            [*spec.command, *args],
            capture_output=True,
            text=True,
            timeout=spec.timeout_seconds,
            shell=False,
            check=False,
        )
        output = _compose_output(completed.stdout, completed.stderr).strip()
        return ActionResult(
            action_name=spec.name,
            status="success" if completed.returncode == 0 else "failed",
            output=output,
            exit_code=completed.returncode,
        )


def _compose_output(stdout: str, stderr: str) -> str:
    chunks: list[str] = []
    if stdout.strip():
        chunks.append(stdout.strip())
    if stderr.strip():
        chunks.append(f"stderr: {stderr.strip()}")
    return "\n".join(chunks)
