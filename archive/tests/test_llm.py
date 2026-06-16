from modules.llm.ollama_client import (
    ask_llm
)

response = ask_llm(

    "analyze project"
)

print(

    "RAW RESPONSE:\n"
)

print(
    response
)