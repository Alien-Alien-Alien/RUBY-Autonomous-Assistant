from modules.actions.code_actions import (
    run_python_file
)


def handle_run_python(
    command,
    args
):

    if not args:

        return (
            "Filename required"
        )

    return run_python_file(
        args[0]
    )