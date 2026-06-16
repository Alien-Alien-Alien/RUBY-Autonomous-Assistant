from modules.agents.recovery_agent import (
    RecoveryAgent
)

agent = RecoveryAgent()

task = {

    "intent": "open_app"
}

print(

    "FIRST RUN\n"
)

result1 = agent.recover(
    task
)

print(result1)

print("\nSECOND RUN\n")

task2 = {

    "intent": "open_app"
}

result2 = agent.recover(
    task2
)

print(result2)