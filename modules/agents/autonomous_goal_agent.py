from modules.agents.goal_agent import (
    GoalAgent
)

from modules.agents.result_verification_agent import (
    ResultVerificationAgent
)

from modules.agents.startup_agent import (
    StartupAgent
)

from modules.agents.page_understanding_agent import (
    PageUnderstandingAgent
)


class AutonomousGoalAgent:


    def execute(
        self,
        goal
    ):

        page = (

            PageUnderstandingAgent()

            .analyze()
        )

        if (
            page["page_type"]
            == "unknown"
        ):

            print(
                "\n[STARTUP]"
            )

            StartupAgent().prepare_browser()

        print(
            "\n[GOAL]"
        )

        result = (

            GoalAgent()

            .execute_goal(
                goal
            )
        )

        if not result.get(
            "success"
        ):

            return result

        query = (

            goal
            .replace(
                "search",
                ""
            )
            .strip()
        )

        print(
            "\n[VERIFY]"
        )

        verification = (

            ResultVerificationAgent()

            .verify_search(
                query
            )
        )

        return verification