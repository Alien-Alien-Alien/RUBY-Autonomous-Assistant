from modules.automation.screen_actions import (
    screenshot
)

from modules.vision.ocr import (
    read_screen_boxes
)

path = screenshot()

print("Screenshot:", path)

boxes = read_screen_boxes(path)

for box in boxes:
    print(box["text"])