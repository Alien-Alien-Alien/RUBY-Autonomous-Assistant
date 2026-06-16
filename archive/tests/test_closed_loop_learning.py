from core.bootstrap import (
    initialize_runtime
)

from modules.agents.execution_agent import (
    ExecutionAgent
)

initialize_runtime()

agent = ExecutionAgent()

task = {

    "intent": "open_app",

    "target": "firefox"
}

agent.execute(task)
