from core.telemetry import telemetry


def calculate_health_score():

    score = 100

    failures = sum(
        telemetry["plugin_failures"].values()
    )

    recoveries = sum(
        telemetry["plugin_recoveries"].values()
    )

    score -= failures * 10
    score += recoveries * 5

    score = max(0, min(100, score))

    return score


def health_status():

    score = calculate_health_score()

    if score >= 80:
        return "HEALTHY"

    if score >= 50:
        return "WARNING"

    return "CRITICAL"