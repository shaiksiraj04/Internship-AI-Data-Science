"""
Day 6 - Edge Case Tests

Tests unusual and unexpected user inputs
to make the AI Registration Assistant
more reliable.
"""

from src.chatbot.chatbot import RegistrationChatbot


def test_empty_message():
    chatbot = RegistrationChatbot()

    response = chatbot.respond("")

    assert "message" in response.lower()

    print("✅ Empty message handled")


def test_whitespace_message():
    chatbot = RegistrationChatbot()

    response = chatbot.respond("   ")

    assert response

    print("✅ Whitespace message handled")


def test_random_input():
    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "The weather is beautiful today"
    )

    assert response

    print("✅ Random input handled")


def test_registration_without_name():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")

    response = chatbot.respond(
        "123456789"
    )

    assert chatbot.dialogue_manager.get_step() == "name"
    assert response

    print("✅ Invalid name input handled")


def test_invalid_email():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Edge Test")

    response = chatbot.respond(
        "not-an-email"
    )

    assert chatbot.dialogue_manager.get_step() == "email"
    assert "email" in response.lower()

    print("✅ Invalid email handled")


def test_invalid_field():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Field Test")
    chatbot.respond("field_edge@example.com")

    response = chatbot.respond(
        "Astrology"
    )

    assert chatbot.dialogue_manager.get_step() == "field"
    assert response

    print("✅ Invalid field handled")


def test_confirmation_unknown():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Confirmation Test")
    chatbot.respond("confirmation_edge@example.com")
    chatbot.respond("CSE")

    response = chatbot.respond(
        "maybe"
    )

    assert chatbot.dialogue_manager.get_step() == "confirmation"
    assert "yes" in response.lower()
    assert "no" in response.lower()

    print("✅ Unknown confirmation handled")


def test_confirmation_yes_variations():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Yes Test")
    chatbot.respond("yes_variation@example.com")
    chatbot.respond("CSE")

    response = chatbot.respond(
        "correct"
    )

    assert chatbot.dialogue_manager.get_step() == "completed"
    assert "successfully" in response.lower()

    print("✅ Confirmation variation handled")


def test_confirmation_no():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is No Test")
    chatbot.respond("no_confirmation@example.com")
    chatbot.respond("CSE")

    response = chatbot.respond(
        "no"
    )

    assert chatbot.dialogue_manager.get_step() == "correction"
    assert "correct" in response.lower()

    print("✅ Negative confirmation handled")


def test_correction_name():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Correction Test")
    chatbot.respond("correction_name@example.com")
    chatbot.respond("CSE")
    chatbot.respond("no")

    response = chatbot.respond("name")

    assert chatbot.dialogue_manager.get_step() == "name"
    assert "name" in response.lower()

    print("✅ Name correction handled")


def test_correction_email():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Correction Email")
    chatbot.respond("correction_email@example.com")
    chatbot.respond("CSE")
    chatbot.respond("no")

    response = chatbot.respond("email")

    assert chatbot.dialogue_manager.get_step() == "email"
    assert "email" in response.lower()

    print("✅ Email correction handled")


def test_correction_field():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Correction Field")
    chatbot.respond("correction_field@example.com")
    chatbot.respond("CSE")
    chatbot.respond("no")

    response = chatbot.respond("field")

    assert chatbot.dialogue_manager.get_step() == "field"
    assert "field" in response.lower()

    print("✅ Field correction handled")


def test_reset_during_registration():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Reset Test")

    chatbot.reset()

    assert chatbot.dialogue_manager.get_step() == "idle"

    print("✅ Registration reset handled")


def run_all_tests():
    """Run all edge-case tests."""

    print("=" * 60)
    print("           DAY 6 - EDGE CASE TESTS")
    print("=" * 60)
    print()

    test_empty_message()
    test_whitespace_message()
    test_random_input()
    test_registration_without_name()
    test_invalid_email()
    test_invalid_field()
    test_confirmation_unknown()
    test_confirmation_yes_variations()
    test_confirmation_no()
    test_correction_name()
    test_correction_email()
    test_correction_field()
    test_reset_during_registration()

    print()
    print("=" * 60)
    print("🎉 ALL DAY 6 EDGE CASE TESTS PASSED!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()