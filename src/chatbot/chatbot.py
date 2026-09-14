"""
Main chatbot for the AI Registration Assistant.

This module connects:
- Intent recognition
- Dialogue management
- Registration workflow
"""

from src.chatbot.intent_classifier import detect_intent
from src.chatbot.dialog_manager import DialogueManager


class RegistrationChatbot:
    """Main chatbot class."""

    def __init__(self):
        """Initialize the chatbot."""

        self.dialogue_manager = DialogueManager()

    # -------------------------------------------------
    # Intent responses
    # -------------------------------------------------

    def greeting_response(self):
        """Return a greeting response."""

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

    # -------------------------------------------------
    # Main response function
    # -------------------------------------------------

    def respond(self, text):
        """
        Generate a chatbot response.

        Args:
            text (str): User message

        Returns:
            str: Chatbot response
        """

        if not text or not text.strip():

            return (
                "I didn't receive any message. "
                "Please type something."
            )

        current_step = self.dialogue_manager.get_step()

        # -------------------------------------------------
        # Registration is already in progress
        # -------------------------------------------------

        if current_step != "idle":

            return self.dialogue_manager.process_message(text)

        # -------------------------------------------------
        # Detect intent
        # -------------------------------------------------

        intent = detect_intent(text)

        # -------------------------------------------------
        # Greeting
        # -------------------------------------------------

        if intent == "greeting":

            return self.greeting_response()

        # -------------------------------------------------
        # Help
        # -------------------------------------------------

        if intent == "help":

            return self.help_response()

        # -------------------------------------------------
        # Registration
        # -------------------------------------------------

        if intent == "register":

            self.dialogue_manager.set_step("name")

            return (
                "Sure! I can help you with internship registration.\n"
                "What is your name?"
            )

        # -------------------------------------------------
        # Thank you
        # -------------------------------------------------

        if intent == "thank_you":

            return (
                "You're welcome! "
                "I'm happy to help."
            )

        # -------------------------------------------------
        # Unknown input
        # -------------------------------------------------

        return (
            "Sorry, I didn't understand that.\n"
            "You can say something like "
            "'I want to register' or 'Help'."
        )

    # -------------------------------------------------
    # Reset chatbot
    # -------------------------------------------------

    def reset(self):
        """Start a fresh conversation."""

        self.dialogue_manager.reset()


def run_chatbot():
    """Run the chatbot in the terminal."""

    chatbot = RegistrationChatbot()

    print("=" * 60)
    print("       AI REGISTRATION ASSISTANT")
    print("=" * 60)

    print("\nBot: Hello! Welcome to the AI Registration Assistant.")
    print("Bot: Type 'exit' or 'quit' to end the conversation.\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() in {
            "exit",
            "quit",
            "bye"
        }:

            print(
                "Bot: Goodbye! Have a great day. 👋"
            )

            break

        response = chatbot.respond(user_input)

        print("Bot:", response)


if __name__ == "__main__":
    run_chatbot()