blackboard = {}


def set_state(key, value):

    blackboard[key] = value


def get_state(key):

    return blackboard.get(key)


def remove_state(key):

    if key in blackboard:

        del blackboard[key]


def show_blackboard():

    return blackboard