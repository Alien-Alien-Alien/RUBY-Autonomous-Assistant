from core.bootstrap import (
    initialize_runtime
)

from core.intent_executor import (
    execute_intent
)

from core.experience_memory import (
    load_experiences
)

initialize_runtime()

execute_intent({

    "intent": "open_app",

    "target": "firefox"
})

print(

    load_experiences()
)