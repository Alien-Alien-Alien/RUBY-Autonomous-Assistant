from modules.vision.region_locator import (
    crop_region
)

from modules.vision.click_text import (
    click_text
)


def fast_click_text(
    screenshot_path,
    target
):

    crop = crop_region(
        screenshot_path
    )

    if not crop["success"]:

        return crop

    return click_text(

        crop["path"],

        target
    )