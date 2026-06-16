from PIL import Image

import pytesseract


def read_text(path):

    image = Image.open(path)

    image = image.resize(
        (
            image.width // 3,
            image.height // 3
        )
    )

    text = pytesseract.image_to_string(
        image,
        config="--oem 1 --psm 6"
    )

    return {

        "success": True,

        "text": text
    }