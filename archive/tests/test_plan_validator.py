from modules.agents.planner_agent import (
    PlannerAgent
)

planner = PlannerAgent()

plan = planner.plan(
    "recover voice system"
)

print()

print(
    "Validated Tasks:"
)

for task in plan.tasks:

    print(task)