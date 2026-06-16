from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.fast_click_text import (
    fast_click_text
)

screen = capture_screen()

print(

    fast_click_text(

        screen["path"],

        "ChatGPT"
    )
)