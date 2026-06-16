active_goals = []


def add_goal(

    goal,

    priority=5
):

    active_goals.append({

        "goal": goal,

        "status": "active",

        "attempts": 0,

        "priority": priority
    })

    print(

        f"[Goal Manager] Added goal: {goal}"
    )



def complete_goal(goal):

    for item in active_goals:

        if item["goal"] == goal:

            item["status"] = "completed"

            print(

                f"[Goal Manager] Completed goal: {goal}"
            )



def fail_goal(goal):

    for item in active_goals:

        if item["goal"] == goal:

            item["attempts"] += 1

            print(

                f"[Goal Manager] Failed attempt for: {goal}"
            )



def get_active_goals():

    return [

        goal for goal in active_goals

        if goal["status"] == "active"
    ]