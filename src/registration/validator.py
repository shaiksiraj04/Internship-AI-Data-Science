import re


# ============================================================
# VALID FIELD / PROGRAM LIST
# ============================================================

VALID_FIELDS = {
    "computer science",
    "data science",
    "artificial intelligence",
    "machine learning",
    "electronics and communication engineering",
    "electrical and electronics engineering",
    "information technology",
    "mechanical engineering",
    "civil engineering"
}


# ============================================================
# NAME VALIDATION
# ============================================================

def validate_name(name):
    """
    Validate a student's name.

    Rules:
        - Name must not be empty.
        - Name must contain only letters and spaces.
        - Name must contain at least 2 characters.

    Returns:
        True if valid, otherwise False.
    """

    if not name:
        return False

    name = name.strip()

    if len(name) < 2:
        return False

    if not re.fullmatch(
        r"[A-Za-z]+(?:\s+[A-Za-z]+)*",
        name
    ):
        return False

    return True


# ============================================================
# EMAIL VALIDATION
# ============================================================

def validate_email(email):
    """
    Validate an email address.

    Returns:
        True if valid, otherwise False.
    """

    if not email:
        return False

    email = email.strip()

    email_pattern = (
        r"^[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+"
        r"\.[A-Za-z]{2,}$"
    )

    return bool(
        re.fullmatch(
            email_pattern,
            email
        )
    )


# ============================================================
# FIELD VALIDATION
# ============================================================

def validate_field(field):
    """
    Validate the student's field/program.

    Returns:
        True if the field is recognized, otherwise False.
    """

    if not field:
        return False

    field = field.strip().lower()

    return field in VALID_FIELDS


# ============================================================
# VALIDATE ALL STUDENT INFORMATION
# ============================================================

def validate_registration_data(
    name=None,
    email=None,
    field=None
):
    """
    Validate all registration information.

    Returns:
        Dictionary containing validation results.
    """

    result = {
        "name": validate_name(name),
        "email": validate_email(email),
        "field": validate_field(field)
    }

    result["is_valid"] = all(result.values())

    return result


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    print("Registration Validation Tests")
    print("=" * 50)

    # --------------------------------------------------------
    # NAME TESTS
    # --------------------------------------------------------

    print("\nNAME VALIDATION")
    print("-" * 30)

    names = [
        "Siraj",
        "Mohammed Siraj",
        "John Smith",
        "A",
        "John123",
        "",
        None
    ]

    for name in names:

        print(
            f"{name!r} → "
            f"{validate_name(name)}"
        )

    # --------------------------------------------------------
    # EMAIL TESTS
    # --------------------------------------------------------

    print("\nEMAIL VALIDATION")
    print("-" * 30)

    emails = [
        "siraj@gmail.com",
        "student123@gmail.com",
        "john.doe@example.com",
        "siraj@gmail",
        "siraj@",
        "@gmail.com",
        "siraj gmail.com",
        "",
        None
    ]

    for email in emails:

        print(
            f"{email!r} → "
            f"{validate_email(email)}"
        )

    # --------------------------------------------------------
    # FIELD TESTS
    # --------------------------------------------------------

    print("\nFIELD VALIDATION")
    print("-" * 30)

    fields = [
        "computer science",
        "data science",
        "artificial intelligence",
        "machine learning",
        "electronics and communication engineering",
        "unknown field",
        "",
        None
    ]

    for field in fields:

        print(
            f"{field!r} → "
            f"{validate_field(field)}"
        )

    # --------------------------------------------------------
    # COMPLETE REGISTRATION TEST
    # --------------------------------------------------------

    print("\nCOMPLETE REGISTRATION VALIDATION")
    print("-" * 40)

    result = validate_registration_data(
        name="Siraj",
        email="siraj@gmail.com",
        field="computer science"
    )

    print(result)