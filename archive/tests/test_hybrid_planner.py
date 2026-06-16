from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

planner = AdaptivePlanner()

print(
    "\nKNOWN GOAL\n"
)

plan = planner.recover(
    "analyze project"
)

for task in plan.tasks:

    print(task)

print(
    "\nUNKNOWN GOAL\n"
)

plan = planner.recover(
    "tell me about this codebase"
)

for task in plan.tasks:

    print(task)