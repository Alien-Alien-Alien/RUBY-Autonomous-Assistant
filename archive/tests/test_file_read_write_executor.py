from core.bootstrap import (
    initialize_runtime
)

from core.intent_executor import (
    execute_intent
)

initialize_runtime()

execute_intent({

    "intent": "file",

    "target": "write",

    "query": "executor_test.txt|hello world"
})

execute_intent({

    "intent": "file",

    "target": "read",

    "query": "executor_test.txt"
})