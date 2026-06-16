from modules.plugins.voice_plugin import (
    initialize
)

initialize()

from modules.agents.adaptive_planner import (
    AdaptivePlanner
)
from core.intent_executor import (
    execute_intent
)


planner = AdaptivePlanner()

plan = planner.recover(

    "search robotics research papers"
)

for task in plan.tasks:

    print(task)

    execute_intent(

        task.__dict__
    )