from modules.memory.long_term_memory import load_memory

from modules.agents.planner_agent import PlannerAgent

from modules.agents.execution_agent import ExecutionAgent


load_memory()


planner = PlannerAgent()

executor = ExecutionAgent()


plan = planner.plan(

    "search robotics papers"
)


print(plan)


tasks = plan.tasks

for task in tasks:

    executor.execute(task.__dict__)