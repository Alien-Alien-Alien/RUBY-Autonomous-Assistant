from dataclasses import dataclass


@dataclass
class Task:

    intent: str

    target: str = ""

    query: str = ""