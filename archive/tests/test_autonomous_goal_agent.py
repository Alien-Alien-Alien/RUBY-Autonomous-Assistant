from modules.agents.autonomous_goal_agent import (
    AutonomousGoalAgent
)

agent = (
    AutonomousGoalAgent()
)

result = (

    agent.execute(
        "search robotics"
    )
)

print(
    "\n[FINAL RESULT]"
)

print(
    result
)