from modules.llm.chat_client import (
    ask_chat
)

from modules.memory.memory_manager import (
    MemoryManager
)

import time


class ChatAgent:

    def __init__(self):

        self.memory = MemoryManager()

    def reply(self, text):

        start = time.time()

        lower = text.lower().strip()


        if lower in {

            "show memory",
            "show user memory"

        }:

            facts = self.memory.user.get_all()

            if not facts:

                return "Memory is empty."

            return "\n".join(facts)

        # -------------------------
        # USER MEMORY COMMANDS
        # -------------------------

        if lower.startswith("remember "):

            fact = text[9:].strip()

            self.memory.user.add_fact(
                fact
            )

            return "I'll remember that."

        if lower.startswith("forget "):

            fact = text[7:].strip()

            self.memory.user.remove_fact(
                fact
            )

            return "I've forgotten that."

        if lower == "show memory" or lower == "show user memory":

            facts = self.memory.user.get_all()

            if not facts:
                return "I am not remembering anything."

            return "\n".join(
                f"- {fact}"
                for fact in facts
            )

        if lower == "clear user memory":

            self.memory.user.clear()

            return "User memory cleared."


        if lower == "forget everything":

            self.memory.user.clear()

            return "I've forgotten everything in user memory."

        # -------------------------
        # CHAT MEMORY
        # -------------------------

        self.memory.chat.add_user(
            text
        )

        print(
            "[HISTORY SIZE]",
            len(self.memory.chat.messages)
        )

        context = self.memory.get_context()

        history = context["history"]

        summary = context["summary"]

        user_facts = context["user_facts"]

        print(
            "\n===== USER MEMORY ====="
        )
        print(user_facts)
        print(
            "=======================\n"
        )

        print(
            "\n===== SUMMARY ====="
        )
        print(summary)
        print(
            "===================\n"
        )

        print(
            "\n===== HISTORY ====="
        )
        print(history)
        print(
            "===================\n"
        )

        response = ask_chat(
    f"""
User Memory:

{user_facts}

Use these facts only if they are relevant.
Do not mention them unless needed.

Conversation Summary:

{summary}

Recent Conversation:

{history}

Latest User Message:

{text}

Respond naturally to the latest user message.
"""
)

        self.memory.chat.add_assistant(
            response
        )

        print(
            "\nCHAT TIME:",
            time.time() - start
        )

        return response