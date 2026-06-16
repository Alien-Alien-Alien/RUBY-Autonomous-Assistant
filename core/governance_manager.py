from core.health_manager import (
    health_status
)
from core.runtime_policy import (
    set_policy
)


class GovernanceManager:


    def evaluate(self):

        status = health_status()

        print(
            f"[Governance] Health: {status}"
        )

        if status == "HEALTHY":

            set_policy(
                "monitoring_level",
                "normal"
            )

            return {
                "action": "continue"
            }


        if status == "WARNING":

            set_policy(
                "monitoring_level",
                "high"
            )

            return {
                "action": "increase_monitoring"
            }


        set_policy(
            "allow_low_priority_goals",
            False
        )

        set_policy(
            "monitoring_level",
            "critical"
        )

        return {
            "action": "stabilize_runtime"
        }