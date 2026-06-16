from modules.agents.workflow_agent import (
    WorkflowAgent
)

agent = WorkflowAgent()

tasks = agent.run(
    "inspect project"
)

for task in tasks:

    print(task)