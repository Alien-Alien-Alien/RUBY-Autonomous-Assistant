import json


MEMORY_FILE = (
    "data/workflow_memory.json"
)


def load_workflows():

    try:

        with open(
            MEMORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return {}


def save_workflows(workflows):

    with open(
        MEMORY_FILE,
        "w"
    ) as file:

        json.dump(
            workflows,
            file,
            indent=4
        )


def remember_workflow(

    name,

    tasks
):

    workflows = load_workflows()

    workflows[name] = tasks

    save_workflows(workflows)


def get_workflow(name):

    workflows = load_workflows()

    return workflows.get(name)