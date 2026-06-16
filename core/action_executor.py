from modules.actions.project_actions import (
    create_python_project
)

from modules.actions.desktop_actions import (
    open_github
)


class ActionExecutor:

    def execute(

        self,

        actions

    ):

        results = []

        for action,data in actions:

            if action == "create_project":

                create_python_project(
                    data
                )

                results.append(
                    f"Created {data}"
                )

            elif action == "open_github":

                open_github()

                results.append(
                    "GitHub opened"
                )

        return results