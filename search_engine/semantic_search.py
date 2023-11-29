# TODO: Builder implementation
from search_engine.tokenizer import Tokenizer


class Semantic:
    pass


class Product1:
    pass


class SemanticDocument(Semantic):
    def __init__(self, tokenizer: Tokenizer) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset(tokenizer)

    def reset(self, tokenizer: Tokenizer) -> None:
        self._product = Product1(tokenizer)
