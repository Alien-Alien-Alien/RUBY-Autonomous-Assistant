from modules.plugins.voice_plugin import (
    initialize
)

initialize()

from core.intent_executor import (
    execute_intent
)

from modules.memory.strategy_memory import (
    get_best_strategies
)

execute_intent(

    {
        "intent": "terminal",

        "target": "pwd"
    }
)

execute_intent(

    {
        "intent": "python",

        "target": "run",

        "query": "missing_file.py"
    }
)

print(

    get_best_strategies()
)