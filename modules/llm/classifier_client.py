import requests

OLLAMA_URL = (
    "http://localhost:11434/api/generate"
)

def classify(text):

    payload = {

        "model": "llama3.2:3b",

        "prompt": f"""
Return one word only.

CHAT
COMMAND
MIXED

Input:
{text}
""",

        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    return (
        response.json()["response"]
        .strip()
        .upper()
    )