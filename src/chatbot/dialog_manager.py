# ============================================================
# DIALOGUE MANAGER
# ============================================================

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


class DialogueManager:
    """
    Manage conversation state, context,
    validation, and fallback handling.
    """

    def __init__(self):
        self.reset()

    # ========================================================
    # RESET CONVERSATION
    # ========================================================

    def reset(self):
        """
        Reset the current conversation.
        """

        self.state = {
            "name": None,
            "email": None,
            "field": None,
            "current_step": "idle",
            "error_count": 0
        }

    # ========================================================
    # SET VALUE
    # ========================================================

    def set_value(self, key, value):

        if key in self.state:
            self.state[key] = value

    # ========================================================
    # GET VALUE
    # ========================================================

    def get_value(self, key):

        return self.state.get(key)

    # ========================================================
    # SET STEP
    # ========================================================

    def set_step(self, step):

        self.state["current_step"] = step

        # Reset errors when moving to a new step
        self.state["error_count"] = 0

    # ========================================================
    # GET STEP
    # ========================================================

    def get_current_step(self):

        return self.state["current_step"]

    # ========================================================
    # INCREASE ERROR COUNT
    # ========================================================

    def increase_error_count(self):

        self.state["error_count"] += 1

    # ========================================================
    # RESET ERROR COUNT
    # ========================================================

    def reset_error_count(self):

        self.state["error_count"] = 0

    # ========================================================
    # EXTRACT ENTITIES
    # ========================================================

    def extract_entities(self, text):

        return {
            "name": extract_name(text),
            "email": extract_email(text),
            "field": extract_field(text)
        }

    # ========================================================
    # PROCESS MESSAGE
    # ========================================================

    def process_message(self, text):

        text = text.strip()

        if not text:

            return {
                "success": False,
                "message": "Please enter a response.",
                "state": self.get_state()
            }

        entities = self.extract_entities(text)

        current_step = self.get_current_step()

        # ====================================================
        # NAME
        # ====================================================

        if current_step == "name":

            name = entities["name"]

            if name and validate_name(name):

                self.set_value(
                    "name",
                    name
                )

                self.set_step(
                    "email"
                )

                return {
                    "success": True,
                    "message": (
                        f"Nice to meet you, {name}! "
                        "What is your email address?"
                    ),
                    "state": self.get_state()
                }

            # Invalid name
            self.increase_error_count()

            if self.state["error_count"] >= 3:

                return {
                    "success": False,
                    "message": (
                        "I'm having trouble getting "
                        "your name. Please enter it "
                        "using letters only, for example: "
                        "Siraj or Mohammed Siraj."
                    ),
                    "state": self.get_state()
                }

            return {
                "success": False,
                "message": (
                    "I couldn't identify your name. "
                    "Please say something like: "
                    "'My name is Siraj'."
                ),
                "state": self.get_state()
            }

        # ====================================================
        # EMAIL
        # ====================================================

        if current_step == "email":

            email = entities["email"]

            if email and validate_email(email):

                self.set_value(
                    "email",
                    email
                )

                self.set_step(
                    "field"
                )

                return {
                    "success": True,
                    "message": (
                        "Thank you! What is your "
                        "field of study?"
                    ),
                    "state": self.get_state()
                }

            # Invalid email
            self.increase_error_count()

            if self.state["error_count"] >= 3:

                return {
                    "success": False,
                    "message": (
                        "The email still doesn't appear "
                        "to be valid. Please enter a complete "
                        "email address such as "
                        "'student@gmail.com'."
                    ),
                    "state": self.get_state()
                }

            return {
                "success": False,
                "message": (
                    "That doesn't look like a valid "
                    "email address. Please provide an email "
                    "such as 'student@gmail.com'."
                ),
                "state": self.get_state()
            }

        # ====================================================
        # FIELD
        # ====================================================

        if current_step == "field":

            field = entities["field"]

            if field and validate_field(field):

                self.set_value(
                    "field",
                    field
                )

                self.set_step(
                    "confirmation"
                )

                return {
                    "success": True,
                    "message": (
                        "Great! I have collected "
                        "all your information.\n\n"
                        "Please confirm your details:\n"
                        f"Name: {self.get_value('name')}\n"
                        f"Email: {self.get_value('email')}\n"
                        f"Field: {self.get_value('field')}\n\n"
                        "Are these details correct? "
                        "Please say yes or no."
                    ),
                    "state": self.get_state()
                }

            # Invalid field
            self.increase_error_count()

            if self.state["error_count"] >= 3:

                return {
                    "success": False,
                    "message": (
                        "I still couldn't recognize "
                        "your field. Some supported "
                        "fields are Computer Science, "
                        "Data Science, AI, ML, ECE, "
                        "EEE, IT, Mechanical, and Civil."
                    ),
                    "state": self.get_state()
                }

            return {
                "success": False,
                "message": (
                    "I couldn't recognize that field. "
                    "Please provide a supported field "
                    "such as CSE, ECE, AI, ML, or "
                    "Data Science."
                ),
                "state": self.get_state()
            }

        # ====================================================
        # CONFIRMATION
        # ====================================================

        if current_step == "confirmation":

            normalized_text = text.lower()

            if normalized_text in [
                "yes",
                "y",
                "correct",
                "confirm",
                "confirmed",
                "yes correct"
            ]:

                self.set_step(
                    "completed"
                )

                return {
                    "success": True,
                    "message": (
                        "Perfect! Your information "
                        "has been confirmed."
                    ),
                    "state": self.get_state()
                }

            if normalized_text in [
                "no",
                "n",
                "incorrect",
                "wrong"
            ]:

                return {
                    "success": False,
                    "message": (
                        "No problem. Please tell me "
                        "which information needs to "
                        "be corrected."
                    ),
                    "state": self.get_state()
                }

            self.increase_error_count()

            return {
                "success": False,
                "message": (
                    "Please confirm your information "
                    "by saying 'yes' or 'no'."
                ),
                "state": self.get_state()
            }

        # ====================================================
        # COMPLETED
        # ====================================================

        if current_step == "completed":

            return {
                "success": True,
                "message": (
                    "Your registration information "
                    "has already been confirmed."
                ),
                "state": self.get_state()
            }

        # ====================================================
        # IDLE
        # ====================================================

        return {
            "success": False,
            "message": (
                "Please say 'I want to register' "
                "to begin the registration process."
            ),
            "state": self.get_state()
        }

    # ========================================================
    # REGISTRATION COMPLETE
    # ========================================================

    def is_registration_complete(self):

        return (
            self.state["name"] is not None
            and self.state["email"] is not None
            and self.state["field"] is not None
        )

    # ========================================================
    # MISSING INFORMATION
    # ========================================================

    def get_missing_information(self):

        missing = []

        if self.state["name"] is None:
            missing.append("name")

        if self.state["email"] is None:
            missing.append("email")

        if self.state["field"] is None:
            missing.append("field")

        return missing

    # ========================================================
    # GET STATE
    # ========================================================

    def get_state(self):

        return self.state.copy()