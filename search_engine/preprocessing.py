import nltk
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words

from search_engine.parameters import TOKENIZER, STEMMER, SYNONYMS, STOPWORDS


def to_lower(docs):
    return [doc.lower() for doc in docs]


def throw_stop_words(docs, stopwords=None):
    if stopwords is None:
        stopwords = []
    return [' '.join(w for w in words if w not in stopwords) for words in docs]


nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
stop_words_v2 = sklearn_stop_words


def stemming(docs, stemmer=None, stopwords=None):
    if stopwords is None:
        stopwords = []
    if stemmer:
        docs = [[stemmer.stem(w) for w in words if w not in stopwords] for words in docs]
    return docs


def synonyms_replace(docs, synonyms=None, stopwords=None):
    if stopwords is None:
        stopwords = []
    if synonyms is None:
        synonyms = {}
    return [[synonyms.get(w, w) for w in words if w not in stopwords] for words in docs]


def normalize_corpus_words(corpus, tokenizer=TOKENIZER, stemmer=STEMMER, synonyms=SYNONYMS, stopwords=STOPWORDS):
    docs = to_lower(corpus)
    #     print(f'after lowerize: \n{docs}')
    docs = [tokenizer(doc) for doc in docs]
    #     print(f'after tokenize: \n{docs}')
    docs = synonyms_replace(docs, synonyms, stopwords)
    #     print(f'after synonyms: \n{docs}')

    if stemmer:
        stemming(docs, stemmer)
        docs = synonyms_replace(docs, synonyms, stopwords)

    throw_stop_words(docs, stopwords)
    docs = [' '.join(w for w in words if w not in stopwords) for words in docs]
    #     print(f'after join: \n{docs}')
    return docs
