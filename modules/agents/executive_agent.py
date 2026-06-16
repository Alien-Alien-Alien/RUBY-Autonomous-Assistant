class ExecutiveAgent:

    def execute_goal(

        self,

        goal

    ):

        goal = goal.lower()

        if "create python project" in goal:

            name = (
                goal.replace(
                    "create python project",
                    ""
                )
                .strip()
            )

            return [
                (
                    "create_project",
                    name
                )
            ]

        if "open github" in goal:

            return [
                (
                    "open_github",
                    None
                )
            ]

        return []