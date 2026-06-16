from modules.agents.import_analyzer import (
    ImportAnalyzer
)

agent = ImportAnalyzer()

print(

    agent.find_users(
        "core.intent_executor"
    )
)