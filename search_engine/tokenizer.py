from typing import Callable

import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.casual import casual_tokenize
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from transformers import AutoTokenizer

from search_engine.parameters import TOKENIZER


def get_tokenizer(tokenizer=TOKENIZER) -> Callable:
    if tokenizer == 'treebank':
        tokenizer = TreebankWordTokenizer().tokenize
    elif tokenizer == 'casual':
        tokenizer = casual_tokenize
    elif tokenizer == 'biobert':
        tokenizer = (AutoTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")).tokenize
    elif tokenizer == 'punkt':
        nltk.download('punkt')
        tokenizer = word_tokenize
    else:
        raise ValueError("Incorrect tokenizer")

    return tokenizer

# Search about n-gram's
