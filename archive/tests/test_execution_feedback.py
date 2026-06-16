from core.bootstrap import (
    initialize_runtime
)

from core.intent_executor import (
    execute_intent
)

initialize_runtime()

print(

    execute_intent({

        "intent": "open_app",

        "target": "firefox"
    })
)

print(

    execute_intent({

        "intent": "open_app",

        "target": "nonexistent"
    })
)