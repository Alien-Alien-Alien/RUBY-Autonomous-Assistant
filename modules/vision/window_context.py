import subprocess


def get_active_window():

    try:

        result = subprocess.check_output(
            [
                "xdotool",
                "getactivewindow",
                "getwindowname"
            ],
            text=True
        )

        return {
            "success": True,
            "title": result.strip()
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }