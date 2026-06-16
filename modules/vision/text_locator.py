from PIL import Image
import pytesseract
import time


def find_text(path, target):
    start = time.time()

    image = Image.open(path)

    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT
    )

    target = target.lower()

    for i in range(
        len(data["text"])
    ):

        text = data["text"][i]

        if target in text.lower():
            print(
                "OCR Time:",
                time.time() - start
            )

            return {

                "success": True,

                "text": text,

                "x": data["left"][i],

                "y": data["top"][i],

                "width": data["width"][i],

                "height": data["height"][i]
            }

    
    return {

        "success": False
    }