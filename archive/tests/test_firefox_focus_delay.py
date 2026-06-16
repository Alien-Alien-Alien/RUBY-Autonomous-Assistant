from modules.automation.apps import (
    open_firefox
)

import time

print(
    "Opening Firefox..."
)

open_firefox()

time.sleep(5)

print(
    "Done."
)