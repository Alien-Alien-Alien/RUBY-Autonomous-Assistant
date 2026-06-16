from modules.memory.memory_manager import (
    MemoryManager
)

memory = MemoryManager()

memory.project.set_project(
    "ruby",
    {
        "completed": [
            "Voice Input",
            "Voice Output",
            "OCR"
        ],
        "current_task":
            "Project Memory"
    }
)

print(
    memory.project.get_project(
        "ruby"
    )
)