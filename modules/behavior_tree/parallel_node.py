import threading

from modules.behavior_tree.base_node import BaseNode


class ParallelNode(BaseNode):


    def __init__(self, children):

        self.children = children


    def run(self):

        results = []


        def execute_node(node):

            results.append(

                node.run()
            )


        threads = []


        for child in self.children:

            thread = threading.Thread(

                target=execute_node,

                args=(child,)
            )

            threads.append(thread)

            thread.start()


        for thread in threads:

            thread.join()


        return all(results)