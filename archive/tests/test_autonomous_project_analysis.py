from core.bootstrap import (
    initialize_runtime
)

from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from core.intent_executor import (
    execute_intent
)

initialize_runtime()

planner = AdaptivePlanner()

plan = planner.recover(
    "analyze project"
)

print("\nPLAN\n")

for task in plan.tasks:

    print(task)

print("\nEXECUTION\n")

for task in plan.tasks:

    execute_intent({

        "intent": task.intent,

        "target": task.target,

        "query": task.query
    })