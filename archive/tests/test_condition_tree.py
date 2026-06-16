from core.blackboard import (

    set_state,

    get_state
)

from modules.behavior_tree.sequence_node import SequenceNode

from modules.behavior_tree.condition_node import ConditionNode

from modules.behavior_tree.action_node import ActionNode


set_state(

    "internet_available",

    True
)


def check_internet():

    print("Checking internet...")

    return get_state(

        "internet_available"
    )


def search_robotics():

    print("Searching robotics papers...")


tree = SequenceNode([

    ConditionNode(check_internet),

    ActionNode(search_robotics)
])


result = tree.run()

print("Tree Success:", result)