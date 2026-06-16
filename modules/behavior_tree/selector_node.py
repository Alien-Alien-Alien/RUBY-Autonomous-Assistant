from modules.behavior_tree.base_node import BaseNode


class SelectorNode(BaseNode):


    def __init__(self, children):

        self.children = children


    def run(self):

        for child in self.children:

            success = child.run()

            if success:

                return True

        return False