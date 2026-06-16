from PIL import Image


def image_info(path):

    image = Image.open(
        path
    )

    width, height = (

        image.size
    )

    return {

        "success": True,

        "width": width,

        "height": height,

        "mode": image.mode
    }