from PIL import Image

def crop_region(path):

    image = Image.open(path)

    cropped = image.crop(
        (0, 400, 800, 900)
    )
    cropped.save(
        "temp/crop.png"
    )

    return {
        "success": True,
        "path": "temp/crop.png"
    }