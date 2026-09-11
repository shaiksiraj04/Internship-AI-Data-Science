from src.nlp.preprocessing import preprocess_text

INTENT_KEYWORDS = {
    "greeting": ["hello", "hi", "hey"],
    "register": ["register", "registration", "apply", "join"],
    "help": ["help", "assist", "support"],
}


def classify_intent(tokens):
    for intent, keywords in INTENT_KEYWORDS.items():
        for word in tokens:
            if word in keywords:
                return intent

    return "unknown"

def detect_intent(text):
    tokens = preprocess_text(text)
    return classify_intent(tokens)

print(detect_intent("Hello!"))
print(detect_intent("I WANT TO REGISTER FOR THE INTERNSHIP!!!"))
print(detect_intent("I need some help."))
print(detect_intent("I am studying computer science."))
