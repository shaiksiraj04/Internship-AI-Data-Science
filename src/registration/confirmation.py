"""
Registration confirmation utilities.

This module handles:
- Creating a readable registration summary
- Interpreting confirmation responses
"""


def create_summary(name, email, field):
    """
    Create a formatted registration summary.

    Args:
        name (str): Student's name
        email (str): Student's email
        field (str): Student's field of study

    Returns:
        str: Formatted registration summary
    """

    summary = (
        "\nRegistration Summary:\n"
        "---------------------\n"
        f"Name  : {name}\n"
        f"Email : {email}\n"
        f"Field : {field}\n"
        "---------------------\n"
        "Are these details correct? (yes/no)"
    )

    return summary


def interpret_confirmation(text):
    """
    Interpret the user's confirmation response.

    Args:
        text (str): User's response

    Returns:
        str: 'yes', 'no', or 'unknown'
    """

    if not text:
        return "unknown"

    response = text.strip().lower()

    yes_words = {
        "yes",
        "y",
        "yeah",
        "yep",
        "correct",
        "right",
        "confirm",
        "confirmed",
        "sure",
        "okay",
        "ok"
    }

    no_words = {
        "no",
        "n",
        "nope",
        "wrong",
        "incorrect",
        "cancel"
    }

    if response in yes_words:
        return "yes"

    if response in no_words:
        return "no"

    return "unknown"


if __name__ == "__main__":
    print("Testing confirmation module...\n")

    summary = create_summary(
        "Siraj",
        "siraj@example.com",
        "computer science"
    )

    print(summary)

    print("\nConfirmation tests:")

    test_responses = [
        "yes",
        "y",
        "correct",
        "no",
        "n",
        "maybe"
    ]

    for response in test_responses:
        result = interpret_confirmation(response)
        print(f"{response} -> {result}")

    print("\nConfirmation module test completed.")