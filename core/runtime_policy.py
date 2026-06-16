runtime_policy = {

    "allow_low_priority_goals": True,

    "recovery_interval": 5,

    "monitoring_level": "normal"
}


def set_policy(

    key,

    value
):

    runtime_policy[key] = value


def get_policy(

    key
):

    return runtime_policy.get(
        key
    )


def show_policy():

    return runtime_policy