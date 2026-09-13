import re


# ============================================================
# NAME EXTRACTION
# ============================================================

def extract_name(text):
    """
    Extract a person's name from common phrases.

    Examples:
        My name is Siraj
        I am Siraj
        I'm Siraj
        This is Siraj

    Returns:
        Extracted name as a string, or None.
    """

    patterns = [
        r"\bmy name is\s+([A-Za-z]+(?:\s+[A-Za-z]+)?)",
        r"\bi am\s+([A-Za-z]+(?:\s+[A-Za-z]+)?)",
        r"\bi'm\s+([A-Za-z]+(?:\s+[A-Za-z]+)?)",
        r"\bthis is\s+([A-Za-z]+(?:\s+[A-Za-z]+)?)"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            name = match.group(1).strip()

            return name.title()

    return None


# ============================================================
# EMAIL EXTRACTION
# ============================================================

def extract_email(text):
    """
    Extract an email address from a text message.

    Returns:
        Extracted email as a string, or None.
    """

    email_pattern = (
        r"\b[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}\b"
    )

    match = re.search(
        email_pattern,
        text
    )

    if match:
        return match.group(0).lower()

    return None


# ============================================================
# FIELD / PROGRAM EXTRACTION
# ============================================================

FIELD_ALIASES = {

    "computer science": [
        "computer science",
        "computer science engineering",
        "cse"
    ],

    "data science": [
        "data science",
        "data science engineering",
        "ds"
    ],

    "artificial intelligence": [
        "artificial intelligence",
        "ai"
    ],

    "machine learning": [
        "machine learning",
        "ml"
    ],

    "electronics and communication engineering": [
        "electronics and communication engineering",
        "electronics communication engineering",
        "ece"
    ],

    "electrical and electronics engineering": [
        "electrical and electronics engineering",
        "electrical electronics engineering",
        "eee"
    ],

    "information technology": [
        "information technology",
        "it"
    ],

    "mechanical engineering": [
        "mechanical engineering",
        "mechanical",
        "mech"
    ],

    "civil engineering": [
        "civil engineering",
        "civil"
    ]
}


def extract_field(text):
    """
    Extract the student's field/program from text.

    Examples:
        I study computer science
        I am a CSE student
        My field is data science
        I study AI
        I am an ECE student

    Returns:
        Standardized field name, or None.
    """

    text_lower = text.lower()

    # Check longer phrases first
    # to avoid matching shorter terms incorrectly.
    aliases = []

    for field, field_aliases in FIELD_ALIASES.items():

        for alias in field_aliases:

            aliases.append(
                (alias, field)
            )

    aliases.sort(
        key=lambda item: len(item[0]),
        reverse=True
    )

    for alias, field in aliases:

        pattern = r"\b" + re.escape(alias) + r"\b"

        if re.search(pattern, text_lower):

            return field

    return None


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    test_messages = [

        # Name tests
        "My name is Siraj",
        "I am Siraj",
        "I'm Siraj",
        "This is John",

        # Email tests
        "My email is siraj@gmail.com",
        "Contact me at student123@gmail.com",

        # Field tests
        "I study computer science",
        "I am a CSE student",
        "My field is data science",
        "I am studying artificial intelligence",
        "I know machine learning",
        "I am an ECE student",
        "My degree is EEE",
        "I study information technology",
        "I am studying mechanical engineering",
        "I study civil engineering"
    ]

    print("Entity Extraction Tests")
    print("=" * 60)

    for message in test_messages:

        name = extract_name(message)
        email = extract_email(message)
        field = extract_field(message)

        print(f"\nUser: {message}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Field: {field}")