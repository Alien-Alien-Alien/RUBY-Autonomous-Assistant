from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

planner = AdaptivePlanner()

plan = planner.recover(
    "analyze project"
)

for task in plan.tasks:

    print(task)