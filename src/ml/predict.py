import os
import pickle


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "intent_model.pkl"
)


CONFIDENCE_THRESHOLD = 0.45


def load_model():
    """
    Load the trained intent classification model.
    """

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model


def predict_intent(text):
    """
    Predict the intent of a user message.

    If the model confidence is below the threshold,
    return 'unknown'.
    """

    model = load_model()

    probabilities = model.predict_proba([text])[0]

    class_index = probabilities.argmax()

    predicted_intent = model.classes_[class_index]

    confidence = probabilities[class_index]

    if confidence < CONFIDENCE_THRESHOLD:
        predicted_intent = "unknown"

    return predicted_intent, confidence


if __name__ == "__main__":

    model = load_model()

    test_messages = [
        "Hello there!",
        "I want to register for the internship",
        "Can you help me?",
        "I am studying computer science",
        "My name is Siraj",
        "My email is siraj@gmail.com",
        "I am a beginner in programming",
        "Thank you for your help",
        "I like playing cricket",
        "What is the weather today?"
    ]

    print("ML Intent Prediction")
    print("=" * 50)

    for message in test_messages:

        probabilities = model.predict_proba([message])[0]

        class_index = probabilities.argmax()

        predicted_intent = model.classes_[class_index]

        confidence = probabilities[class_index]

        if confidence < CONFIDENCE_THRESHOLD:
            predicted_intent = "unknown"

        print(f"\nUser: {message}")
        print(f"Intent: {predicted_intent}")
        print(f"Confidence: {confidence:.2f}")