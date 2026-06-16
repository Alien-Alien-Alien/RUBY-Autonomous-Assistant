from core.telemetry import (
    record_failure,
    record_recovery
)

from core.health_manager import (
    calculate_health_score,
    health_status
)

record_failure("voice_plugin")
record_failure("voice_plugin")
record_recovery("voice_plugin")

print(
    calculate_health_score()
)

print(
    health_status()
)