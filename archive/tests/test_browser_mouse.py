from modules.automation.mouse_controller import (
    move_mouse
)

print(
    "Moving mouse in 3 seconds..."
)

import time

time.sleep(3)

move_mouse(
    700,
    300
)

print(
    "Done"
)