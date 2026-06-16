import json
import os

EXPERIENCE_FILE = (
    "data/experience_memory.json"
)


def load_experiences():

    if not os.path.exists(
        EXPERIENCE_FILE
    ):

        return {}

    with open(
        EXPERIENCE_FILE,
        "r"
    ) as file:

        return json.load(file)


def save_experiences(
    experiences
):

    with open(
        EXPERIENCE_FILE,
        "w"
    ) as file:

        json.dump(
            experiences,
            file,
            indent=4
        )


def record_success(
    goal,
    strategy
):

    experiences = load_experiences()

    if goal not in experiences:

        experiences[goal] = []

    for entry in experiences[goal]:

        if entry["strategy"] == strategy:

            entry["successes"] += 1

            save_experiences(
                experiences
            )

            return

    experiences[goal].append({

        "strategy": strategy,

        "successes": 1,

        "failures": 0
    })

    save_experiences(
        experiences
    )


def record_failure(
    goal,
    strategy
):

    experiences = load_experiences()

    if goal not in experiences:

        experiences[goal] = []

    for entry in experiences[goal]:

        if entry["strategy"] == strategy:

            entry["failures"] += 1

            save_experiences(
                experiences
            )

            return

    experiences[goal].append({

        "strategy": strategy,

        "successes": 0,

        "failures": 1
    })

    save_experiences(
        experiences
    )


def get_experience(
    goal
):

    experiences = (
        load_experiences()
    )

    return experiences.get(
        goal
    )



def success_rate(
    successes,
    failures
):

    total = successes + failures

    if total == 0:

        return 0

    return successes / total


def select_best_strategy(
    strategies
):

    return max(

        strategies,

        key=lambda s: success_rate(

            s["successes"],

            s["failures"]
        )
    )


def get_best_strategy(
    goal
):

    experiences = load_experiences()

    if goal not in experiences:

        return None

    strategies = experiences[goal]

    best = select_best_strategy(
        strategies
    )

    return best["strategy"]