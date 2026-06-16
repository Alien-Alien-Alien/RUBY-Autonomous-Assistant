from modules.agents.response_agent import (
    ResponseAgent
)

agent = ResponseAgent()

print(
    agent.respond(
        {
            "success": True,
            "query": "robotics"
        }
    )
)