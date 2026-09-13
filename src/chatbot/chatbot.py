# ============================================================
# AI REGISTRATION ASSISTANT
# ============================================================

from src.chatbot.dialog_manager import DialogueManager
from src.chatbot.intent_classifier import detect_intent


class RegistrationChatbot:
    """
    Main AI Registration Assistant.

    Connects:

        Intent Detection
        Dialogue Management
        Entity Extraction
        Validation
        Registration Storage
    """

    def __init__(self):

        self.dialogue_manager = DialogueManager()

    # ========================================================
    # RESPOND
    # ========================================================

    def respond(self, text):

        text = text.strip()

        if not text:

            return "Please enter a message."

        current_step = (
            self.dialogue_manager
            .get_current_step()
        )

        # ----------------------------------------------------
        # Detect intent
        # ----------------------------------------------------

        intent = detect_intent(text)

        # ----------------------------------------------------
        # GREETING
        # ----------------------------------------------------

        if (
            intent == "greeting"
            and current_step == "idle"
        ):

            return (
                "Hello! Welcome to the "
                "AI Registration Assistant. "
                "I can help you register for "
                "the internship. "
                "Say 'I want to register' "
                "to begin."
            )

        # ----------------------------------------------------
        # HELP
        # ----------------------------------------------------

        if intent == "help":

            return (
                "I can help you with internship "
                "registration. Say 'I want to "
                "register' to begin."
            )

        # ----------------------------------------------------
        # START REGISTRATION
        # ----------------------------------------------------

        if (
            intent == "register"
            and current_step == "idle"
        ):

            self.dialogue_manager.set_step(
                "name"
            )

            return (
                "Sure! I can help you with "
                "internship registration. "
                "What is your name?"
            )

        # ----------------------------------------------------
        # REGISTRATION FLOW
        # ----------------------------------------------------

        if current_step in [
            "name",
            "email",
            "field",
            "confirmation",
            "completed"
        ]:

            result = (
                self.dialogue_manager
                .process_message(text)
            )

            return result["message"]

        # ----------------------------------------------------
        # THANK YOU
        # ----------------------------------------------------

        if intent == "thank_you":

            return "You're welcome!"

        # ----------------------------------------------------
        # FALLBACK
        # ----------------------------------------------------

        return (
            "Sorry, I didn't understand that. "
            "Could you please rephrase?"
        )


# ============================================================
# INTERACTIVE CHAT
# ============================================================

def run_chatbot():

    chatbot = RegistrationChatbot()

    print("=" * 60)
    print("AI REGISTRATION ASSISTANT")
    print("=" * 60)

    print(
        "\nBot: Hello! Welcome to the "
        "AI Registration Assistant."
    )

    print(
        "Bot: Type 'quit' or 'exit' "
        "to end the conversation."
    )

    print()

    while True:

        user_input = input("You: ").strip()

        # ----------------------------------------------------
        # Empty input
        # ----------------------------------------------------

        if not user_input:

            print(
                "Bot: Please enter a message."
            )

            continue

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        if user_input.lower() in [
            "quit",
            "exit",
            "bye"
        ]:

            print(
                "Bot: Goodbye! Thank you."
            )

            break

        # ----------------------------------------------------
        # Generate response
        # ----------------------------------------------------

        response = chatbot.respond(
            user_input
        )

        print(
            f"Bot: {response}"
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    run_chatbot()