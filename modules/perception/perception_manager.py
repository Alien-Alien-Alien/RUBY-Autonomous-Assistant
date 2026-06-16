import time

from modules.perception.internet_sensor import (

    check_internet
)


class PerceptionManager:


    def __init__(

        self,

        interval=5
    ):

        self.interval = interval

        self.running = True


    def run(self):

        while self.running:

            check_internet()

            time.sleep(

                self.interval
            )


    def stop(self):

        self.running = False