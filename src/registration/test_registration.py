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
    load_registrations,
    get_registration_count
)

from src.registration.registration_processor import (
    process_registration
)


# ============================================================
# TEST ENTITY EXTRACTION
# ============================================================

def test_entity_extraction():

    print("\n" + "=" * 60)
    print("TEST 1: ENTITY EXTRACTION")
    print("=" * 60)

    message = (
        "My name is Arjun, "
        "my email is arjun@example.com "
        "and I study CSE."
    )

    name = extract_name(message)
    email = extract_email(message)
    field = extract_field(message)

    print("\nUser:")
    print(message)

    print("\nExtracted Information:")
    print(f"Name  : {name}")
    print(f"Email : {email}")
    print(f"Field : {field}")

    assert name == "Arjun"
    assert email == "arjun@example.com"
    assert field == "computer science"

    print("\nResult: PASSED ✅")


# ============================================================
# TEST VALIDATION
# ============================================================

def test_validation():

    print("\n" + "=" * 60)
    print("TEST 2: VALIDATION")
    print("=" * 60)

    # Valid information
    assert validate_name("Arjun") is True
    assert validate_email("arjun@example.com") is True
    assert validate_field("computer science") is True

    print("\nValid information:")
    print("Name  → Arjun ✅")
    print("Email → arjun@example.com ✅")
    print("Field → computer science ✅")

    # Invalid information
    assert validate_name("Arjun123") is False
    assert validate_email("arjun@example") is False
    assert validate_field("unknown field") is False

    print("\nInvalid information:")
    print("Name  → Arjun123 ❌")
    print("Email → arjun@example ❌")
    print("Field → unknown field ❌")

    print("\nResult: PASSED ✅")


# ============================================================
# TEST COMPLETE REGISTRATION
# ============================================================

def test_complete_registration():

    print("\n" + "=" * 60)
    print("TEST 3: COMPLETE REGISTRATION")
    print("=" * 60)

    message = (
        "I want to register. "
        "My name is Test Student, "
        "my email is test_student_001@example.com "
        "and I study CSE."
    )

    print("\nUser:")
    print(message)

    result = process_registration(message)

    print("\nProcessor Result:")
    print(result)

    assert result["success"] is True

    registration = result["registration"]

    assert registration["name"] == "Test Student"
    assert registration["email"] == "test_student_001@example.com"
    assert registration["field"] == "computer science"

    print("\nRegistration:")
    print(f"Name  : {registration['name']}")
    print(f"Email : {registration['email']}")
    print(f"Field : {registration['field']}")

    print("\nResult: PASSED ✅")


# ============================================================
# TEST MISSING INFORMATION
# ============================================================

def test_missing_information():

    print("\n" + "=" * 60)
    print("TEST 4: MISSING INFORMATION")
    print("=" * 60)

    message = "My name is Missing Student"

    print("\nUser:")
    print(message)

    result = process_registration(message)

    print("\nProcessor Result:")
    print(result)

    assert result["success"] is False
    assert result["name"] == "Missing Student"
    assert result["email"] is None
    assert result["field"] is None

    print("\nMissing:")
    print("Email → ❌")
    print("Field → ❌")

    print("\nResult: PASSED ✅")


# ============================================================
# TEST INVALID EMAIL
# ============================================================

def test_invalid_email():

    print("\n" + "=" * 60)
    print("TEST 5: INVALID EMAIL")
    print("=" * 60)

    message = (
        "My name is Invalid Student "
        "and my email is invalid@email"
    )

    print("\nUser:")
    print(message)

    result = process_registration(message)

    print("\nProcessor Result:")
    print(result)

    assert result["success"] is False

    print("\nInvalid email detected: ❌")

    print("\nResult: PASSED ✅")


# ============================================================
# TEST UNKNOWN FIELD
# ============================================================

def test_unknown_field():

    print("\n" + "=" * 60)
    print("TEST 6: UNKNOWN FIELD")
    print("=" * 60)

    message = (
        "My name is Field Student "
        "my email is field@example.com "
        "and I study rocket science."
    )

    print("\nUser:")
    print(message)

    result = process_registration(message)

    print("\nProcessor Result:")
    print(result)

    assert result["success"] is False
    assert result["field"] is None

    print("\nUnsupported field detected: ❌")

    print("\nResult: PASSED ✅")


# ============================================================
# RUN ALL TESTS
# ============================================================

if __name__ == "__main__":

    print("\n")
    print("*" * 60)
    print("AI REGISTRATION ASSISTANT")
    print("DAY 3 - COMPLETE TESTING")
    print("*" * 60)

    test_entity_extraction()

    test_validation()

    test_complete_registration()

    test_missing_information()

    test_invalid_email()

    test_unknown_field()

    print("\n" + "*" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY ✅")
    print("*" * 60)

    print("\nCurrent Registration Count:")
    print(get_registration_count())

    print("\nStored Registrations:")
    print(load_registrations())