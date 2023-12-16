from typing import Callable

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.casual import casual_tokenize
from nltk.util import ngrams

from search_engine.parameters import TOKENIZER


def get_tokenizer(tokenizer=TOKENIZER) -> Callable:
    if tokenizer == 'regexp':
        tokenizer = RegexpTokenizer(r'\w+').tokenize
    elif tokenizer == 'treebank':
        tokenizer = TreebankWordTokenizer().tokenize
    elif tokenizer == 'casual':
        tokenizer = casual_tokenize
    else:
        raise ValueError("Incorrect tokenizer")

    return tokenizer

# Search about n-gram's
