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

from core.world_state import (
    get_state
)

from modules.memory.strategy_memory import (
    get_best_strategies
)

planner = AdaptivePlanner()

goal = (
    "search robotics research papers"
)

print("\nGOAL")
print(goal)

print("\nPLAN")

plan = planner.recover(
    goal
)

for task in plan.tasks:

    print(task)

print("\nEXECUTION")

for task in plan.tasks:

    result = execute_intent(
        task.__dict__
    )

    print(result)

print("\nWORLD STATE")

print(
    get_state()
)

print("\nSTRATEGIES")

print(
    get_best_strategies()
)