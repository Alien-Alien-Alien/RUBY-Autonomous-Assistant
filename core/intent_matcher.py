import difflib


KNOWN_COMMANDS = [

    "open firefox",

    "open youtube",

    "open github",

    "open sublime",

    "list files"
]


def match_intent(text):

    matches = difflib.get_close_matches(

        text,

        KNOWN_COMMANDS,

        n=1,

        cutoff=0.85
    )

    if matches:

        return matches[0]

    return text