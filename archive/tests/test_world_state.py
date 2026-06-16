from modules.plugins.voice_plugin import (
    initialize
)

initialize()

from core.intent_executor import (
    execute_intent
)

from core.world_state import (
    get_state
)

execute_intent(

    {
        "intent": "terminal",

        "target": "pwd"
    }
)

print(

    get_state()
)