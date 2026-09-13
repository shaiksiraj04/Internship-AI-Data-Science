from src.nlp.entity_extractor import (
    extract_name,
    extract_email,
    extract_field
)

from src.registration.validator import (
    validate_name,
    validate_email,
    validate_field
)

from src.registration.registration_manager import (
    create_registration,
    add_registration,
    email_exists
)


def process_registration(text):
    """
    Extract, validate, and store registration information
    from a user's message.
    """

    # --------------------------------------------------------
    # STEP 1: Extract entities
    # --------------------------------------------------------

    name = extract_name(text)
    email = extract_email(text)
    field = extract_field(text)

    # --------------------------------------------------------
    # STEP 2: Validate entities
    # --------------------------------------------------------

    validation = {
        "name": validate_name(name),
        "email": validate_email(email),
        "field": validate_field(field)
    }

    # --------------------------------------------------------
    # STEP 3: Check whether all information is valid
    # --------------------------------------------------------

    if not all(validation.values()):

        return {
            "success": False,
            "name": name,
            "email": email,
            "field": field,
            "validation": validation
        }

    # --------------------------------------------------------
    # STEP 4: Check duplicate email
    # --------------------------------------------------------

    if email_exists(email):

        return {
            "success": False,
            "name": name,
            "email": email,
            "field": field,
            "validation": validation,
            "error": "Email is already registered."
        }

    # --------------------------------------------------------
    # STEP 5: Create registration
    # --------------------------------------------------------

    registration = create_registration(
        name=name,
        email=email,
        field=field
    )

    # --------------------------------------------------------
    # STEP 6: Save registration
    # --------------------------------------------------------

    add_registration(registration)

    return {
        "success": True,
        "registration": registration
    }


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    test_message = (
        "I want to register. "
        "My name is Rahul, "
        "my email is rahul@example.com "
        "and I study CSE."
    )

    print("Registration Processing Test")
    print("=" * 50)

    print("\nUser:")
    print(test_message)

    result = process_registration(
        test_message
    )

    print("\nResult:")
    print(result)