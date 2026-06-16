from modules.agents.screen_awareness_agent import (
    ScreenAwarenessAgent
)

agent = ScreenAwarenessAgent()

result = agent.observe()

print(
    result["text"][:1000]
)