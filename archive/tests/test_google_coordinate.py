from modules.automation.mouse_controller import (
    get_mouse_position
)

import time

print(
    "Move mouse to Google search box..."
)

time.sleep(5)

print(
    get_mouse_position()
)