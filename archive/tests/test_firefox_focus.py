from modules.automation.apps import (
    open_firefox
)

import pyautogui

import time


print(
    "Opening Firefox..."
)

open_firefox()

time.sleep(3)

pyautogui.write(
    "HELLO_FIREFOX",
    interval=0.05
)