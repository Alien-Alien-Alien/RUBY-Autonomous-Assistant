import threading

import time

from modules.perception.perception_manager import (

    PerceptionManager
)

from core.blackboard import get_state


manager = PerceptionManager(

    interval=3
)


thread = threading.Thread(

    target=manager.run
)

thread.start()


try:

    while True:

        print(

            "Internet State:",

            get_state(

                "internet_available"
            )
        )

        time.sleep(3)

except KeyboardInterrupt:

    manager.stop()

    print(

        "\nPerception stopped."
    )