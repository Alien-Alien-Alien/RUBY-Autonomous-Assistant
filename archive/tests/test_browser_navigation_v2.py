from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)

agent = (
    BrowserNavigationAgent()
)

result = (

    agent.youtube_search(
        "robotics"
    )
)

print(
    result
)