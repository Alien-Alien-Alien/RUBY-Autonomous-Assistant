from modules.memory.json_memory import (
    JsonMemory
)

MAX_MESSAGES = 20
KEEP_RECENT = 10


class ChatMemory:

    def __init__(self):

        self.storage = JsonMemory(
            "memory/chat_memory.json"
        )

        data = self.storage.load()

        if not data:
            data = {
                "messages": []
            }
            self.storage.save(data)

        self.messages = data.get(
            "messages",
            []
        )

        self._trim_if_needed()

    def _trim_if_needed(self):

        if len(self.messages) > MAX_MESSAGES:

            self.messages = self.messages[
                -KEEP_RECENT:
            ]

            self.save()

    def save(self):

        self.storage.save(
            {
                "messages": self.messages
            }
        )

    def add_user(self, text):

        ignore = {

            "hi",
            "hello",
            "hey",
            "ok",
            "okay",
            "thanks",
            "thank you",

            "show memory",
            "show user memory",
            "clear user memory",
            "forget everything"
        }

        if text.lower().strip() in ignore:
            return

        self.messages.append(
            f"User: {text}"
        )

        self.save()

        self._trim_if_needed()
    def add_assistant(self, text):

        self.messages.append(
            f"Assistant: {text}"
        )

        self.save()
        self._trim_if_needed()


    def recent(self, count=12):

        return "\n".join(
            self.messages[-count:]
        )

    def clear(self):

        self.messages = []

        self.save()