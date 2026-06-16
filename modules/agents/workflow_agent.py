from modules.memory.workflow_memory import (
    get_workflow
)

from core.intent_executor import (
    execute_intent
)

from modules.agents.desktop_agent import (
    DesktopAgent
)

from modules.agents.verification_agent import (
    VerificationAgent
)


class WorkflowAgent:

    def __init__(self):

        self.desktop = DesktopAgent()

        self.verifier = VerificationAgent()

    def run_workflow(
        self,
        workflow_name
    ):

        workflow = get_workflow(
            workflow_name
        )

        if not workflow:

            return {

                "success": False,

                "error":
                    "Workflow not found"
            }

        print(
            f"\n[WorkflowAgent] Running: "
            f"{workflow_name}\n"
        )

        results = []

        for task in workflow:

            print(task)

            result = execute_intent(
                task
            )

            results.append(
                result
            )

            if not result.get(
                "success",
                False
            ):

                return {

                    "success": False,

                    "failed_task": task,

                    "result": result,

                    "results": results
                }

        return {

            "success": True,

            "results": results
        }

    def observe(self):

        return self.desktop.observe()

    def verify_text(
        self,
        expected_text
    ):

        screen_text = self.observe()

        return self.verifier.text_exists(
            expected_text,
            screen_text
        )
    def verify_after_action(
        self,
        expected_text
    ):

        screen_text = self.observe()

        return self.verifier.verify(
            expected_text,
            screen_text
        )
    def retry_until_visible(
        self,
        task,
        expected_text,
        max_retries=3
    ):

        for attempt in range(
            max_retries
        ):

            result = execute_intent(
                task
            )

            if not result["success"]:
                continue

            verification = (
                self.verify_after_action(
                    expected_text
                )
            )

            if verification["success"]:

                return {
                    "success": True,
                    "attempts": attempt + 1
                }

        return {
            "success": False
        }