import time

from modules.vision.screen_capture import (
    capture_screen
)

start = time.time()

capture_screen()

print(
    "Capture Time:",
    round(
        time.time() - start,
        3
    ),
    "seconds"
)