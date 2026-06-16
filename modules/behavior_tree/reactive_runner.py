import time


class ReactiveRunner:


    def __init__(

        self,

        tree,

        interval=1
    ):

        self.tree = tree

        self.interval = interval

        self.running = True


    def run(self):

        while self.running:

            print(

                "\n[Reactive Tick]\n"
            )

            self.tree.run()

            time.sleep(

                self.interval
            )


    def stop(self):

        self.running = False