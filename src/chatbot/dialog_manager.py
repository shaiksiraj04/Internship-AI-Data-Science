"""
Dialogue manager for the AI Registration Assistant.

This module manages:
- Conversation state
- Registration information
- Validation
- Confirmation
- Registration completion
"""

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
    add_registration,
    email_exists
)

from src.registration.registration_processor import (
    complete_registration
)

from src.registration.confirmation import (
    create_summary,
    interpret_confirmation
)


class DialogueManager:
    """Manage the state and flow of a registration conversation."""

    def __init__(self):
        """Initialize a new conversation."""

        self.reset()

    # -------------------------------------------------
    # State management
    # -------------------------------------------------

    def reset(self):
        """Reset the conversation state."""

        self.state = {
            "name": None,
            "email": None,
            "field": None,
            "current_step": "idle"
        }

        self.error_count = 0

    def set_step(self, step):
        """Set the current conversation step."""

        self.state["current_step"] = step
        self.error_count = 0

    def get_step(self):
        """Return the current conversation step."""

        return self.state["current_step"]

    def set_value(self, key, value):
        """Store a value in the conversation state."""

        self.state[key] = value

    def get_value(self, key):
        """Get a value from the conversation state."""

        return self.state.get(key)

    # -------------------------------------------------
    # State checks
    # -------------------------------------------------

    def has_name(self):
        return bool(self.state["name"])

    def has_email(self):
        return bool(self.state["email"])

    def has_field(self):
        return bool(self.state["field"])

    def is_registration_complete(self):
        """Check whether all registration information exists."""

        return (
            self.has_name()
            and self.has_email()
            and self.has_field()
        )

    def get_missing_information(self):
        """Return missing registration fields."""

        missing = []

        if not self.has_name():
            missing.append("name")

        if not self.has_email():
            missing.append("email")

        if not self.has_field():
            missing.append("field")

        return missing

    def get_state(self):
        """Return a copy of the current state."""

        return self.state.copy()

    # -------------------------------------------------
    # Name handling
    # -------------------------------------------------

    def process_name(self, text):
        """Process and validate the student's name."""

        name = extract_name(text)

        if not name:
            self.error_count += 1

            if self.error_count >= 2:
                return (
                    "I couldn't identify your name. "
                    "Please use a format like: "
                    "'My name is Siraj'."
                )

            return "Please provide your name. For example: My name is Siraj."

        if not validate_name(name):
            self.error_count += 1

            return (
                "That doesn't look like a valid name. "
                "Please enter your name using letters only."
            )

        self.set_value("name", name)
        self.set_step("email")

        return (
            f"Nice to meet you, {name}! "
            "What is your email address?"
        )

    # -------------------------------------------------
    # Email handling
    # -------------------------------------------------

    def process_email(self, text):
        """Process and validate the student's email."""

        email = extract_email(text)

        if not email:
            self.error_count += 1

            if self.error_count >= 2:
                return (
                    "I couldn't identify a valid email address. "
                    "Please use a format such as "
                    "siraj@example.com."
                )

            return "Please provide a valid email address."

        if not validate_email(email):
            self.error_count += 1

            return (
                "That email address is not valid. "
                "Please try again."
            )

        # Check duplicate email early
        if email_exists(email):
            self.error_count += 1

            return (
                "This email address is already registered. "
                "Please provide a different email address."
            )

        self.set_value("email", email)
        self.set_step("field")

        return (
            "Thank you! What is your field of study?\n"
            "For example: CSE, Data Science, AI, ECE, or Mechanical."
        )

    # -------------------------------------------------
    # Field handling
    # -------------------------------------------------

    def process_field(self, text):
        """Process and validate the student's field."""

        field = extract_field(text)

        if not field:
            self.error_count += 1

            if self.error_count >= 2:
                return (
                    "I couldn't identify your field of study. "
                    "Please provide a field such as "
                    "Computer Science, Data Science, "
                    "Artificial Intelligence, ECE, or Mechanical."
                )

            return "Please provide your field of study."

        if not validate_field(field):
            self.error_count += 1

            return "That field is not currently supported. Please try another field."

        self.set_value("field", field)
        self.set_step("confirmation")

        return create_summary(
            self.state["name"],
            self.state["email"],
            self.state["field"]
        )

    # -------------------------------------------------
    # Confirmation handling
    # -------------------------------------------------

    def process_confirmation(self, text):
        """Process the user's confirmation response."""

        confirmation = interpret_confirmation(text)

        # ---------------------------------------------
        # User confirmed
        # ---------------------------------------------

        if confirmation == "yes":

            name = self.state["name"]
            email = self.state["email"]
            field = self.state["field"]

            # Final registration processing
            result = complete_registration(
                name,
                email,
                field
            )

            if not result["success"]:

                if result.get("duplicate"):
                    return (
                        "This email address is already registered. "
                        "Please restart the registration with a different email."
                    )

                return (
                    f"Registration could not be completed: "
                    f"{result['message']}"
                )

            # Save registration
            add_registration(result["data"])

            self.set_step("completed")

            return (
                "\nPerfect! Your registration has been "
                "successfully completed. 🎉\n\n"
                "Thank you for registering for the internship!"
            )

        # ---------------------------------------------
        # User rejected
        # ---------------------------------------------

        if confirmation == "no":

            self.set_step("correction")

            return (
                "No problem. Which information would you like "
                "to correct?\n\n"
                "1. Name\n"
                "2. Email\n"
                "3. Field"
            )

        # ---------------------------------------------
        # Unknown response
        # ---------------------------------------------

        self.error_count += 1

        return (
            "Please confirm your registration by answering "
            "'yes' or 'no'."
        )

    # -------------------------------------------------
    # Correction handling
    # -------------------------------------------------

    def process_correction(self, text):
        """Handle correction requests after confirmation."""

        response = text.strip().lower()

        # Name correction
        if (
            "name" in response
            or response == "1"
        ):
            self.set_step("name")

            return "Sure. Please provide your correct name."

        # Email correction
        if (
            "email" in response
            or "mail" in response
            or response == "2"
        ):
            self.set_step("email")

            return "Sure. Please provide your correct email address."

        # Field correction
        if (
            "field" in response
            or "study" in response
            or response == "3"
        ):
            self.set_step("field")

            return "Sure. Please provide your correct field of study."

        return (
            "Please choose one option:\n"
            "1. Name\n"
            "2. Email\n"
            "3. Field"
        )

    # -------------------------------------------------
    # Completed state
    # -------------------------------------------------

    def process_completed(self, text):
        """Handle messages after registration is completed."""

        return (
            "Your registration has already been completed. "
            "Thank you!"
        )

    # -------------------------------------------------
    # Main message processor
    # -------------------------------------------------

    def process_message(self, text):
        """
        Process a message according to the current state.

        Args:
            text (str): User message

        Returns:
            str: Chatbot response
        """

        if not text or not text.strip():

            return (
                "I didn't receive any information. "
                "Please enter a message."
            )

        current_step = self.get_step()

        if current_step == "name":
            return self.process_name(text)

        if current_step == "email":
            return self.process_email(text)

        if current_step == "field":
            return self.process_field(text)

        if current_step == "confirmation":
            return self.process_confirmation(text)

        if current_step == "correction":
            return self.process_correction(text)

        if current_step == "completed":
            return self.process_completed(text)

        return (
            "Please tell me if you would like to "
            "register for the internship."
        )


if __name__ == "__main__":

    print("Testing Dialogue Manager...\n")

    manager = DialogueManager()

    print("Step:", manager.get_step())

    manager.set_step("name")

    print(
        "\nBot:",
        manager.process_message("My name is Test Student")
    )

    print(
        "Current step:",
        manager.get_step()
    )

    print("\nDialogue manager test completed.")