import time

from modules.behavior_tree.parallel_node import ParallelNode

from modules.behavior_tree.action_node import ActionNode


def monitor_sensors():

    print(

        "Monitoring sensors..."
    )

    time.sleep(2)

    print(

        "Sensors complete."
    )


def listen_voice():

    print(

        "Listening for voice..."
    )

    time.sleep(2)

    print(

        "Voice complete."
    )


tree = ParallelNode([

    ActionNode(

        monitor_sensors
    ),

    ActionNode(

        listen_voice
    )
])


result = tree.run()

print(

    "Tree Success:",

    result
)