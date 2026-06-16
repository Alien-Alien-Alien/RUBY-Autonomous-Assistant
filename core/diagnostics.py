from core.telemetry import telemetry


def run_diagnostics():

    report = []

    failures = telemetry["plugin_failures"]

    for plugin, count in failures.items():

        if count >= 3:

            report.append(

                f"UNSTABLE PLUGIN: {plugin}"
            )

    execution_times = telemetry["execution_times"]

    for intent, duration in execution_times.items():

        if duration > 5:

            report.append(

                f"SLOW EXECUTION: {intent}"
            )

    if not report:

        report.append(

            "SYSTEM HEALTHY"
        )

    return report