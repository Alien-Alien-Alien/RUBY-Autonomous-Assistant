import json

HISTORY_FILE = "data/history.json"


def load_history():

    try:

        with open(HISTORY_FILE, "r") as file:

            return json.load(file)

    except:

        return []



def save_command(command):

    history = load_history()

    history.append(command)

    with open(HISTORY_FILE, "w") as file:

        json.dump(history, file, indent=4)



def get_history():

    return load_history()