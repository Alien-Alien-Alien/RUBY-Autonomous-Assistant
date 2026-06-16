from core.telemetry import (
    record_failure
)

from core.governance_manager import (
    GovernanceManager
)

from core.runtime_policy import (
    show_policy
)


for _ in range(6):

    record_failure(
        "voice_plugin"
    )


manager = GovernanceManager()

manager.evaluate()

print()

print(
    show_policy()
)