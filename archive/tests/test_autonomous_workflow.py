from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from core.intent_executor import (
    execute_intent
)

from core.bootstrap import (
    initialize_runtime
)

initialize_runtime()

planner = AdaptivePlanner()

plan = planner.recover(
    "inspect project"
)

print("\nPLAN\n")

for task in plan.tasks:

    print(task)

print("\nEXECUTION\n")

for task in plan.tasks:

    print(
        "DEBUG:",
        task.intent,
        task.target,
        task.query
    )

    execute_intent({

        "intent": task.intent,

        "target": task.target,

        "query": task.query
    })