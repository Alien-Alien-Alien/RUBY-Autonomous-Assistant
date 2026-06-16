import asyncio

from core.goal_manager import get_active_goals

from modules.agents.base_agent import BaseAgent


class GoalRetryAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "Goal Retry Agent"
        )


    async def retry_loop(self):

        while True:

            goals = get_active_goals()

            for goal in goals:

                self.log(

                    f"Goal still active: {goal}"
                )

            await asyncio.sleep(10)