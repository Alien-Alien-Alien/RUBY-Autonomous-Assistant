from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

planner = AdaptivePlanner()

plan = planner.recover(
    "recover voice system"
)

print()

for task in plan.tasks:

    print(task)