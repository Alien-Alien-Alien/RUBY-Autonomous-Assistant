import json

from modules.llm.ollama_client import (
    ask_llm
)

from core.schemas.task_schema import (
    Task
)

from core.schemas.plan_schema import (
    Plan
)

import time


class LLMPlanner:


    def plan(
        self,
        goal
    ):

        llm_start = time.time()

        start = time.time()

        response = ask_llm(
            goal
        )

        print(
            "ONLY LLM:",
            time.time() - start
        )

        print(
            "[LLM TIME]",
            time.time() - llm_start
        )
        print("\n===== RAW PLAN =====")
        print(response)
        print("====================\n")

        data = json.loads(
            response
        )
        if "intent" in data:

            data = {

                "goal": goal,

                "tasks": [data]
            }

        tasks = []

        for item in data.get(
            "tasks",
            []
        ):

            tasks.append(

                Task(

                    intent=item.get(
                        "intent",
                        ""
                    ),

                    target=item.get(
                        "target",
                        ""
                    ),

                    query=item.get(
                        "query",
                        ""
                    )
                )
            )

        return Plan(

            goal=data.get(
                "goal",
                goal
            ),

            tasks=tasks
        )