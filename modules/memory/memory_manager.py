from modules.memory.chat_memory import (
    ChatMemory
)

from modules.memory.chat_summary import (
    ChatSummary
)

from modules.memory.user_memory import (
    UserMemory
)
from modules.memory.project_memory import (
    ProjectMemory
)

class MemoryManager:

    def __init__(self):

        self.chat = ChatMemory()

        self.summary = ChatSummary()

        self.user = UserMemory()

        self.project = ProjectMemory()

        
    def get_context(self):

        return {

            "history":
                self.chat.recent(),

            "summary":
                self.summary.get(),

            "user_facts":
                "\n".join(
                    self.user.get_all()
                ),

            "projects":
                self.project.get_all()
        }

    def clear_chat(self):

        self.chat.clear()

    def clear_summary(self):

        self.summary.clear()

    def clear_user_memory(self):

        self.user.clear()

    def clear_all(self):

        self.chat.clear()

        self.summary.clear()

        self.user.clear()