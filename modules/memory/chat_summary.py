from modules.memory.json_memory import JsonMemory


class ChatSummary:

    def __init__(self):

        self.storage = JsonMemory(
            "memory/chat_summary.json"
        )


        data = self.storage.load()
        if not data:
            data = {"summary": ""}
            self.storage.save(data)

        self.summary = data.get(
            "summary",
            ""
        )

    def get(self):
        return self.summary

    def set(self, text):

        self.summary = text

        self.storage.save(
            {
                "summary": text
            }
        )

        
    def clear(self):

        self.summary = ""

        self.storage.save(
            {
                "summary": ""
            }
        )


    def append(self, text):

        if not text:
            return

        if self.summary:

            self.summary += "\n" + text

        else:

            self.summary = text

        self.storage.save(
            {
                "summary": self.summary
            }
        )