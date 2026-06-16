from modules.memory.json_memory import JsonMemory


class UserMemory:

    def __init__(self):

        self.storage = JsonMemory(
            "memory/user_memory.json"
        )

        data = self.storage.load()

        self.facts = data.get(
            "facts",
            []
        )

    def save(self):

        self.storage.save(
            {
                "facts": self.facts
            }
        )

    def add_fact(self, fact):

        fact = fact.strip().lower()

        existing = [
            f.lower()
            for f in self.facts
        ]

        if fact in existing:
            return

        self.facts.append(fact)

        self.save()
    def remove_fact(self, fact):

        self.facts = [

            f

            for f in self.facts

            if fact.lower() not in f.lower()
        ]

        self.save()

    def get_all(self):

        return self.facts

    def clear(self):

        self.facts = []

        self.save()