import pyautogui


def get_mouse_position():

    x, y = pyautogui.position()

    return {
        "success": True,
        "x": x,
        "y": y
    }


def move_mouse(x, y):

    pyautogui.moveTo(
        x,
        y,
        duration=0.1
    )

    return {
        "success": True
    }


def left_click(x=None, y=None):

    pyautogui.click(
        x=x,
        y=y
    )

    return {
        "success": True
    }


def right_click(x=None, y=None):

    pyautogui.rightClick(
        x=x,
        y=y
    )

    return {
        "success": True
    }


def double_click(x=None, y=None):

    pyautogui.doubleClick(
        x=x,
        y=y
    )

    return {
        "success": True
    }


def scroll(amount):

    pyautogui.scroll(amount)

    return {
        "success": True
    }