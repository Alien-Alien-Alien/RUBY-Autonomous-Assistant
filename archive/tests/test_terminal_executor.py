from core.bootstrap import (
    initialize_runtime
)

from core.intent_executor import (
    execute_intent
)

initialize_runtime()

execute_intent({

    "intent": "terminal",

    "target": "pwd"
})