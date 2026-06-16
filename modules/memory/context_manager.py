import json

CONTEXT_FILE = "data/context.json"


def load_context():

    try:

        with open(CONTEXT_FILE, "r") as file:

            return json.load(file)

    except:

        return {}



def save_context(context):

    with open(CONTEXT_FILE, "w") as file:

        json.dump(context, file, indent=4)



def update_context(key, value):

    context = load_context()

    context[key] = value

    save_context(context)



def get_context(key):

    context = load_context()

    return context.get(key)