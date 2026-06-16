import subprocess

import time


def open_firefox():

    subprocess.Popen(
        ["firefox"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(2)

    try:

        subprocess.run(
            [
                "wmctrl",
                "-a",
                "Firefox"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception:

        pass


def open_sublime():

    subprocess.Popen(
        ["subl"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(2)

    try:

        subprocess.run(
            [
                "wmctrl",
                "-a",
                "Sublime"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception:

        pass