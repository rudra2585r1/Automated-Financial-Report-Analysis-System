def detect_red_flags(text):

    risk_keywords = [
        "risk",
        "competition",
        "cybersecurity",
        "economic slowdown",
        "decline",
        "loss",
        "uncertain",
        "debt",
        "threat"
    ]

    detected = []

    text_lower = text.lower()

    for word in risk_keywords:

        if word in text_lower:
            detected.append(word)

    return detected