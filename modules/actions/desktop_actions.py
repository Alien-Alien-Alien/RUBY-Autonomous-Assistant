import subprocess


def open_firefox():

    subprocess.Popen(
        ["firefox"]
    )


def open_terminal():

    subprocess.Popen(
        ["gnome-terminal"]
    )


def open_github():

    subprocess.Popen(
        [
            "firefox",
            "https://github.com"
        ]
    )


def open_chatgpt():

    subprocess.Popen(
        [
            "firefox",
            "https://chatgpt.com"
        ]
    )