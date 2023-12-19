from sklearn.metrics.pairwise import pairwise_distances

from search_engine.parameters import DISTANCE_METRIC, DISTANCES_METRICS


def calculate_distances(query_vector: [float], article_vectors: [[float]], metric: str = DISTANCE_METRIC):
    if len(article_vectors) < 1 or len(query_vector) != len(article_vectors[0]):
        raise ValueError("Incorrect vectors")

    if metric in DISTANCES_METRICS:
        distances = pairwise_distances(article_vectors, [query_vector], metric=metric)
    else:
        raise ValueError("Incorrect metric")

    return distances.flatten().tolist()
