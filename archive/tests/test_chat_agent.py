from modules.agents.chat_agent import (
    ChatAgent
)

agent = ChatAgent()

print(
    agent.reply(
        "What is robotics?"
    )
)