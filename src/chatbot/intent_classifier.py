# ============================================================
# INTENT CLASSIFIER
# ============================================================

from src.nlp.preprocessing import preprocess_text


# ============================================================
# RULE-BASED INTENT KEYWORDS
# ============================================================

INTENT_KEYWORDS = {

    "greeting": [
        "hello",
        "hi",
        "hey",
        "greet"
    ],

    "register": [
        "register",
        "registration",
        "apply",
        "join",
        "enroll",
        "signup",
        "sign"
    ],

    "help": [
        "help",
        "assist",
        "support",
        "guidance"
    ],

    "thank_you": [
        "thank",
        "thanks",
        "appreciate"
    ]
}


# ============================================================
# INTENT RESPONSES
# ============================================================

INTENT_RESPONSES = {

    "greeting":
        "Hello! Welcome to the AI Registration Assistant.",

    "register":
        "Sure! I can help you with internship registration.",

    "help":
        "I can help you with internship registration and related questions.",

    "thank_you":
        "You're welcome!",

    "unknown":
        "Sorry, I didn't understand that. Could you please rephrase."
}


# ============================================================
# CLASSIFY INTENT
# ============================================================

def classify_intent(tokens):
    """
    Classify an intent using keyword matching.
    """

    for intent, keywords in INTENT_KEYWORDS.items():

        for word in tokens:

            if word in keywords:
                return intent

    return "unknown"


# ============================================================
# DETECT INTENT
# ============================================================

def detect_intent(text):
    """
    Preprocess the user's message and detect its intent.
    """

    tokens = preprocess_text(text)

    return classify_intent(tokens)


# ============================================================
# GENERATE RESPONSE
# ============================================================

def generate_response(intent):

    return INTENT_RESPONSES.get(
        intent,
        INTENT_RESPONSES["unknown"]
    )


# ============================================================
# CHATBOT RESPONSE
# ============================================================

def chatbot_response(text):

    intent = detect_intent(text)

    return generate_response(intent)


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    test_messages = [

        "Hello",

        "Hi there",

        "I want to register",

        "I want to apply for the internship",

        "I want to join the internship",

        "Can you help me?",

        "Thanks for your help",

        "I like playing cricket"
    ]

    print("=" * 60)
    print("INTENT CLASSIFIER TEST")
    print("=" * 60)

    for message in test_messages:

        tokens = preprocess_text(message)
        intent = classify_intent(tokens)

        print(f"\nUser: {message}")
        print(f"Tokens: {tokens}")
        print(f"Intent: {intent}")