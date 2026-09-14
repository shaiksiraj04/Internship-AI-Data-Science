"""
ML intent prediction module.

Uses the trained TF-IDF + Logistic Regression model
to predict the user's intent and confidence score.
"""

from pathlib import Path
import joblib


# -------------------------------------------------
# Model paths
# -------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "intent_model.pkl"


# -------------------------------------------------
# Load model
# -------------------------------------------------

model = joblib.load(MODEL_PATH)


# -------------------------------------------------
# Configuration
# -------------------------------------------------

CONFIDENCE_THRESHOLD = 0.50


# -------------------------------------------------
# Prediction
# -------------------------------------------------

def predict_intent(text):
    """
    Predict the intent of a user message.

    Args:
        text (str): User message

    Returns:
        tuple: (intent, confidence)
    """

    if not text or not text.strip():
        return "unknown", 0.0

    probabilities = model.predict_proba([text])[0]

    classes = model.classes_

    best_index = probabilities.argmax()

    intent = classes[best_index]
    confidence = float(probabilities[best_index])

    # -------------------------------------------------
    # Unknown intent handling
    # -------------------------------------------------

    if confidence < CONFIDENCE_THRESHOLD:
        return "unknown", confidence

    return intent, confidence


def predict_intent_with_details(text):
    """
    Return detailed intent prediction information.

    Args:
        text (str): User message

    Returns:
        dict: Intent prediction details
    """

    intent, confidence = predict_intent(text)

    return {
        "text": text,
        "intent": intent,
        "confidence": round(confidence, 4)
    }


# -------------------------------------------------
# Manual testing
# -------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("       ML INTENT PREDICTION TEST")
    print("=" * 60)

    test_messages = [
        "Hello",
        "I want to register",
        "Can you help me?",
        "My name is Siraj",
        "siraj@example.com",
        "I study computer science",
        "Thank you",
        "The weather is beautiful today",
        "I like playing cricket"
    ]

    for message in test_messages:

        result = predict_intent_with_details(message)

        print()
        print(f"Text       : {result['text']}")
        print(f"Intent     : {result['intent']}")
        print(f"Confidence : {result['confidence']}")