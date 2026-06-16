from modules.automation.browser import (
    open_google
)

from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

import time

open_google()

time.sleep(3)

move_mouse(
    1388,
    543
)

left_click()

input(
    "Did Google search box get focus?"
)