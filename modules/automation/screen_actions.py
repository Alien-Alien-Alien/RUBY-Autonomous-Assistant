from modules.automation.mouse_controller import (
    move_mouse,
    left_click,
    right_click,
    double_click
)

from modules.automation.keyboard_controller import (
    type_text
)

from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.ocr import (
    read_screen_boxes
)
import time

def find_all_text(text, image_path):

    boxes = read_screen_boxes(
        image_path
    )

    text = text.lower()

    matches = []

    for box in boxes:

        if text in box["text"].lower():

            matches.append(
                {
                    "text": box["text"],
                    "x": box["x"] + box["w"] // 2,
                    "y": box["y"] + box["h"] // 2
                }
            )

    return matches


def find_text(text, image_path):

    matches = find_all_text(
        text,
        image_path
    )

    if not matches:

        return {
            "success": False
        }
    print(matches)
    best = max(
        matches,
        key=lambda m: m["y"]
    )

    return {
        "success": True,
        **best
    }



def click_text(text):

    image_path = screenshot()

    result = find_text(
        text,
        image_path
    )

    if not result["success"]:

        return result

    move_mouse(
        result["x"],
        result["y"]
    )

    left_click()

    return {
        "success": True,
        "x": result["x"],
        "y": result["y"]
    }

def screenshot():

    result = capture_screen(
        "temp/screenshot.png"
    )

    if not result["success"]:
        return None

    return result["path"]


def double_click_text(text):

    image_path = screenshot()

    result = find_text(
        text,
        image_path
    )

    if not result["success"]:
        return result

    move_mouse(
        result["x"],
        result["y"]
    )

    double_click()

    return {
        "success": True
    }

def right_click_text(text):

    image_path = screenshot()

    result = find_text(
        text,
        image_path
    )

    if not result["success"]:
        return result

    move_mouse(
        result["x"],
        result["y"]
    )

    right_click()

    return {
        "success": True
    }


def type_at_text(
    text_to_find,
    text_to_type
):

    result = click_text(
        text_to_find
    )

    if not result["success"]:
        return result

    time.sleep(0.4)

    type_text(
        text_to_type
    )

    return {
        "success": True
    }