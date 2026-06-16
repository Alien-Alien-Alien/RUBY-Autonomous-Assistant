import time

from modules.behavior_tree.action_node import ActionNode

from modules.behavior_tree.timeout_decorator import TimeoutDecorator


def slow_action():

    print(

        "Starting slow action..."
    )

    time.sleep(10)

    print(

        "Finished action."
    )


tree = TimeoutDecorator(

    ActionNode(slow_action),

    timeout=3
)


result = tree.run()

print(

    "Tree Success:",

    result
)