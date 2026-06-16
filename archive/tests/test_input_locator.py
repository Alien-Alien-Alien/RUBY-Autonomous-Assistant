from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.text_locator import (
    find_text
)

screen = capture_screen()

print(
    find_text(
        screen["path"],
        "Ask"
    )
)