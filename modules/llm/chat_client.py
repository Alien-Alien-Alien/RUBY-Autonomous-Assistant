import requests

from modules.configs.personality import (
    ASSISTANT_NAME,
    PERSONALITY
)
import time
OLLAMA_URL = (
    "http://localhost:11434/api/generate"
)


def ask_chat(prompt):

    payload = {

        "model": "qwen2.5:7b",

        "keep_alive": "30m",

        "prompt": f"""
Name:
{ASSISTANT_NAME}

{PERSONALITY}

Rules:

* Do not use emojis, emoticons, or symbols.
* Respond to the user's actual intent.
* Match the user's tone naturally.
* Be concise by default.
* Expand only when asked.
* Use conversation history when relevant.
* Do not force jokes, games, excitement, or playful behavior.
* If the user is serious, be serious.
* If the user is casual, be casual.
* If the user is annoyed, respond calmly and directly.
* Avoid generic assistant phrases.
* Avoid repeating yourself.
* Stay consistent with previous conversation.
* Never ignore the user's question.
* Prefer clarity over personality.
* Do not invent facts, events, or game states.
* When information is missing, ask a clarifying question.
* Keep greetings under 5 words unless more detail is requested.
* For simple acknowledgements, use one short sentence.
* Do not act overly cheerful unless the user initiates that tone.
* Only use capabilities explicitly listed above.
* Never invent new intents.
Conversation:

{prompt}
""",

        "stream": False
    }

    start = time.time()

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    print(
        "OLLAMA REQUEST:",
        time.time() - start
    )

    data = response.json()

    return data["response"].strip()