from modules.agents.action_selector_agent import (
    ActionSelectorAgent
)

agent = (
    ActionSelectorAgent()
)

result = (

    agent.choose_action(
        "search robotics",
        "youtube"
    )
)

print(result)