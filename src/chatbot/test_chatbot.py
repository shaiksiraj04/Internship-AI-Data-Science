# ============================================================
# AI REGISTRATION ASSISTANT
# DAY 4 - COMPLETE CHATBOT TESTING
# ============================================================

from src.chatbot.chatbot import RegistrationChatbot


# ============================================================
# TEST 1: START REGISTRATION
# ============================================================

def test_start_registration():

    print("\n" + "=" * 60)
    print("TEST 1: START REGISTRATION")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "I want to register"
    )

    print("\nUser: I want to register")
    print(f"Bot: {response}")

    assert (
        "What is your name?"
        in response
    )

    assert (
        chatbot.dialogue_manager.get_current_step()
        == "name"
    )

    print("\nResult: PASSED ✅")


# ============================================================
# TEST 2: NAME COLLECTION
# ============================================================

def test_name_collection():

    print("\n" + "=" * 60)
    print("TEST 2: NAME COLLECTION")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    response = chatbot.respond(
        "My name is Test User"
    )

    print("\nUser: My name is Test User")
    print(f"Bot: {response}")

    assert (
        chatbot.dialogue_manager
        .get_value("name")
        == "Test User"
    )

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "email"
    )

    print("\nStored Name: Test User")
    print("Result: PASSED ✅")


# ============================================================
# TEST 3: EMAIL COLLECTION
# ============================================================

def test_email_collection():

    print("\n" + "=" * 60)
    print("TEST 3: EMAIL COLLECTION")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    chatbot.respond(
        "My name is Email Tester"
    )

    response = chatbot.respond(
        "emailtester_day4@example.com"
    )

    print(
        "\nUser: emailtester_day4@example.com"
    )

    print(
        f"Bot: {response}"
    )

    assert (
        chatbot.dialogue_manager
        .get_value("email")
        == "emailtester_day4@example.com"
    )

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "field"
    )

    print(
        "\nStored Email: "
        "emailtester_day4@example.com"
    )

    print("Result: PASSED ✅")


# ============================================================
# TEST 4: FIELD COLLECTION
# ============================================================

def test_field_collection():

    print("\n" + "=" * 60)
    print("TEST 4: FIELD COLLECTION")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    chatbot.respond(
        "My name is Field Tester"
    )

    chatbot.respond(
        "fieldtester_day4@example.com"
    )

    response = chatbot.respond(
        "CSE"
    )

    print("\nUser: CSE")
    print(f"Bot: {response}")

    assert (
        chatbot.dialogue_manager
        .get_value("field")
        == "computer science"
    )

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "confirmation"
    )

    print(
        "\nStored Field: computer science"
    )

    print("Result: PASSED ✅")


# ============================================================
# TEST 5: COMPLETE REGISTRATION
# ============================================================

