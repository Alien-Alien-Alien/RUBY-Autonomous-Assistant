from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

move_mouse(
    500,
    500
)

input(
    "Press Enter to click..."
)

print(
    left_click()
)
