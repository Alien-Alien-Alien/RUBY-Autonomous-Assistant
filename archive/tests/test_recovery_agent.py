from modules.plugins.voice_plugin import (
    initialize
)

initialize()

from core.intent_executor import (
    execute_intent
)

from modules.agents.recovery_agent import (
    RecoveryAgent
)


task = {

    "intent": "open_app"
}


agent = RecoveryAgent()


fixed_task = agent.recover(
    task
)


print(

    "Recovered Task:",
    fixed_task
)


if fixed_task:

    result = execute_intent(
        fixed_task
    )

    print(result)