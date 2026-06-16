from modules.plugins.voice_plugin import (
    initialize
)

initialize()

from core.intent_executor import (
    execute_intent
)

result = execute_intent(

    {
        "intent": "python",

        "target": "run",

        "query": "missing_file.py"
    }
)

print(result)