from modules.agents.chatgpt_agent import (
    ChatGPTAgent
)

agent = ChatGPTAgent()

print(

    agent.send_message(
        "hello from my ai assistant"
    )
)