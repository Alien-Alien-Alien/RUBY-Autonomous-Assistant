from modules.behavior_tree.selector_node import SelectorNode

from modules.behavior_tree.action_node import ActionNode


def broken_browser():

    print("Firefox failed.")

    raise Exception()


def backup_browser():

    print("Chrome opened.")




tree = SelectorNode([

    ActionNode(broken_browser),

    ActionNode(backup_browser)
])


result = tree.run()

print("Tree Success:", result)