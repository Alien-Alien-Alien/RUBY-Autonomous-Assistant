import json


MEMORY_FILE = (
    "data/strategy_memory.json"
)


def load_memory():

    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return {}


def save_memory(memory):

    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            memory,
            file,
            indent=4
        )


def record_strategy(

    strategy,

    success
):

    memory = load_memory()

    if strategy not in memory:

        memory[strategy] = {

            "success": 0,

            "failure": 0
        }

    if success:

        memory[strategy]["success"] += 1

    else:

        memory[strategy]["failure"] += 1

    save_memory(memory)


def get_best_strategies():

    memory = load_memory()

    ranked = sorted(

        memory.items(),

        key=lambda x:
        x[1]["success"],

        reverse=True
    )

    return ranked