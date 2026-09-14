"""
FAQ module for the AI Registration Assistant.

This module:
- Loads FAQ data from JSON
- Searches for matching FAQ questions
- Returns appropriate answers
"""

import json
from pathlib import Path


# -------------------------------------------------
# File path
# -------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

FAQ_PATH = PROJECT_ROOT / "data" / "faq.json"


# -------------------------------------------------
# Load FAQ data
# -------------------------------------------------

def load_faqs():
    """Load FAQs from the JSON file."""

    try:

        with open(
            FAQ_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data.get("faqs", [])

    except FileNotFoundError:

        print("Warning: faq.json was not found.")

        return []

    except json.JSONDecodeError:

        print("Warning: faq.json contains invalid JSON.")

        return []


# -------------------------------------------------
# Keyword matching
# -------------------------------------------------

def find_faq(text):
    """
    Find the best FAQ answer for a user message.

    Args:
        text (str): User message

    Returns:
        str or None: FAQ answer if a match is found
    """

    if not text or not text.strip():
        return None

    user_text = text.lower()

    faqs = load_faqs()

    best_match = None
    best_score = 0

    for faq in faqs:

        score = 0

        keywords = faq.get("keywords", [])

        for keyword in keywords:

            if keyword.lower() in user_text:
                score += 1

        if score > best_score:

            best_score = score
            best_match = faq

    if best_match and best_score > 0:

        return best_match.get("answer")

    return None


# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("              FAQ SYSTEM TEST")
    print("=" * 60)

    questions = [
        "What information do I need?",
        "Which fields are supported?",
        "Can I correct my details?",
        "What happens after registration?",
        "How can I get help?",
        "Can I register again?"
    ]

    for question in questions:

        print()
        print("Question:", question)

        answer = find_faq(question)

        if answer:

            print("Answer:", answer)

        else:

            print("No FAQ found.")

    print()
    print("FAQ system test completed.")