def test_complete_registration():

    print("\n" + "=" * 60)
    print("TEST 5: COMPLETE REGISTRATION")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    messages = [
        "I want to register",
        "My name is Complete Tester",
        "complete_day4@example.com",
        "CSE",
        "yes"
    ]

    for message in messages:

        response = chatbot.respond(
            message
        )

        print(f"\nUser: {message}")
        print(f"Bot: {response}")

    state = (
        chatbot.dialogue_manager
        .get_state()
    )

    print("\nFinal State:")
    print(state)

    assert (
        state["name"]
        == "Complete Tester"
    )

    assert (
        state["email"]
        == "complete_day4@example.com"
    )

    assert (
        state["field"]
        == "computer science"
    )

    assert (
        state["current_step"]
        == "completed"
    )

    assert (
        chatbot.dialogue_manager
        .is_registration_complete()
        is True
    )

    print("\nRegistration Complete: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# TEST 6: INVALID EMAIL RECOVERY
# ============================================================

def test_invalid_email_recovery():

    print("\n" + "=" * 60)
    print("TEST 6: INVALID EMAIL RECOVERY")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    chatbot.respond(
        "My name is Invalid Email Tester"
    )

    response = chatbot.respond(
        "invalid-email"
    )

    print("\nUser: invalid-email")
    print(f"Bot: {response}")

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "email"
    )

    assert (
        chatbot.dialogue_manager
        .get_value("email")
        is None
    )

    print("\nInvalid email rejected: YES ✅")

    # Try valid email
    response = chatbot.respond(
        "valid_day4@example.com"
    )

    print(
        "\nUser: valid_day4@example.com"
    )

    print(
        f"Bot: {response}"
    )

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "field"
    )

    print("\nValid email accepted: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# TEST 7: INVALID FIELD RECOVERY
# ============================================================

def test_invalid_field_recovery():

    print("\n" + "=" * 60)
    print("TEST 7: INVALID FIELD RECOVERY")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    chatbot.respond(
        "My name is Invalid Field Tester"
    )

    chatbot.respond(
        "invalidfield_day4@example.com"
    )

    response = chatbot.respond(
        "Rocket Science"
    )

    print("\nUser: Rocket Science")
    print(f"Bot: {response}")

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "field"
    )

    assert (
        chatbot.dialogue_manager
        .get_value("field")
        is None
    )

    print("\nInvalid field rejected: YES ✅")

    # Try valid field
    response = chatbot.respond(
        "Data Science"
    )

    print("\nUser: Data Science")
    print(f"Bot: {response}")

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "confirmation"
    )

    print("\nValid field accepted: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# TEST 8: EMPTY MESSAGE
# ============================================================

def test_empty_message():

    print("\n" + "=" * 60)
    print("TEST 8: EMPTY MESSAGE")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        ""
    )

    print("\nUser: [empty]")
    print(f"Bot: {response}")

    assert (
        response
        == "Please enter a message."
    )

    print("\nEmpty input handled: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# TEST 9: HELP
# ============================================================

def test_help():

    print("\n" + "=" * 60)
    print("TEST 9: HELP")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "I need help"
    )

    print("\nUser: I need help")
    print(f"Bot: {response}")

    assert (
        "registration"
        in response.lower()
    )

    print("\nHelp response received: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# TEST 10: GREETING
# ============================================================

def test_greeting():

    print("\n" + "=" * 60)
    print("TEST 10: GREETING")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    response = chatbot.respond(
        "Hello"
    )

    print("\nUser: Hello")
    print(f"Bot: {response}")

    assert (
        "welcome"
        in response.lower()
    )

    print("\nGreeting handled: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# TEST 11: UNKNOWN INPUT
# ============================================================

def test_unknown_input():

    print("\n" + "=" * 60)
    print("TEST 11: UNKNOWN INPUT")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    response = chatbot.respond(
        "I like playing cricket"
    )

    print(
        "\nUser: I like playing cricket"
    )

    print(
        f"Bot: {response}"
    )

    assert (
        chatbot.dialogue_manager
        .get_current_step()
        == "name"
    )

    print(
        "\nUnexpected input handled: YES ✅"
    )

    print("Result: PASSED ✅")


# ============================================================
# TEST 12: CONVERSATION STATE
# ============================================================

def test_conversation_state():

    print("\n" + "=" * 60)
    print("TEST 12: CONVERSATION STATE")
    print("=" * 60)

    chatbot = RegistrationChatbot()

    chatbot.respond(
        "I want to register"
    )

    chatbot.respond(
        "My name is State Tester"
    )

    chatbot.respond(
        "state_day4@example.com"
    )

    state = (
        chatbot.dialogue_manager
        .get_state()
    )

    print("\nCurrent State:")
    print(state)

    assert (
        state["name"]
        == "State Tester"
    )

    assert (
        state["email"]
        == "state_day4@example.com"
    )

    assert (
        state["field"]
        is None
    )

    assert (
        state["current_step"]
        == "field"
    )

    print("\nConversation state preserved: YES ✅")
    print("Result: PASSED ✅")


# ============================================================
# RUN ALL TESTS
# ============================================================

if __name__ == "__main__":

    print("\n")
    print("*" * 60)
    print("AI REGISTRATION ASSISTANT")
    print("DAY 4 - COMPLETE TEST SUITE")
    print("*" * 60)

    test_start_registration()

    test_name_collection()

    test_email_collection()

    test_field_collection()

    test_complete_registration()

    test_invalid_email_recovery()

    test_invalid_field_recovery()

    test_empty_message()

    test_help()

    test_greeting()

    test_unknown_input()

    test_conversation_state()

    print("\n")
    print("*" * 60)
    print("ALL DAY 4 TESTS PASSED SUCCESSFULLY! 🎉")
    print("*" * 60)