class TaskInferenceAgent:

    def infer(
        self,
        window_findings,
        screen_findings,
        recent_context
    ):

        if isinstance(
            window_findings,
            str
        ):
            window_findings = [
                window_findings
            ]

        if isinstance(
            screen_findings,
            str
        ):
            screen_findings = [
                screen_findings
            ]

        if isinstance(
            recent_context,
            str
        ):
            recent_context = [
                recent_context
            ]

        text = " ".join(
            window_findings
            +
            screen_findings
            +
            recent_context
        ).lower()

        if "ocr" in text:
            return (
                "Working on OCR system"
            )

        if "voice" in text:
            return (
                "Working on voice system"
            )

        if "whisper" in text:
            return (
                "Improving speech recognition"
            )

        if "ai assistant" in text:
            return (
                "Developing AI assistant"
            )

        if "python" in text:
            return (
                "Programming in Python"
            )

        return (
            "Task unknown"
        )