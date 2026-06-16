from modules.memory.long_term_memory import (

    load_memory
)

from core.goal_manager import (

    add_goal
)

from core.goal_dispatcher import (

    GoalDispatcher
)


load_memory()


add_goal(

    "search robotics papers",

    priority=3
)

add_goal(

    "check battery status",

    priority=10
)


dispatcher = GoalDispatcher()

dispatcher.dispatch()