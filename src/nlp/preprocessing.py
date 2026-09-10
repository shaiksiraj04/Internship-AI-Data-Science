import nltk
import string
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    text = text.lower()
    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in string.punctuation]

    return tokens

print(preprocess_text("HELLO!!! I WANT TO REGISTER!!!"))
