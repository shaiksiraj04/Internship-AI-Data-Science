import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag


# Stopwords
STOP_WORDS = set(stopwords.words("english"))

# Lemmatizer
LEMMATIZER = WordNetLemmatizer()


def get_wordnet_pos(tag):
    """
    Convert NLTK POS tags into WordNet POS tags.
    """

    if tag.startswith("J"):
        return "a"       # Adjective

    elif tag.startswith("V"):
        return "v"       # Verb

    elif tag.startswith("N"):
        return "n"       # Noun

    elif tag.startswith("R"):
        return "r"       # Adverb

    return "n"


def preprocess_text(text):
    """
    Preprocess user input using:
    1. Lowercasing
    2. Tokenization
    3. Punctuation removal
    4. Stopword removal
    5. POS tagging
    6. Lemmatization

    Returns:
        list: Cleaned and lemmatized tokens
    """

    # 1. Convert text to lowercase
    text = text.lower()

    # 2. Tokenize text
    tokens = word_tokenize(text)

    # 3. Remove punctuation
    tokens = [
        word
        for word in tokens
        if word not in string.punctuation
    ]

    # 4. Remove stopwords
    tokens = [
        word
        for word in tokens
        if word not in STOP_WORDS
    ]

    # 5. POS tagging
    tagged_tokens = pos_tag(tokens)

    # 6. Lemmatization using POS tags
    tokens = [
        LEMMATIZER.lemmatize(
            word,
            get_wordnet_pos(tag)
        )
        for word, tag in tagged_tokens
    ]

    return tokens


if __name__ == "__main__":

    test_text = "HELLO!!! I am STUDYING Computer Science."

    print("Original:")
    print(test_text)

    print("\nProcessed:")
    print(preprocess_text(test_text))