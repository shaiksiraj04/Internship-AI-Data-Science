import json
import os
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


# Project paths
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "intents.json"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "intent_model.pkl"
)


def load_training_data():
    """
    Load intent patterns from intents.json.
    """

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    texts = []
    labels = []

    for intent in data["intents"]:

        intent_name = intent["intent"]

        for pattern in intent["patterns"]:
            texts.append(pattern)
            labels.append(intent_name)

    return texts, labels


def train_model():
    """
    Train the intent classification model.
    """

    texts, labels = load_training_data()

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                ngram_range=(1, 2)
            )
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ])

    model.fit(texts, labels)

    os.makedirs(MODEL_DIR, exist_ok=True)

    with open(MODEL_PATH, "wb") as file:
        pickle.dump(model, file)

    print("Training completed successfully.")
    print(f"Training examples: {len(texts)}")
    print(f"Intent classes: {len(set(labels))}")
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    train_model()