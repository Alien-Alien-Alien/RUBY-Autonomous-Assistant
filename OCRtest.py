import time

from modules.vision.ocr_reader import read_text

start = time.time()

result = read_text("screen.png")

print(
    "OCR:",
    time.time() - start
)