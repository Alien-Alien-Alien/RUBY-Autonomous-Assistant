from modules.llm.chat_client import ask_chat


class IntentClassifier:

    def classify(self, text):

        prompt = f"""
Classify the user input.

Return ONLY one word:

CHAT
COMMAND
MIXED

Examples:

open firefox
COMMAND

what is firefox
CHAT

open firefox and tell me what firefox is
MIXED

Input:
{text}
"""

        result = ask_chat(prompt)

        return result.strip().upper()