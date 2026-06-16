from core.goal_manager import (
    add_goal
)

from core.runtime_policy import (
    set_policy
)

from core.goal_dispatcher import (
    GoalDispatcher
)

add_goal(
    "search robotics papers",
    priority=2
)

add_goal(
    "recover voice system",
    priority=10
)

set_policy(
    "allow_low_priority_goals",
    False
)

dispatcher = GoalDispatcher()

dispatcher.dispatch()