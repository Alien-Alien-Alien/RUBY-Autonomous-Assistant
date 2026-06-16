import threading

import time

from core.blackboard import (

    get_state,

    set_state
)

from modules.perception.perception_manager import (

    PerceptionManager
)

from modules.behavior_tree.sequence_node import (

    SequenceNode
)

from modules.behavior_tree.condition_node import (

    ConditionNode
)

from modules.behavior_tree.action_node import (

    ActionNode
)

from modules.behavior_tree.reactive_runner import (

    ReactiveRunner
)


# INITIAL BLACKBOARD STATE

set_state(

    "search_completed",

    False
)


# CONDITION

def internet_available():

    status = get_state(

        "internet_available"
    )

    print(

        f"Internet Status: {status}"
    )

    return status


# ACTION

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


# BUILD TREE

tree = SequenceNode([

    ConditionNode(

        internet_available
    ),

    ActionNode(

        search_robotics
    )
])


# PERCEPTION MANAGER

perception = PerceptionManager(

    interval=3
)


# REACTIVE RUNNER

runner = ReactiveRunner(

    tree,

    interval=2
)


# START PERCEPTION THREAD

perception_thread = threading.Thread(

    target=perception.run
)

perception_thread.start()


# START REACTIVE SYSTEM

try:

    runner.run()

except KeyboardInterrupt:

    perception.stop()

    runner.stop()

    print(

        "\nAutonomous runtime stopped."
    )