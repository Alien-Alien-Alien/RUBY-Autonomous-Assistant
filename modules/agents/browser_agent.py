from modules.automation.browser import (
    open_google
)

from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

from modules.automation.keyboard_controller import (
    type_text,
    press_key
)

import time


class BrowserAgent:


    def search(
        self,
        query
    ):

        open_google()

        time.sleep(3)

        move_mouse(
            1388,
            543
        )

        left_click()

        time.sleep(1)

        type_text(
            query
        )

        press_key("enter")

        return {

            "success": True,

            "query": query
        }