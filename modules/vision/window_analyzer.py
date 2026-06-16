def analyze_window(title):

    findings = []

    title_lower = title.lower()

    if "ai-assistant" in title_lower:
        findings.append(
            "Working on AI Assistant project"
        )

    if "terminal" in title_lower:
        findings.append(
            "Using terminal"
        )

    if ".py" in title_lower:
        findings.append(
            "Editing Python file"
        )

    if "firefox" in title_lower:
        findings.append(
            "Using Firefox"
        )

    if "chatgpt" in title_lower:
        findings.append(
            "ChatGPT open"
        )

    return findings