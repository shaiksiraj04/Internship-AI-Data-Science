"""
Registration processor.

This module handles the complete registration-data processing workflow:
1. Extract entities from user input
2. Validate extracted information
3. Check for duplicate email
4. Prepare registration data
"""


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
    email_exists
)


def process_registration_data(text):
    """
    Extract and validate registration information from text.

    Args:
        text (str): User input

    Returns:
        dict: Processing result
    """

    if not text or not text.strip():
        return {
            "success": False,
            "message": "Please provide your registration information."
        }

    # -------------------------------------------------
    # Extract entities
    # -------------------------------------------------

    name = extract_name(text)
    email = extract_email(text)
    field = extract_field(text)

    # -------------------------------------------------
    # Validate name
    # -------------------------------------------------

    if name is not None:

        if not validate_name(name):
            return {
                "success": False,
                "field": "name",
                "message": (
                    "The name you provided is not valid. "
                    "Please enter your name using letters only."
                )
            }

    # -------------------------------------------------
    # Validate email
    # -------------------------------------------------

    if email is not None:

        if not validate_email(email):
            return {
                "success": False,
                "field": "email",
                "message": (
                    "The email address is not valid. "
                    "Please enter a valid email address."
                )
            }

        # Check duplicate email
        if email_exists(email):
            return {
                "success": False,
                "field": "email",
                "duplicate": True,
                "message": (
                    "This email address is already registered. "
                    "Please use a different email address."
                )
            }

    # -------------------------------------------------
    # Validate field
    # -------------------------------------------------

    if field is not None:

        if not validate_field(field):
            return {
                "success": False,
                "field": "field",
                "message": (
                    "The field of study is not supported. "
                    "Please provide a valid field such as "
                    "Computer Science, Data Science, "
                    "Artificial Intelligence, or ECE."
                )
            }

    # -------------------------------------------------
    # Prepare result
    # -------------------------------------------------

    registration_data = {
        "name": name,
        "email": email,
        "field": field
    }

    return {
        "success": True,
        "data": registration_data,
        "message": "Registration information processed successfully."
    }


def complete_registration(name, email, field):
    """
    Validate and prepare a complete registration.

    Args:
        name (str): Student name
        email (str): Student email
        field (str): Field of study

    Returns:
        dict: Registration result
    """

    # Validate all fields

    if not validate_name(name):
        return {
            "success": False,
            "field": "name",
            "message": "Invalid name."
        }

    if not validate_email(email):
        return {
            "success": False,
            "field": "email",
            "message": "Invalid email address."
        }

    if not validate_field(field):
        return {
            "success": False,
            "field": "field",
            "message": "Invalid field of study."
        }

    # Check duplicate email

    if email_exists(email):
        return {
            "success": False,
            "field": "email",
            "duplicate": True,
            "message": "This email address is already registered."
        }

    # Create registration object

    registration = create_registration(
        name,
        email,
        field
    )

    return {
        "success": True,
        "data": registration,
        "message": "Registration created successfully."
    }


if __name__ == "__main__":

    print("Testing Registration Processor...\n")

    # Test complete registration
    result = complete_registration(
        "Test Student",
        "test_day5@example.com",
        "computer science"
    )

    print("Complete registration test:")
    print(result)

    print("\nRegistration processor test completed.")