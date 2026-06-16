plugin_states = {}


def register_plugin(

    plugin_name
):

    plugin_states[plugin_name] = (

        "registered"
    )


def set_plugin_state(

    plugin_name,

    state
):

    plugin_states[plugin_name] = state


def get_plugin_state(

    plugin_name
):

    return plugin_states.get(

        plugin_name
    )


def show_plugin_states():

    return plugin_states