from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from core.intent_executor import (
    execute_intent
)

from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.window_capture import (
    capture_window
)

from modules.vision.ocr import (
    read_screen_text
)

from modules.agents.verification_agent import (
    VerificationAgent
)

from modules.vision.window_observer import (
    observe_window
)

class DesktopAgent:

    def __init__(self):

        self.planner = AdaptivePlanner()

        self.verifier = VerificationAgent()

    def observe(self):

        result = capture_window(
            "Firefox",
            "temp/observe.png"
        )

        if not result["success"]:

            return ""

        return read_screen_text(
            result["path"]
        )

    def run(self, goal):

        plan = self.planner.recover(
            goal
        )

        print(
            "\n===== PLAN ====="
        )

        print(
            plan.tasks
        )

        print(
            "================\n"
        )

        results = []

        for task in plan.tasks:

            result = execute_intent(
                {
                    "intent": task.intent,
                    "target": task.target,
                    "query": task.query
                }
            )

            print(
                "\n===== RESULT ====="
            )

            print(
                result
            )

            print(
                "=================="
            )

            results.append(
                result
            )

            screen_text = self.observe()

            print(
                "\n===== OBSERVATION ====="
            )

            print(
                screen_text[:1000]
            )

            print(
                "=======================\n"
            )

        return results

    def verify_text(
        self,
        expected_text
    ):

        texts = self.observe_window(
            "Firefox"
        )

        return self.verifier.text_exists(
            expected_text,
            texts
        )
        
    def run_and_verify(
        self,
        goal,
        expected_text
    ):

        results = self.run(
            goal
        )

        success = self.verify_text(
            expected_text
        )

        return {
            "success": success,
            "results": results
        }



    def observe_window(
        self,
        title
    ):

        return observe_window(
            title
        )