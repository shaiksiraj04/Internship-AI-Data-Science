"""
Day 5 - Comprehensive Registration Tests

Tests:
1. Start registration
2. Collect name
3. Collect email
4. Collect field
5. Confirmation
6. Successful registration
7. Invalid email
8. Invalid field
9. Duplicate email
10. Correction flow
11. JSON persistence
12. Reset conversation
"""

import json
from pathlib import Path

from src.chatbot.chatbot import RegistrationChatbot
from src.registration.registration_manager import load_registrations


def test_start_registration():
    chatbot = RegistrationChatbot()

    response = chatbot.respond("I want to register")

    assert "What is your name?" in response
    assert chatbot.dialogue_manager.get_step() == "name"

    print("✅ Test 1: Start registration")


def test_name_collection():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    response = chatbot.respond("My name is Test Student")

    assert chatbot.dialogue_manager.get_value("name") == "Test Student"
    assert chatbot.dialogue_manager.get_step() == "email"
    assert "email" in response.lower()

    print("✅ Test 2: Name collection")


def test_email_collection():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Test Student")

    response = chatbot.respond("unique_email_day5@example.com")

    assert (
        chatbot.dialogue_manager.get_value("email")
        == "unique_email_day5@example.com"
    )

    assert chatbot.dialogue_manager.get_step() == "field"
    assert "field" in response.lower()

    print("✅ Test 3: Email collection")


def test_field_collection():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Test Student")
    chatbot.respond("field_test_day5@example.com")

    response = chatbot.respond("CSE")

    assert (
        chatbot.dialogue_manager.get_value("field")
        == "computer science"
    )

    assert chatbot.dialogue_manager.get_step() == "confirmation"
    assert "correct" in response.lower()

    print("✅ Test 4: Field collection")


def test_successful_registration():
    chatbot = RegistrationChatbot()

    import uuid

    unique_email = (
        f"successful_{uuid.uuid4().hex[:8]}@example.com"
    )

    chatbot.respond("I want to register")
    chatbot.respond("My name is Successful Student")
    chatbot.respond(unique_email)
    chatbot.respond("CSE")

    response = chatbot.respond("yes")

    assert "successfully completed" in response.lower()
    assert chatbot.dialogue_manager.get_step() == "completed"

    print("✅ Test 5: Successful registration")


def test_invalid_email():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Email Student")

    response = chatbot.respond("invalid-email")

    assert "valid email" in response.lower()
    assert chatbot.dialogue_manager.get_step() == "email"

    print("✅ Test 6: Invalid email handling")


def test_invalid_field():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Field Student")
    chatbot.respond("field_student@example.com")

    response = chatbot.respond("Rocket Science")

    assert chatbot.dialogue_manager.get_step() == "field"
    assert (
        "field" in response.lower()
        or "supported" in response.lower()
    )

    print("✅ Test 7: Invalid field handling")


def test_duplicate_email():
    chatbot = RegistrationChatbot()

    import uuid

    # Generate a unique email for this test run
    unique_email = (
        f"duplicate_{uuid.uuid4().hex[:8]}@example.com"
    )

    # -------------------------------------------------
    # First registration
    # -------------------------------------------------

    chatbot.respond("I want to register")

    chatbot.respond(
        "My name is First Student"
    )

    chatbot.respond(
        unique_email
    )

    chatbot.respond("CSE")

    first_response = chatbot.respond("yes")

    assert "successfully completed" in first_response.lower()

    # -------------------------------------------------
    # Start a new registration
    # -------------------------------------------------

    chatbot.reset()

    chatbot.respond(
        "I want to register"
    )

    chatbot.respond(
        "My name is Second Student"
    )

    # -------------------------------------------------
    # Try the same email
    # -------------------------------------------------

    second_response = chatbot.respond(
        unique_email
    )

    assert "already registered" in second_response.lower()

    assert (
        chatbot.dialogue_manager.get_step()
        == "email"
    )

    print("✅ Test 8: Duplicate email protection")


def test_correction_flow():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Correction Student")
    chatbot.respond("correction_day5@example.com")
    chatbot.respond("CSE")

    response = chatbot.respond("no")

    assert chatbot.dialogue_manager.get_step() == "correction"
    assert "name" in response.lower()
    assert "email" in response.lower()
    assert "field" in response.lower()

    print("✅ Test 9: Correction flow")


def test_json_persistence():
    registrations = load_registrations()

    assert isinstance(registrations, list)

    print("✅ Test 10: JSON persistence")


def test_chatbot_reset():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Reset Student")

    chatbot.reset()

    assert chatbot.dialogue_manager.get_step() == "idle"
    assert chatbot.dialogue_manager.get_value("name") is None
    assert chatbot.dialogue_manager.get_value("email") is None
    assert chatbot.dialogue_manager.get_value("field") is None

    print("✅ Test 11: Conversation reset")


def test_greeting():
    chatbot = RegistrationChatbot()

    response = chatbot.respond("Hello")

    assert "welcome" in response.lower()

    print("✅ Test 12: Greeting")


def test_help():
    chatbot = RegistrationChatbot()

    response = chatbot.respond("Help me")

    assert "register" in response.lower()

    print("✅ Test 13: Help")


def run_all_tests():
    """Run every Day 5 test."""

    print("=" * 60)
    print("       DAY 5 REGISTRATION TESTS")
    print("=" * 60)
    print()

    test_start_registration()
    test_name_collection()
    test_email_collection()
    test_field_collection()
    test_successful_registration()
    test_invalid_email()
    test_invalid_field()
    test_duplicate_email()
    test_correction_flow()
    test_json_persistence()
    test_chatbot_reset()
    test_greeting()
    test_help()

    print()
    print("=" * 60)
    print("🎉 ALL DAY 5 TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()