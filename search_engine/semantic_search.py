import pandas as pd

from search_engine.parameters import TOKENIZER, VECTORIZER, SEMANTIZATOR, NUM_TOPICS, DISTANCE_METRIC
from search_engine.semantization import semanticize
from search_engine.similarity import calculate_distances
# from search_engine.tokenizer import tokenize
from search_engine.vectorization import vectorize


def search(query: str, articles: pd.Series, tokenizer=TOKENIZER, vector_method=VECTORIZER,
           semantic_method=SEMANTIZATOR, num_topics=NUM_TOPICS, similarity_metric=DISTANCE_METRIC) -> pd.Series:
    # Create corpus (articles) topics
    # tokens = articles['content'].apply(lambda x: tokenize(x, tokenizer))
    # vectors, vectorizer = vectorize(tokens, method=vector_method)
    vectors, vectorizer = vectorize(articles, method=vector_method, tokenizer=tokenizer)
    topic_vectors, model = semanticize(vectors, method=semantic_method, num_topics=num_topics)

    # Create user query topics
    query_vector = vectorizer.transform([query])
    query_topic_vector = model.transform(query_vector.toarray())

    # Calc similarity between user query and articles topics
    distances = calculate_distances(query_topic_vector[0], topic_vectors, metric=similarity_metric)

    return distances
