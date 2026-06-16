import time

from modules.vision.ocr_reader import (
    read_text
)

start = time.time()

result = read_text(
    "temp/crop.png"
)

print(result)

print(
    "OCR Time:",
    round(
        time.time() - start,
        3
    ),
    "seconds"
)