import re

from core.grammar_registry import get_grammars


def parse_command(command):

    command = command.lower().strip()

    # Grammar-based parsing
    for grammar in get_grammars():

        match = re.match(

            grammar["pattern"],

            command
        )

        if match:

            return {

                "type": grammar["name"],

                "handler": grammar["handler"],

                "args": list(match.groups())
            }

    # Token-based fallback
    tokens = command.split()
    if "called" in tokens:

        tokens.remove("called")

    verb = tokens[0] if len(tokens) > 0 else ""

    target = tokens[1] if len(tokens) > 1 else ""

    args = tokens[2:] if len(tokens) > 2 else []

    return {

        "verb": verb,

        "target": target,

        "args": args
    }