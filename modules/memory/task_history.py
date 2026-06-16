from modules.memory.json_memory import (
    JsonMemory
)


class TaskHistory:

    def __init__(self):

        self.storage = JsonMemory(
            "memory/task_history.json"
        )

        data = self.storage.load()

        self.history = data.get(
            "history",
            []
        )

    def add(self, task):

        if not task:
            return

        self.history.append(
            task
        )

        self.history = (
            self.history[-20:]
        )

        self.storage.save(
            {
                "history":
                self.history
            }
        )

    def recent(self, count=5):

        return self.history[-count:]

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]