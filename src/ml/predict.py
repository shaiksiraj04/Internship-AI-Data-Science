import os
import pickle


# Project paths
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


def load_model():
    """
    Load the trained intent model.
    """

    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)

    return model


def predict_intent(text):
    """
    Predict the intent of a new user message.
    """

    model = load_model()

    prediction = model.predict([text])

    return prediction[0]


if __name__ == "__main__":

    model = load_model()

    test_messages = [
        "Hello there!",
        "I want to sign up for the internship",
        "Can you help me?",
        "I am studying computer science",
        "My name is Siraj",
        "My email is siraj@gmail.com",
        "I am a beginner in programming",
        "Thank you for your help",
        "I like playing cricket"
    ]

    for message in test_messages:

        intent = model.predict([message])[0]

        print(f"\nUser: {message}")
        print(f"Predicted Intent: {intent}")