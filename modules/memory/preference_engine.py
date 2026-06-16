from modules.memory.long_term_memory import recall


def infer_preferences():

    usage = recall("command_usage")

    if not usage:

        return {}

    sorted_usage = sorted(

        usage.items(),

        key=lambda item: item[1],

        reverse=True
    )

    preferences = {

        "most_used_command": sorted_usage[0][0]
    }

    return preferences