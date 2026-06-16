from modules.agents.context_agent import (
    ContextAgent
)

agent = ContextAgent()

result = agent.build_context()

print(result)