from modules.agents.desktop_agent import (
    DesktopAgent
)


class AutonomousAgent:

    def __init__(self):

        self.desktop = DesktopAgent()

    def run_goal(
        self,
        goal,
        expected_text,
        max_attempts=3
    ):

        for attempt in range(
            max_attempts
        ):

            print(
                f"\n===== ATTEMPT {attempt + 1} ====="
            )

            result = (
                self.desktop.run_and_verify(
                    goal,
                    expected_text
                )
            )

            print(
                "VERIFY RESULT:",
                result
            )

            if result["success"]:

                return {
                    "success": True,
                    "attempts": attempt + 1
                }

        return {
            "success": False,
            "attempts": max_attempts
        }