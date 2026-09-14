"""
Main chatbot for the AI Registration Assistant.

Features:
- Rule-based handling for very clear commands
- ML intent recognition
- Confidence-based unknown detection
- FAQ system
- Dialogue management
- Registration workflow
- Conversation logging
"""

from src.ml.predict import predict_intent
from src.chatbot.dialog_manager import DialogueManager
from src.chatbot.faq import find_faq
from src.utils.logger import log_conversation


class RegistrationChatbot:
    """Main AI Registration Chatbot."""

    def __init__(self):
        """Initialize chatbot."""

        self.dialogue_manager = DialogueManager()

    # =================================================
    # Basic Responses
    # =================================================

    def greeting_response(self):
        """Return greeting response."""

        return (
            "Hello! Welcome to the AI Registration Assistant. "
            "How can I help you today?"
        )

    def help_response(self):
        """Return help response."""

        return (
            "I can help you register for the internship. "
            "I can collect your name, email, and field of study "
            "and complete your registration."
        )

    def unknown_response(self):
        """Return fallback response."""

        return (
            "Sorry, I didn't understand that.\n"
            "You can ask me about the internship, "
            "ask for help, or say 'I want to register'."
        )

    # =================================================
    # Clear Intent Detection
    # =================================================

    def detect_clear_intent(self, text):
        """
        Detect very clear user intents.

        This protects important chatbot commands from
        errors caused by a small ML training dataset.

        Returns:
            str or None
        """

        if not text:
            return None

        message = text.strip().lower()

        # ---------------------------------------------
        # Greeting
        # ---------------------------------------------

        greeting_words = {
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening",
            "greetings"
        }

        if message in greeting_words:
            return "greeting"

        # ---------------------------------------------
        # Registration
        # ---------------------------------------------

        registration_phrases = {
            "i want to register",
            "i want registration",
            "i want to apply",
            "i want to enroll",
            "i want to join",
            "register me",
            "help me register",
            "i would like to register",
            "i would like to apply",
            "sign me up"
        }

        if message in registration_phrases:
            return "register"

        return None

    # =================================================
    # Intent Processing
    # =================================================

    def process_intent(self, text):
        """
        Process user message using the ML classifier.

        Returns:
            tuple: (response, intent)
        """

        intent, confidence = predict_intent(text)

        # ---------------------------------------------
        # Greeting
        # ---------------------------------------------

        if intent == "greeting":

            return (
                self.greeting_response(),
                "greeting"
            )

        # ---------------------------------------------
        # Registration
        # ---------------------------------------------

        if intent == "register":

            self.dialogue_manager.set_step("name")

            return (
                "Sure! I can help you with internship registration.\n"
                "What is your name?",
                "register"
            )

        # ---------------------------------------------
        # Help
        # ---------------------------------------------

        if intent == "help":

            return (
                self.help_response(),
                "help"
            )

        # ---------------------------------------------
        # Thank you
        # ---------------------------------------------

        if intent == "thank_you":

            return (
                "You're welcome! I'm happy to help.",
                "thank_you"
            )

        # ---------------------------------------------
        # Unknown
        # ---------------------------------------------

        return (
            self.unknown_response(),
            "unknown"
        )

    # =================================================
    # Main Response Function
    # =================================================

    def respond(self, text):
        """
        Generate a chatbot response.

        Priority:

        1. Empty input
        2. Registration conversation
        3. Clear greeting/registration commands
        4. FAQ
        5. ML intent classification
        6. Unknown fallback
        """

        # -------------------------------------------------
        # Empty input
        # -------------------------------------------------

        if not text or not text.strip():

            response = (
                "I didn't receive any message. "
                "Please type something."
            )

            log_conversation(
                user_message=text,
                bot_response=response,
                intent="unknown",
                conversation_step=(
                    self.dialogue_manager.get_step()
                )
            )

            return response

        # -------------------------------------------------
        # Current conversation state
        # -------------------------------------------------

        current_step = self.dialogue_manager.get_step()

        # -------------------------------------------------
        # Registration in progress
        # -------------------------------------------------

        if current_step != "idle":

            response = self.dialogue_manager.process_message(
                text
            )

            log_conversation(
                user_message=text,
                bot_response=response,
                intent="registration",
                conversation_step=current_step
            )

            return response

        # -------------------------------------------------
        # Clear intent handling
        # -------------------------------------------------

        clear_intent = self.detect_clear_intent(text)

        # ---------------------------------------------
        # Clear greeting
        # ---------------------------------------------

        if clear_intent == "greeting":

            response = self.greeting_response()

            log_conversation(
                user_message=text,
                bot_response=response,
                intent="greeting",
                conversation_step="idle"
            )

            return response

        # ---------------------------------------------
        # Clear registration request
        # ---------------------------------------------

        if clear_intent == "register":

            self.dialogue_manager.set_step("name")

            response = (
                "Sure! I can help you with internship registration.\n"
                "What is your name?"
            )

            log_conversation(
                user_message=text,
                bot_response=response,
                intent="register",
                conversation_step="name"
            )

            return response

        # -------------------------------------------------
        # FAQ
        # -------------------------------------------------

        faq_answer = find_faq(text)

        if faq_answer:

            log_conversation(
                user_message=text,
                bot_response=faq_answer,
                intent="faq",
                conversation_step="idle"
            )

            return faq_answer

        # -------------------------------------------------
        # ML intent recognition
        # -------------------------------------------------

        response, intent = self.process_intent(text)

        log_conversation(
            user_message=text,
            bot_response=response,
            intent=intent,
            conversation_step=(
                self.dialogue_manager.get_step()
            )
        )

        return response

    # =================================================
    # Reset
    # =================================================

    def reset(self):
        """Reset chatbot conversation."""

        self.dialogue_manager.reset()


# =====================================================
# Terminal Chatbot
# =====================================================

def run_chatbot():
    """Run chatbot in terminal."""

    chatbot = RegistrationChatbot()

    print("=" * 60)
    print("          AI REGISTRATION ASSISTANT")
    print("=" * 60)

    print(
        "\nBot: Hello! Welcome to the AI Registration Assistant."
    )

    print(
        "Bot: I can help with internship registration and FAQs."
    )

    print(
        "Bot: Type 'exit', 'quit', or 'bye' to end.\n"
    )

    while True:

        try:

            user_input = input("You: ").strip()

        except (KeyboardInterrupt, EOFError):

            print(
                "\nBot: Goodbye! Have a great day. 👋"
            )

            break

        # -------------------------------------------------
        # Exit commands
        # -------------------------------------------------

        if user_input.lower() in {
            "exit",
            "quit",
            "bye"
        }:

            print(
                "Bot: Goodbye! Have a great day. 👋"
            )

            break

        # -------------------------------------------------
        # Generate response
        # -------------------------------------------------

        response = chatbot.respond(user_input)

        print("Bot:", response)


# =====================================================
# Program Entry Point
# =====================================================

if __name__ == "__main__":

    run_chatbot()