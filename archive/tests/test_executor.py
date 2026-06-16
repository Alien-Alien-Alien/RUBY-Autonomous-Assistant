import json

from modules.llm.ollama_client import ask_llm

from core.intent_executor import execute_intent

from core.intent_resolver import resolve_intent

from core.intent_validator import validate_intent

from modules.memory.long_term_memory import load_memory


load_memory()


response = ask_llm(

    "open browser"
)

print(response)


task_list = json.loads(response)


for task in task_list:

    resolved_task = resolve_intent(task)

    print(resolved_task)


    if validate_intent(resolved_task):

        execute_intent(resolved_task)

    else:

        print("Invalid intent:", resolved_task)