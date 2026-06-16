from modules.memory.long_term_memory import (

    remember,

    recall
)


def store_experience(command):

    # Store last command
    remember(

        "last_command",

        command
    )

    # Track repeated usage
    usage = recall("command_usage")

    if usage is None:

        usage = {}

    usage[command] = usage.get(command, 0) + 1

    remember(

        "command_usage",

        usage
    )