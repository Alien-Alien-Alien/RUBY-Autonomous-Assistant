from modules.agents.planner_agent import PlannerAgent

from modules.behavior_tree.tree_builder import TreeBuilder

from modules.memory.long_term_memory import load_memory


load_memory()


planner = PlannerAgent()

builder = TreeBuilder()


plan = planner.plan(

    "search robotics papers"
)


tree = builder.build(

    plan.tasks
)


result = tree.run()

print(

    "Behavior Tree Result:",

    result
)