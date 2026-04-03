KEYWORDS = {
    "Billing": ["payment", "refund", "invoice"],
    "Technical": ["error", "bug", "crash"],
    "Account": ["login", "password"],
    "Feature Request": ["feature", "request"]
}

URGENCY_WORDS = ["urgent", "asap", "immediately", "down"]

def analyze_ticket(message: str):
    msg = message.lower()

    category = "Other"
    matched = []

    for cat, words in KEYWORDS.items():
        for word in words:
            if word in msg:
                category = cat
                matched.append(word)

    urgency = any(word in msg for word in URGENCY_WORDS)

    # 🔥 Custom Rule (MANDATORY)
    if "refund" in msg and "urgent" in msg:
        priority = "P0"
    elif urgency and category == "Technical":
        priority = "P0"
    elif urgency:
        priority = "P1"
    elif category != "Other":
        priority = "P2"
    else:
        priority = "P3"

    confidence = round(len(matched) / 5, 2)

    return category, priority, confidence
