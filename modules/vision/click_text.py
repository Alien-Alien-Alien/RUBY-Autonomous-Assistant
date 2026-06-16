from modules.vision.text_locator import (
    find_text
)

from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)


def click_text(
    image_path,
    target
):

    result = find_text(
        image_path,
        target
    )

    if not result["success"]:

        return result

    center_x = result["x"] + result["width"] // 2

    center_y = (
        result["y"]
        + result["height"]
        + 50
    )

    move_mouse(
        center_x,
        center_y
    )

    left_click()

    return {

        "success": True,

        "clicked": target,

        "x": center_x,

        "y": center_y
    }