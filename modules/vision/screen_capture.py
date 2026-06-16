from mss import mss


def capture_screen(
    output="screen.png"
):

    try:

        with mss() as sct:

            sct.shot(
                output=output
            )

        return {
            "success": True,
            "path": output
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }