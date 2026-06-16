from modules.agents.base_agent import BaseAgent
from modules.memory.recovery_memory import (
    remember_fix,
    get_fix
)

class RecoveryAgent(BaseAgent):


    def __init__(self):

        super().__init__(

            "Recovery Agent"
        )


    def recover(self, task):
        problem = str(task)

        known_fix = get_fix(
            problem
        )

        if known_fix:

            self.log(
                "Using remembered fix."
            )

            return known_fix

                    
        self.log(

            f"Attempting recovery for: {task}"
        )


        if task.get("intent") == "open_app":

            if "target" not in task:

                task["target"] = "firefox"

                self.log(

                    "Applied default browser."
                )

                remember_fix(
                    problem,
                    task
                )

                return task


        return None


    def handle_failure(

        self,

        result
    ):

        if result["success"]:

            return result

        error = ""

        if "error" in result:

            error = result["error"]

        elif "stderr" in result:

            error = result["stderr"]

        self.log(

            f"Failure detected: {error}"
        )

        return {

            "success": False,

            "recovered": False,

            "error": error
        }