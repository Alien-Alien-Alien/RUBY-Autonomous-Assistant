from modules.agents.planner_agent import (

    PlannerAgent
)

from modules.behavior_tree.tree_builder import (

    TreeBuilder
)

from core.runtime_policy import (
    get_policy
)

from core.goal_manager import (

    get_active_goals
)


class GoalDispatcher:


    def __init__(self):

        self.planner = PlannerAgent()

        self.builder = TreeBuilder()


    def dispatch(self):

        goals = get_active_goals()
        allow_low_priority = get_policy(
            "allow_low_priority_goals"
        )
        goals.sort(

            key=lambda g:

            g["priority"],

            reverse=True
        )

        for goal in goals:
            if (
                not allow_low_priority
                and goal["priority"] < 5
            ):

                print(
                    f"[Dispatcher] Skipping "
                    f"low-priority goal: "
                    f"{goal['goal']}"
                )

                continue

            goal_text = goal["goal"]


            print(

                f"\n[Dispatching Goal] {goal_text}"
            )


            plan = self.planner.plan(

                goal_text
            )

            tree = self.builder.build(

                plan.tasks
            )


            tree.run()