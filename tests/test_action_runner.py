from __future__ import annotations

from app.actions.runner import ActionRunner


def test_action_runner_executes_function_action() -> None:
    runner = ActionRunner()
    runner.register_function_action(name="echo", function=lambda args: " ".join(args))

    result = runner.run(action_name="echo", args=["hello", "world"])

    assert result.status == "success"
    assert result.output == "hello world"
    assert result.exit_code == 0


def test_action_runner_rejects_dangerous_argument() -> None:
    runner = ActionRunner()
    runner.register_function_action(name="echo", function=lambda args: " ".join(args))

    result = runner.run(action_name="echo", args=["hello;rm -rf /"])

    assert result.status == "rejected"
    assert "dangerous" in result.output.lower()


def test_action_runner_validates_allowed_args() -> None:
    runner = ActionRunner()
    runner.register_function_action(
        name="mode",
        function=lambda args: args[0],
        allowed_args={"safe"},
    )

    result = runner.run(action_name="mode", args=["unsafe"])

    assert result.status == "rejected"
    assert "not allowed" in result.output.lower()


def test_action_runner_command_captures_output_and_exit_code() -> None:
    runner = ActionRunner()
    runner.register_command_action(
        name="python_fail",
        command=["python3", "-c", "import sys; print('oops'); sys.exit(2)"],
    )

    result = runner.run(action_name="python_fail", args=[])

    assert result.status == "failed"
    assert result.exit_code == 2
    assert "oops" in result.output
