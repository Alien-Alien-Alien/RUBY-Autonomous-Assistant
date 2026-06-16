from modules.agents.llm_planner import (
    LLMPlanner
)

planner = LLMPlanner()

plan = planner.plan(
    "analyze project"
)

for task in plan.tasks:

    print(task)