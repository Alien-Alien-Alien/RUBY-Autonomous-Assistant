import time

from PIL import Image
import pytesseract

start = time.time()

image = Image.open("screen.png")

print(
    "LOAD:",
    time.time() - start
)

start = time.time()

image = image.convert("L")

print(
    "GRAY:",
    time.time() - start
)

start = time.time()

image = image.resize(
    (
        image.width // 2,
        image.height // 2
    )
)

print(
    "RESIZE:",
    time.time() - start
)

start = time.time()

text = pytesseract.image_to_string(
    image
)

print(
    "OCR:",
    time.time() - start
)