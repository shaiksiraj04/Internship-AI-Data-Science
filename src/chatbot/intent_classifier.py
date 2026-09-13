from src.nlp.preprocessing import preprocess_text


# Intent keywords
INTENT_KEYWORDS = {

    "greeting": [
        "hello",
        "hi",
        "hey"
    ],

    "register": [
        "register",
        "registration",
        "apply",
        "join"
    ],

    "help": [
        "help",
        "assist",
        "support"
    ]
}


# Responses for each intent
INTENT_RESPONSES = {

    "greeting":
        "Hello! Welcome to the AI Registration Assistant.",

    "register":
        "Sure! I can help you with internship registration.",

    "help":
        "I can help you with internship registration and related questions.",

    "unknown":
        "Sorry, I didn't understand that. Could you please rephrase."
}


def classify_intent(tokens):
    """
    Identify the user's intent from processed tokens.
    """

    for intent, keywords in INTENT_KEYWORDS.items():

        for word in tokens:

            if word in keywords:
                return intent

    return "unknown"


def detect_intent(text):
    """
    Process raw user text and identify its intent.
    """

    tokens = preprocess_text(text)

    return classify_intent(tokens)


def generate_response(intent):
    """
    Generate a response based on the detected intent.
    """

    return INTENT_RESPONSES.get(
        intent,
        INTENT_RESPONSES["unknown"]
    )


def chatbot_response(text):
    """
    Complete chatbot pipeline:

    User text
        ↓
    Preprocessing
        ↓
    Intent detection
        ↓
    Response generation
    """

    intent = detect_intent(text)

    response = generate_response(intent)

    return response


if __name__ == "__main__":

    test_messages = [
        "Hello!",
        "I WANT TO REGISTER FOR THE INTERNSHIP!!!",
        "I need some help.",
        "I am studying computer science.",
        "I'd like to join the internship."
    ]

    for message in test_messages:

        print("\nUser:", message)

        intent = detect_intent(message)

        print("Intent:", intent)

        print("Bot:", generate_response(intent))