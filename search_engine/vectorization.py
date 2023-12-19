from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

from search_engine.parameters import TOKENIZER, VECTORIZER
from search_engine.tokenizer import get_tokenizer


def vectorize(texts: pd.Series, method=VECTORIZER, tokenizer=TOKENIZER):
    tokenizer = get_tokenizer(tokenizer)
    if method == 'bow':
        vectorizer = CountVectorizer(tokenizer=tokenizer)
    elif method == 'tfidf':
        vectorizer = TfidfVectorizer(tokenizer=tokenizer)
    else:
        raise ValueError("Incorrect vectorizer")

    texts = texts.str.lower()
    vectors = vectorizer.fit_transform(texts).toarray()
    return vectors, vectorizer
