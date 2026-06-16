from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

from modules.automation.keyboard_controller import (
    type_text,
    press_key
)

import time


def send_message(
    message
):

    move_mouse(
        1300,
        995
    )

    left_click()

    time.sleep(1)

    type_text(
        message
    )

    press_key("enter")
    return {
        "success": True
    }