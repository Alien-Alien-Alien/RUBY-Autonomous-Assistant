from modules.behavior_tree.sequence_node import SequenceNode

from modules.behavior_tree.action_node import ActionNode

from modules.agents.execution_agent import ExecutionAgent


class TreeBuilder:


    def __init__(self):

        self.executor = ExecutionAgent()


    def build(self, tasks):

        nodes = []


        for task in tasks:

            node = ActionNode(

                lambda t=task:

                self.executor.execute(

                    t.__dict__
                )
            )

            nodes.append(node)


        return SequenceNode(nodes)