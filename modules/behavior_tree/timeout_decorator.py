import threading

from modules.behavior_tree.base_node import BaseNode


class TimeoutDecorator(BaseNode):


    def __init__(

        self,

        child,

        timeout=5
    ):

        self.child = child

        self.timeout = timeout


    def run(self):

        result = [False]


        def target():

            result[0] = self.child.run()


        thread = threading.Thread(

            target=target
        )

        thread.start()

        thread.join(

            timeout=self.timeout
        )


        if thread.is_alive():

            print(

                "Behavior timed out."
            )

            return False


        return result[0]