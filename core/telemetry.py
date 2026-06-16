import time


telemetry = {

    "plugin_failures": {},

    "plugin_recoveries": {},

    "execution_counts": {},

    "execution_times": {}
}


def record_failure(

    plugin_name
):

    telemetry["plugin_failures"][

        plugin_name
    ] = telemetry[

        "plugin_failures"

    ].get(

        plugin_name,

        0
    ) + 1


def record_recovery(

    plugin_name
):

    telemetry["plugin_recoveries"][

        plugin_name
    ] = telemetry[

        "plugin_recoveries"

    ].get(

        plugin_name,

        0
    ) + 1


def record_execution(

    intent
):

    telemetry["execution_counts"][

        intent
    ] = telemetry[

        "execution_counts"

    ].get(

        intent,

        0
    ) + 1


def record_execution_time(

    intent,

    duration
):

    telemetry["execution_times"][

        intent
    ] = duration


def show_telemetry():

    return telemetry