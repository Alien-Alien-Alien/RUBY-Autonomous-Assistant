from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.click_text import (
    click_text
)


class UIAgent:

    def click_label(
        self,
        label
    ):

        screenshot = capture_screen()

        if not screenshot["success"]:

            return screenshot

        return click_text(

            screenshot["path"],

            label
        )