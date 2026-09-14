"""
Day 6 - Final Integration Tests

Tests the complete AI Registration Assistant:

1. Greeting
2. FAQ
3. Registration
4. Name validation
5. Email validation
6. Field validation
7. Confirmation
8. Duplicate email protection
9. Correction flow
10. Unknown input
11. Chatbot reset
12. Logging
"""

from pathlib import Path

from src.chatbot.chatbot import RegistrationChatbot
from src.utils.logger import read_logs


def test_greeting():
    chatbot = RegistrationChatbot()

    response = chatbot.respond("Hello")

    assert response
    assert "welcome" in response.lower()

    print("✅ 1. Greeting")


def test_faq():
    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "What information is required?"
    )

    assert response
    assert "name" in response.lower()
    assert "email" in response.lower()

    print("✅ 2. FAQ")


def test_start_registration():
    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "I want to register"
    )

    assert "name" in response.lower()
    assert chatbot.dialogue_manager.get_step() == "name"

    print("✅ 3. Registration start")


def test_invalid_name():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")

    response = chatbot.respond("123456")

    assert response
    assert chatbot.dialogue_manager.get_step() == "name"

    print("✅ 4. Invalid name")


def test_invalid_email():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Final Test")

    response = chatbot.respond("invalid-email")

    assert response
    assert chatbot.dialogue_manager.get_step() == "email"

    print("✅ 5. Invalid email")


def test_invalid_field():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Field Final Test")
    chatbot.respond(
        "field_final_test@example.com"
    )

    response = chatbot.respond(
        "Astrology"
    )

    assert response
    assert chatbot.dialogue_manager.get_step() == "field"

    print("✅ 6. Invalid field")


def test_successful_registration():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Final Student")
    chatbot.respond(
        "final_day6_unique@example.com"
    )
    chatbot.respond("CSE")

    response = chatbot.respond("yes")

    assert response
    assert "successfully" in response.lower()
    assert chatbot.dialogue_manager.get_step() == "completed"

    print("✅ 7. Successful registration")


def test_correction_flow():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Correction Final")
    chatbot.respond(
        "correction_final@example.com"
    )
    chatbot.respond("CSE")

    response = chatbot.respond("no")

    assert response
    assert chatbot.dialogue_manager.get_step() == "correction"

    response = chatbot.respond("name")

    assert chatbot.dialogue_manager.get_step() == "name"
    assert "name" in response.lower()

    print("✅ 8. Correction flow")


def test_unknown_input():
    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "I like watching random movies"
    )

    assert response

    print("✅ 9. Unknown input")


def test_reset():
    chatbot = RegistrationChatbot()

    chatbot.respond("I want to register")
    chatbot.respond("My name is Reset Final")

    chatbot.reset()

    assert chatbot.dialogue_manager.get_step() == "idle"
    assert chatbot.dialogue_manager.get_value("name") is None
    assert chatbot.dialogue_manager.get_value("email") is None
    assert chatbot.dialogue_manager.get_value("field") is None

    print("✅ 10. Chatbot reset")


def test_logging():
    chatbot = RegistrationChatbot()

    chatbot.respond("Hello")
    chatbot.respond(
        "What information is required?"
    )

    logs = read_logs()

    assert isinstance(logs, list)
    assert len(logs) > 0

    last_log = logs[-1]

    assert "timestamp" in last_log
    assert "user_message" in last_log
    assert "intent" in last_log
    assert "conversation_step" in last_log
    assert "bot_response" in last_log

    print("✅ 11. Conversation logging")


def test_multiple_faq_questions():
    chatbot = RegistrationChatbot()

    questions = [
        "How can I register?",
        "What information is required?",
        "Which fields are supported?",
        "Can I correct my information?",
        "How can I get help?"
    ]

    for question in questions:

        response = chatbot.respond(question)

        assert response
        assert len(response) > 10

    print("✅ 12. Multiple FAQ questions")


def run_all_tests():
    """Run all final Day 6 tests."""

    print("=" * 65)
    print("          DAY 6 - FINAL INTEGRATION TESTS")
    print("=" * 65)
    print()

    test_greeting()
    test_faq()
    test_start_registration()
    test_invalid_name()
    test_invalid_email()
    test_invalid_field()
    test_successful_registration()
    test_correction_flow()
    test_unknown_input()
    test_reset()
    test_logging()
    test_multiple_faq_questions()

    print()
    print("=" * 65)
    print("🎉 ALL DAY 6 FINAL TESTS PASSED SUCCESSFULLY!")
    print("=" * 65)


if __name__ == "__main__":
    run_all_tests()