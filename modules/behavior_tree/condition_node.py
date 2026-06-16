from modules.behavior_tree.base_node import BaseNode


class ConditionNode(BaseNode):


    def __init__(self, condition):

        self.condition = condition


    def run(self):

        try:

            return self.condition()

        except Exception:

            return False