import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def warmup_models():

    for model in [
        "qwen2.5:7b",
        "llama3.2:3b"
    ]:

        requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": "hi",
                "keep_alive": "30m",
                "stream": False
            }
        )