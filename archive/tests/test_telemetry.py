from core.telemetry import (

    show_telemetry,

    record_execution,

    record_failure,

    record_recovery
)


record_execution(

    "open_app"
)

record_execution(

    "google_search"
)

record_failure(

    "voice_plugin"
)

record_recovery(

    "voice_plugin"
)


print(

    show_telemetry()
)