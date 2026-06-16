from modules.memory.workflow_memory import (

    remember_workflow,

    get_workflow
)

workflow = [

    {
        "intent": "open_app",
        "target": "firefox"
    },

    {
        "intent": "google_search",
        "query": "robotics research papers"
    }
]

remember_workflow(

    "research_workflow",

    workflow
)

loaded = get_workflow(
    "research_workflow"
)

print(loaded)