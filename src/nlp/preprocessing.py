import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag


STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()


def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return "a"
    elif tag.startswith("V"):
        return "v"
    elif tag.startswith("N"):
        return "n"
    elif tag.startswith("R"):
        return "r"
    else:
        return "n"


def preprocess_text(text):
    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    tokens = [
        word for word in tokens
        if word not in STOP_WORDS
    ]

    tagged_tokens = pos_tag(tokens)

    tokens = [
        LEMMATIZER.lemmatize(word, get_wordnet_pos(tag))
        for word, tag in tagged_tokens
    ]

    return tokens