import time

from modules.llm.chat_client import (
    ask_chat
)

start = time.time()

response = ask_chat(
    "Say hello in one sentence."
)

print(response)

print(
    "\nTIME:",
    time.time() - start
)