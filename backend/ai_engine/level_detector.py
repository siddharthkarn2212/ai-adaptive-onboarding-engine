def detect_level(text):
    text = text.lower()

    if "intern" in text or "fresher" in text:
        return "Beginner"
    elif "experience" in text or "worked" in text:
        return "Intermediate"
    elif "senior" in text or "lead" in text:
        return "Advanced"
    else:
        return "Unknown"