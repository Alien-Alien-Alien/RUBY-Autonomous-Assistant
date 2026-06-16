import os
import subprocess


def create_file(filename):

    open(
        filename,
        "a"
    ).close()


def create_folder(foldername):

    os.makedirs(
        foldername,
        exist_ok=True
    )


def open_file(filename):

    subprocess.Popen(
        ["xdg-open", filename]
    )


def read_file(filename):

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    except Exception as e:

        return str(e)