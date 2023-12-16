from sklearn.metrics.pairwise import cosine_similarity

from search_engine.parameters import SIMILARITY_METRIC


def calculate_similarity(query_vector: [float], article_vectors: [[float]], metric=SIMILARITY_METRIC):
    similarities = []

    if len(article_vectors) < 1 or len(query_vector) != len(article_vectors[0]):
        raise ValueError("Incorrect vectors")

    if metric == 'cosine':
        for article_vector in article_vectors:
            similarities.append(cosine_similarity([query_vector], [article_vector])[0][0])
    else:
        raise ValueError("Incorrect metric")
    # Add other methods

    return similarities
