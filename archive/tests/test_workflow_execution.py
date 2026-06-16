from modules.plugins.voice_plugin import (
    initialize
)

initialize()

from modules.agents.workflow_agent import (
    WorkflowAgent
)

agent = WorkflowAgent()

result = agent.run_workflow(

    "research_workflow"
)

print(result)