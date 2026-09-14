"""
Main chatbot for the AI Registration Assistant.

This module connects:
- ML intent recognition
- Confidence-based unknown detection
- FAQ system
- Dialogue management
- Registration workflow
"""

from src.ml.predict import predict_intent
from src.chatbot.dialog_manager import DialogueManager
from src.chatbot.faq import find_faq


class RegistrationChatbot:
    """Main AI Registration Chatbot."""

    def __init__(self):
        """Initialize a new chatbot."""

        self.dialogue_manager = DialogueManager()

    # -------------------------------------------------
    # Basic responses
    # -------------------------------------------------

    def greeting_response(self):
        """Return greeting response."""

        return (
            "Hello! Welcome to the AI Registration Assistant. "
            "How can I help you today?"
        )

    def help_response(self):
        """Return help information."""

        return (
            "I can help you register for the internship. "
            "I can collect your name, email, and field of study "
            "and complete your registration."
        )

    def unknown_response(self):
        """Return fallback response for unknown input."""

        return (
            "Sorry, I didn't understand that.\n"
            "You can ask me about the internship, "
            "ask for help, or say 'I want to register'."
        )

    # -------------------------------------------------
    # ML Intent Processing
    # -------------------------------------------------

    def process_intent(self, text):
        """
        Process a user message using the ML intent classifier.

        Args:
            text (str): User message

        Returns:
            str: Chatbot response
        """

        intent, confidence = predict_intent(text)

        # -------------------------------------------------
        # Greeting intent
        # -------------------------------------------------

        if intent == "greeting":

            return self.greeting_response()

        # -------------------------------------------------
        # Registration intent
        # -------------------------------------------------

        if intent == "register":

            self.dialogue_manager.set_step("name")

            return (
                "Sure! I can help you with internship registration.\n"
                "What is your name?"
            )

        # -------------------------------------------------
        # Help intent
        # -------------------------------------------------

        if intent == "help":

            return self.help_response()

        # -------------------------------------------------
        # Thank-you intent
        # -------------------------------------------------

        if intent == "thank_you":

            return (
                "You're welcome! "
                "I'm happy to help."
            )

        # -------------------------------------------------
        # Unknown intent
        # -------------------------------------------------

        return self.unknown_response()

    # -------------------------------------------------
    # Main Response Function
    # -------------------------------------------------

    def respond(self, text):
        """
        Generate a response to a user message.

        Registration messages are handled by the
        DialogueManager.

        Other messages are checked against the FAQ
        system and then the ML intent classifier.

        Args:
            text (str): User message

        Returns:
            str: Chatbot response
        """

        # -------------------------------------------------
        # Empty input
        # -------------------------------------------------

        if not text or not text.strip():

            return (
                "I didn't receive any message. "
                "Please type something."
            )

        # -------------------------------------------------
        # Get current conversation state
        # -------------------------------------------------

        current_step = self.dialogue_manager.get_step()

        # -------------------------------------------------
        # Registration conversation
        # -------------------------------------------------
        #
        # If registration is already in progress,
        # DialogueManager gets priority.
        #

        if current_step != "idle":

            return self.dialogue_manager.process_message(text)

        # -------------------------------------------------
        # FAQ handling
        # -------------------------------------------------
        #
        # Check the FAQ database before using
        # the ML intent classifier.
        #

        faq_answer = find_faq(text)

        if faq_answer:

            return faq_answer

        # -------------------------------------------------
        # ML intent recognition
        # -------------------------------------------------

        return self.process_intent(text)

    # -------------------------------------------------
    # Reset
    # -------------------------------------------------

    def reset(self):
        """Reset the chatbot conversation."""

        self.dialogue_manager.reset()


# =====================================================
# Terminal Chatbot
# =====================================================

def run_chatbot():
    """Run the chatbot in the terminal."""

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