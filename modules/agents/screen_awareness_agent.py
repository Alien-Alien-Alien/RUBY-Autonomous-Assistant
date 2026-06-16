from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.screen_analyzer import (
    analyze_screen
)


class ScreenAwarenessAgent:

    def observe(self):

        capture_result = capture_screen()

        if not capture_result["success"]:

            return {
                "success": False,
                "error": "Screen capture failed"
            }

        image_path = capture_result["path"]

        analysis = analyze_screen(
            image_path
        )

        return analysis

    def contains(
        self,
        target_text
    ):

        result = self.observe()

        if not result["success"]:

            return False

        raw_text = result.get(
            "raw_text",
            ""
        )

        return (
            target_text.lower()
            in
            raw_text.lower()
        )

    def get_context(self):

        result = self.observe()

        if not result["success"]:

            return {}

        return result.get(
            "context",
            {}
        )

    def get_summary(self):

        result = self.observe()

        if not result["success"]:

            return "Screen analysis failed"

        return result.get(
            "summary",
            ""
        )