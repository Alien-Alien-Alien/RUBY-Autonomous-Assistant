from modules.behavior_tree.base_node import BaseNode


class RetryDecorator(BaseNode):


    def __init__(self, child, retries=3):

        self.child = child

        self.retries = retries


    def run(self):

        for attempt in range(

            self.retries
        ):

            success = self.child.run()

            print(

                f"Retry Attempt: {attempt + 1}"
            )

            if success:

                return True


        return False