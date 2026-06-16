from PIL import Image, ImageDraw

from modules.vision.screen_capture import capture_screen
from modules.vision.text_locator import find_text

screen = capture_screen()

result = find_text(
    screen["path"],
    "Ask"
)

img = Image.open(
    screen["path"]
)

draw = ImageDraw.Draw(img)

draw.rectangle(
    [
        result["x"],
        result["y"],
        result["x"] + result["width"],
        result["y"] + result["height"]
    ],
    outline="red",
    width=3
)

img.save(
    "temp/target_debug.png"
)

print(result)
print("Saved: temp/target_debug.png")