import json
import os


# ============================================================
# FILE PATH
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

REGISTRATION_FILE = os.path.join(
    DATA_DIR,
    "registrations.json"
)


# ============================================================
# INITIALIZE REGISTRATION FILE
# ============================================================

def initialize_storage():
    """
    Create the registrations.json file if it doesn't exist.
    """

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(REGISTRATION_FILE):

        with open(
            REGISTRATION_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )


# ============================================================
# LOAD REGISTRATIONS
# ============================================================

def load_registrations():
    """
    Load all registrations from registrations.json.

    Returns:
        List of registrations.
    """

    initialize_storage()

    with open(
        REGISTRATION_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ============================================================
# SAVE REGISTRATIONS
# ============================================================

def save_registrations(registrations):
    """
    Save registrations to registrations.json.
    """

    initialize_storage()

    with open(
        REGISTRATION_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            registrations,
            file,
            indent=4
        )


# ============================================================
# CREATE REGISTRATION
# ============================================================

def create_registration(
    name,
    email,
    field
):
    """
    Create a registration dictionary.

    Returns:
        Registration dictionary.
    """

    registration = {
        "name": name,
        "email": email,
        "field": field
    }

    return registration


# ============================================================
# ADD REGISTRATION
# ============================================================

def add_registration(registration):
    """
    Add a registration to the JSON storage.

    Returns:
        True after successful storage.
    """

    registrations = load_registrations()

    registrations.append(registration)

    save_registrations(registrations)

    return True


# ============================================================
# CHECK EXISTING EMAIL
# ============================================================

def email_exists(email):
    """
    Check whether an email is already registered.

    Returns:
        True if email already exists.
        False otherwise.
    """

    registrations = load_registrations()

    for registration in registrations:

        if registration["email"].lower() == email.lower():
            return True

    return False


# ============================================================
# GET REGISTRATION COUNT
# ============================================================

def get_registration_count():
    """
    Return the total number of registrations.
    """

    registrations = load_registrations()

    return len(registrations)


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    print("Registration Storage Tests")
    print("=" * 50)

    # Create a sample registration
    registration = create_registration(
        name="Siraj",
        email="siraj@example.com",
        field="computer science"
    )

    print("\nCreated Registration:")
    print(registration)

    # Check whether email already exists
    print("\nEmail Already Registered?")
    print(email_exists("siraj@example.com"))

    # Add registration only if email doesn't exist
    if not email_exists("siraj@example.com"):

        add_registration(registration)

        print("\nRegistration saved successfully.")

    else:

        print("\nRegistration already exists.")

    # Display total registrations
    print("\nTotal Registrations:")
    print(get_registration_count())

    # Display all registrations
    print("\nAll Registrations:")
    print(load_registrations())