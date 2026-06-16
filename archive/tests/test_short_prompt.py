# test_short_prompt.py

import time

from modules.agents.chat_agent import ChatAgent

start = time.time()

response = ChatAgent().reply(
    "Answer in one sentence: what is robotics?"
)

print(response)

print(
    "\nTIME:",
    round(time.time() - start, 2)
)