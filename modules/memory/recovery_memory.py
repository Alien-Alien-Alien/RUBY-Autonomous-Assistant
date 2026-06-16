import json


MEMORY_FILE = (
    "data/recovery_memory.json"
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


def remember_fix(

    problem,

    solution
):

    memory = load_memory()

    memory[problem] = solution

    save_memory(memory)


def get_fix(problem):

    memory = load_memory()

    return memory.get(problem)