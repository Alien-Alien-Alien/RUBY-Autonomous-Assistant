from modules.automation.apps import (
    open_firefox
)

from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)

import time


print(
    "\nOpening Firefox..."
)

open_firefox()

time.sleep(3)

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