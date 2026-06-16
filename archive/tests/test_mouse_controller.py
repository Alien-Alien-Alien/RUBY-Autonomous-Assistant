from modules.automation.mouse_controller import (
    get_mouse_position,
    move_mouse
)

print(

    get_mouse_position()
)

move_mouse(
    500,
    500
)

print(

    get_mouse_position()
)