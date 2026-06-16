from modules.behavior_tree.base_node import BaseNode


class ActionNode(BaseNode):


    def __init__(self, action):

        self.action = action


    def run(self):

        try:

            self.action()

            return True

        except Exception:

            return False