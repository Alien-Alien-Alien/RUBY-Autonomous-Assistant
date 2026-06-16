from core.telemetry import (
    record_failure
)

from core.governance_manager import (
    GovernanceManager
)


for _ in range(6):

    record_failure(
        "voice_plugin"
    )


manager = GovernanceManager()

decision = manager.evaluate()

print(
    decision
)