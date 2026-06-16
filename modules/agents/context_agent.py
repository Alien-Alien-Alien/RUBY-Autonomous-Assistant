from modules.agents.situation_agent import (
    SituationAgent
)

from modules.agents.screen_awareness_agent import (
    ScreenAwarenessAgent
)


class ContextAgent:


    def build_context(self):

        situation = (

            SituationAgent()

            .analyze()
        )

        screen = (

            ScreenAwarenessAgent()

            .observe()
        )

        return {

            "success": True,

            "situation":
            situation,

            "screen":
            screen
        }