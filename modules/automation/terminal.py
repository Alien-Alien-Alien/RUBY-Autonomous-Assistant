import subprocess

SAFE_TERMINAL_COMMANDS = {

    "pwd": ["pwd"],

    "ls": ["ls"],

    "whoami": ["whoami"]
}


def run_terminal_command(command):

    if command not in SAFE_TERMINAL_COMMANDS:

        return {

            "success": False,

            "output": "Unsafe or unknown terminal command."
        }

    result = subprocess.run(

        SAFE_TERMINAL_COMMANDS[command],

        capture_output=True,

        text=True
    )

    return {

        "success": True,

        "output": result.stdout
    }