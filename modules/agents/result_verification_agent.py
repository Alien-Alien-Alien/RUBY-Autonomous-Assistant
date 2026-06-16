import time

from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.ocr_reader import (
    read_text
)


class ResultVerificationAgent:


    def verify_search(
        self,
        query
    ):

        time.sleep(3)

        screenshot = (
            capture_screen()
        )

        text = (
            read_text(
                screenshot["path"]
            )
        )

        screen_text = (
            text["text"]
            .lower()
        )

        success = (
            query.lower()
            in screen_text
        )

        return {

            "success": success,

            "query": query,

            "screen_text":
            screen_text[:1000]
        }