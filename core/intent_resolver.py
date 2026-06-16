from modules.memory.preference_engine import (

    infer_preferences
)


def resolve_intent(task):

    preferences = infer_preferences()

    print(preferences)


    intent = task.get("intent")

    target = task.get("target")


    if intent == "open_app":

        if target == "browser":

            preferred = preferences.get(

                "most_used_command"
            )

            print(preferred)


            if preferred == "open firefox":

                task["target"] = "firefox"

            elif preferred == "open chrome":

                task["target"] = "chrome"


    return task