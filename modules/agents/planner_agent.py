import json

from modules.llm.ollama_client import ask_llm

from core.schemas.task_schema import Task

from core.schemas.plan_schema import Plan

from core.plan_validator import (
    validate_plan
)

from core.capability_registry import (
    show_capabilities
)

from modules.agents.adaptive_planner import (
    AdaptivePlanner
)


class PlannerAgent:


    def plan(self, user_input):

        capabilities = show_capabilities()

        prompt = f"""
You are an autonomous planning agent.

AVAILABLE CAPABILITIES:
{capabilities}

RULES:
1. ONLY use intents that exist in AVAILABLE CAPABILITIES.
2. ONLY use targets that exist in AVAILABLE CAPABILITIES.
3. NEVER invent new intents.
4. NEVER invent new targets.
5. Return ONLY valid JSON.
6. If the goal cannot be completed using available capabilities, return:

{{
    "goal": "{user_input}",
    "tasks": []
}}

JSON FORMAT:

{{
    "goal": "{user_input}",
    "tasks": [
        {{
            "intent": "...",
            "target": "...",
            "query": "..."
        }}
    ]
}}

USER GOAL:
{user_input}
"""

        response = ask_llm(prompt)
        print("\n===== RAW LLM RESPONSE =====")
        print(response)
        print("===========================\n")

        try:

            data = json.loads(response)

        except json.JSONDecodeError:

            print(
                "[Planner] Invalid JSON returned."
            )

            return Plan(
                goal=user_input,
                tasks=[]
            )

        tasks = []

        for task_data in data.get(
            "tasks",
            []
        ):

            task = Task(

                intent=task_data.get(
                    "intent",
                    ""
                ),

                target=task_data.get(
                    "target",
                    ""
                ),

                query=task_data.get(
                    "query",
                    ""
                )
            )

            tasks.append(task)

        tasks = validate_plan(
            tasks
        )
        if not tasks:

            print(
                "[Planner] Empty plan."
            )

            adaptive = AdaptivePlanner()

            return adaptive.recover(
                data["goal"]
            )
        return Plan(

            goal=data.get(
                "goal",
                user_input
            ),

            tasks=tasks
        )