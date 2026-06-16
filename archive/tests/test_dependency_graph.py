from modules.agents.dependency_graph import (
    DependencyGraph
)

agent = DependencyGraph()

print(

    agent.analyze(
        "modules/agents/execution_agent.py"
    )
)