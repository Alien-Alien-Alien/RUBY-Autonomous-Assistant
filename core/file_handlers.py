from modules.actions.file_actions import (
    create_file,
    create_folder,
    open_file,
    read_file
)


def handle_create_file(
    command,
    args
):

    if not args:

        return "Filename required"

    create_file(
        args[0]
    )

    return (
        f"Created file {args[0]}"
    )


def handle_open_file(
    command,
    args
):

    if not args:

        return "Filename required"

    open_file(
        args[0]
    )

    return (
        f"Opened {args[0]}"
    )


def handle_read_file(
    command,
    args
):

    if not args:

        return "Filename required"

    return read_file(
        args[0]
    )