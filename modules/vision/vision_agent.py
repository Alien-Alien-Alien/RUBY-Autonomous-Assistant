from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.screen_analyzer import (
    analyze_screen
)


class VisionAgent:


    def observe(self):

        screenshot = (

            capture_screen()
        )

        if not screenshot["success"]:

            return screenshot

        analysis = (

            analyze_screen(
                screenshot["path"]
            )
        )

        return {

            "success": True,

            "image":

                screenshot["path"],

            "analysis":

                analysis
        }