import pyautogui


def type_text(text):

    pyautogui.write(
        text
    )

    return {
        "success": True
    }


def press_key(key):

    pyautogui.press(
        key
    )

    return {
        "success": True
    }


def hotkey(*keys):

    pyautogui.hotkey(
        *keys
    )

    return {
        "success": True
    }