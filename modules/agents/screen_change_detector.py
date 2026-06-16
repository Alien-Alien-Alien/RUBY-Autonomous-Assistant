import hashlib


class ScreenChangeDetector:

    def __init__(self):

        self.last_hash = None

    def has_changed(self, image_path):


        with open(
            image_path,
            "rb"
        ) as f:

            current_hash = hashlib.md5(
                f.read()
            ).hexdigest()

        print(
            "HASH:",
            current_hash
        )

        if self.last_hash is None:

            self.last_hash = current_hash

            return True

        if current_hash != self.last_hash:

            self.last_hash = current_hash

            return True

        return False