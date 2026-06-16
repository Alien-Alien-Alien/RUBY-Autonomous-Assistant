from dataclasses import dataclass

from typing import List

from core.schemas.task_schema import Task


@dataclass
class Plan:

    goal: str

    tasks: List[Task]