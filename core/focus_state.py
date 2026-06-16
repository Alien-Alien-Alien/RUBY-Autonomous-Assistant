focus_state = {

    "focused_element": None
}


def set_focus(element):

    focus_state["focused_element"] = element


def get_focus():

    return focus_state["focused_element"]