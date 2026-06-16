from modules.memory.json_memory import (
    JsonMemory
)


class ProjectMemory:

    def __init__(self):

        self.storage = JsonMemory(
            "memory/project_memory.json"
        )

        data = self.storage.load()

        if not data:

            data = {
                "projects": {}
            }

            self.storage.save(data)

        self.projects = data.get(
            "projects",
            {}
        )

    def save(self):

        self.storage.save(
            {
                "projects": self.projects
            }
        )

    def set_project(
        self,
        name,
        data
    ):

        self.projects[name] = data

        self.save()

    def get_project(
        self,
        name
    ):

        return self.projects.get(
            name
        )

    def get_all(self):

        return self.projects

    def delete_project(
        self,
        name
    ):

        if name in self.projects:

            del self.projects[name]

            self.save()