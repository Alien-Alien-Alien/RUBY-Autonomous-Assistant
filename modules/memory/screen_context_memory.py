from collections import deque
from datetime import datetime


class ScreenContextMemory:

    def __init__(self, max_items=20):

        self.history = deque(
            maxlen=max_items
        )

    def add(self, summary):

        self.history.append(
            {
                "time": datetime.now(),
                "summary": summary
            }
        )

    def latest(self):

        if not self.history:
            return None

        return self.history[-1]

    def recent(self, count=5):

        return list(
            self.history
        )[-count:]

    def get_activity_chain(self):

        if not self.history:
            return "No history"

        return "\n".join(
            item["summary"]
            for item in self.history
        )