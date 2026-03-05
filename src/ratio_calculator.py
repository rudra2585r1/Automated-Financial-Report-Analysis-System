import re


def calculate_ratios(text):

    ratios = {}

    patterns = {
        "Gross Profit Margin": r"Gross Profit Margin\s*([0-9.]+)%",
        "Operating Margin": r"Operating Margin\s*([0-9.]+)%",
        "Net Profit Margin": r"Net Profit Margin\s*([0-9.]+)%",
        "Debt-to-Equity Ratio": r"Debt[- ]to[- ]Equity Ratio\s*([0-9.]+)",
        "Current Ratio": r"Current Ratio\s*([0-9.]+)"
    }

    for name, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            ratios[name] = match.group(1)

    return ratios