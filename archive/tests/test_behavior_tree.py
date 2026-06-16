from modules.behavior_tree.sequence_node import SequenceNode

from modules.behavior_tree.action_node import ActionNode


def open_browser():

    print("Opening browser...")


def search_robotics():

    print("Searching robotics papers...")


tree = SequenceNode([

    ActionNode(open_browser),

    ActionNode(search_robotics)
])


result = tree.run()

print("Tree Success:", result)