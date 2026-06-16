from modules.agents.base_agent import BaseAgent


class MonitorAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "Monitor Agent"
        )


    async def handle_event(self, data):

        self.log(

            f"Observed Event: {data}"
        )