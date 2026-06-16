from modules.vision.ocr_reader import (
    read_text
)


def analyze_screen(path):

    result = read_text(path)

    if not result["success"]:
        return result

    text = result["text"].lower()

    findings = []

    context = {
        "app": None,
        "website": None,
        "project": None
    }

    # -------------------------
    # Applications
    # -------------------------

    if "chatgpt" in text:
        findings.append(
            "ChatGPT is open"
        )

    if "firefox" in text:
        findings.append(
            "Firefox is open"
        )

        context["app"] = "firefox"

    if "terminal" in text:
        findings.append(
            "Terminal is open"
        )

        context["app"] = "terminal"

    if "visual studio code" in text:
        findings.append(
            "VS Code detected"
        )

        context["app"] = "vscode"

    if "sublime" in text:
        findings.append(
            "Sublime Text detected"
        )

        context["app"] = "sublime"

    # -------------------------
    # Websites
    # -------------------------

    if "github" in text:
        findings.append(
            "GitHub detected"
        )

        context["website"] = "github"

    if "youtube" in text:
        findings.append(
            "YouTube detected"
        )

        context["website"] = "youtube"

    if "google" in text:
        findings.append(
            "Google detected"
        )

        context["website"] = "google"

    if "stackoverflow" in text:
        findings.append(
            "Stack Overflow detected"
        )

        context["website"] = "stackoverflow"

    if "reddit" in text:
        findings.append(
            "Reddit detected"
        )

        context["website"] = "reddit"

    if "huggingface" in text:
        findings.append(
            "Hugging Face detected"
        )

        context["website"] = "huggingface"

    # -------------------------
    # Programming
    # -------------------------

    if "python" in text:
        findings.append(
            "Python related work detected"
        )

    if ".py" in text:
        findings.append(
            "Python files detected"
        )

    if "traceback" in text:
        findings.append(
            "Python traceback detected"
        )

    if "error" in text:
        findings.append(
            "Error message detected"
        )

    if "exception" in text:
        findings.append(
            "Exception detected"
        )

    if "module not found" in text:
        findings.append(
            "Import error detected"
        )

    # -------------------------
    # Project Detection
    # -------------------------

    if "ai-assistant" in text:
        findings.append(
            "AI assistant project detected"
        )

        context["project"] = "ai-assistant"

    if "easyocr" in text:
        findings.append(
            "OCR development detected"
        )

    if "whisper" in text:
        findings.append(
            "Speech recognition work detected"
        )

    if "vosk" in text:
        findings.append(
            "Vosk speech system detected"
        )

    if "ollama" in text:
        findings.append(
            "Ollama detected"
        )

    if "piper" in text:
        findings.append(
            "Piper TTS detected"
        )

    # -------------------------
    # Cleanup
    # -------------------------

    findings = list(
        dict.fromkeys(findings)
    )

    confidence = min(
        len(findings) * 10,
        100
    )

    # -------------------------
    # Summary
    # -------------------------

    if findings:

        summary = (
            " | ".join(findings)
        )

    else:

        summary = (
            "No known activity detected"
        )

    return {
        "success": True,
        "summary": summary,
        "findings": findings,
        "context": context,
        "confidence": confidence,
        "raw_text": result["text"]
    }