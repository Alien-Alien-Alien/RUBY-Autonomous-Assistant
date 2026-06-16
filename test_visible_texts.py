from modules.vision.window_capture import (
    capture_window
)

from modules.vision.ocr import (
    get_visible_texts
)

capture_window(
    "Firefox",
    "temp/test.png"
)

texts = get_visible_texts(
    "temp/test.png"
)

for text in texts:

    print(text)