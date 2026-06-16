from modules.agents.page_understanding_agent import (
    PageUnderstandingAgent
)

from modules.agents.action_selector_agent import (
    ActionSelectorAgent
)

from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)


class GoalAgent:


    def execute_goal(
        self,
        goal
    ):

        page = (

            PageUnderstandingAgent()

            .analyze()
        )

        print(
            "\n[PAGE]"
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
            "\n[ACTION]"
        )

        print(
            action
        )

        if not action["success"]:

            return {

                "success": False,

                "error":
                "No action selected"
            }

        navigator = (
            BrowserNavigationAgent()
        )

        if action["action"] == "youtube_search":

            return (

                navigator.youtube_search(
                    action["query"]
                )
            )

        if action["action"] == "google_search":

            return (

                navigator.google_search(
                    action["query"]
                )
            )

        if action["action"] == "github_search":

            return (

                navigator.github_search(
                    action["query"]
                )
            )

        return {

            "success": False,

            "error":
            "Unknown action"
        }