import json
import os


MEMORY_FILE = "data/long_term_memory.json"


memory_data = {}


def load_memory():

    global memory_data

    if not os.path.exists(MEMORY_FILE):

        memory_data = {}

        return

    with open(MEMORY_FILE, "r") as file:

        try:

            memory_data = json.load(file)

        except json.JSONDecodeError:

            memory_data = {}



def save_memory():

    with open(MEMORY_FILE, "w") as file:

        json.dump(

            memory_data,

            file,

            indent=4
        )



def remember(key, value):

    memory_data[key] = value

    save_memory()



def recall(key):

    return memory_data.get(key)