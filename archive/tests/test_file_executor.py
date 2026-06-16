from core.bootstrap import (
    initialize_runtime
)

from core.intent_executor import (
    execute_intent
)

initialize_runtime()

execute_intent({

    "intent": "file",

    "target": "create_folder",

    "query": "agent_test"
})

execute_intent({

    "intent": "file",

    "target": "list"
})

execute_intent({

    "intent": "file",

    "target": "delete_folder",

    "query": "agent_test"
})