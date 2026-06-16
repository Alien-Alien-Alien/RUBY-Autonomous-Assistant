from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)

agent = (
    BrowserNavigationAgent()
)

input(
    "Open Firefox first and press Enter..."
)

result = (

    agent.youtube_search(
        "robotics"
    )
)

print(
    result
)