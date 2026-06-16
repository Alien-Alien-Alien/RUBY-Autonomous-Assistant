import threading

import time

from core.blackboard import (

    set_state,

    get_state
)

from modules.behavior_tree.sequence_node import SequenceNode

from modules.behavior_tree.condition_node import ConditionNode

from modules.behavior_tree.action_node import ActionNode

from modules.behavior_tree.reactive_runner import ReactiveRunner


set_state(

    "internet_available",

    False
)
set_state(

    "search_completed",

    False
)

def check_internet():

    status = get_state(

        "internet_available"
    )

    print(

        f"Internet Status: {status}"
    )

    return status


def search_robotics():

    if get_state(

        "search_completed"
    ):

        print(

            "Search already completed."
        )

        return


    print(

        "Searching robotics papers..."
    )


    set_state(

        "search_completed",

        True
    )

tree = SequenceNode([

    ConditionNode(check_internet),

    ActionNode(search_robotics)
])


runner = ReactiveRunner(

    tree,

    interval=2
)


def simulate_environment_change():

    time.sleep(5)

    print(

        "\n[Environment Changed]\n"
    )

    set_state(

        "internet_available",

        True
    )


threading.Thread(

    target=simulate_environment_change
).start()


try:

    runner.run()

except KeyboardInterrupt:

    runner.stop()

    print(

        "\nReactive system stopped."
    )