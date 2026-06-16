import socket

from core.blackboard import set_state


def check_internet():

    try:

        socket.create_connection(

            ("8.8.8.8", 53),

            timeout=2
        )

        set_state(

            "internet_available",

            True
        )

    except OSError:

        set_state(

            "internet_available",

            False
        )