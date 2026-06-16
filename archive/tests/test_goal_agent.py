from modules.agents.goal_agent import (
    GoalAgent
)

agent = (
    GoalAgent()
)

result = (

    agent.execute_goal(
        "search robotics"
    )
)

print(
    "\n[RESULT]"
)

print(
    result
)