from core.capability_registry import (
    has_capability
)


def validate_plan(tasks):

    valid_tasks = []

    for task in tasks:

        intent = task.intent
        target = task.target

        if has_capability(
            intent,
            target
        ):

            valid_tasks.append(
                task
            )

        else:

            print(
                f"[Plan Validator] "
                f"Removing unsupported task: "
                f"{intent} -> {target}"
            )

    return valid_tasks