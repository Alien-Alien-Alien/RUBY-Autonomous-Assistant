from modules.agents.page_understanding_agent import (
    PageUnderstandingAgent
)

from modules.agents.action_selector_agent import (
    ActionSelectorAgent
)

from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)

goal = "search robotics"

page = (

    PageUnderstandingAgent()

    .analyze()
)

print(
    "\nPAGE\n"
)

print(
    page
)

action = (

    ActionSelectorAgent()

    .choose_action(
        goal,
        page["page_type"]
    )
)

print(
    "\nACTION\n"
)

print(
    action
)

if action["success"]:

    navigator = (
        BrowserNavigationAgent()
    )

    if action["action"] == "youtube_search":

        result = (

            navigator.youtube_search(
                action["query"]
            )
        )

    elif action["action"] == "google_search":

        result = (

            navigator.google_search(
                action["query"]
            )
        )

    elif action["action"] == "github_search":

        result = (

            navigator.github_search(
                action["query"]
            )
        )

    else:

        result = {

            "success": False
        }

    print(
        "\nRESULT\n"
    )

    print(
        result
    )

else:

    print(
        "\nNO ACTION SELECTED\n"
    )