import time

from modules.automation.apps import (
    open_firefox
)

open_firefox()

print(
    "Switch to Firefox..."
)

time.sleep(5)

from modules.agents.page_understanding_agent import (
    PageUnderstandingAgent
)

print(

    PageUnderstandingAgent()

    .analyze()
)