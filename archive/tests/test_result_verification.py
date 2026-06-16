from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)

from modules.agents.result_verification_agent import (
    ResultVerificationAgent
)


navigator = (
    BrowserNavigationAgent()
)

navigator.youtube_search(
    "robotics"
)

verifier = (
    ResultVerificationAgent()
)

result = (

    verifier.verify_search(
        "robotics"
    )
)

print(result)
