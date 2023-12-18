from sklearn.metrics import DistanceMetric
from sklearn.metrics.pairwise import cosine_similarity

from search_engine.parameters import SIMILARITY_METRIC, SIMILARITY_METRICS


def calculate_similarity(query_vector: [float], article_vectors: [[float]], metric=SIMILARITY_METRIC):
    similarities = []

    if len(article_vectors) < 1 or len(query_vector) != len(article_vectors[0]):
        raise ValueError("Incorrect vectors")

    if metric in SIMILARITY_METRICS:
        if metric == 'cosine':
            similarity_function = cosine_similarity
        else:
            distance_metric = DistanceMetric.get_metric(SIMILARITY_METRIC)
            similarity_function = lambda x, y: 1 / (1 + distance_metric.pairwise([x, y])[0][1])

        query_vector_2d = query_vector.reshape(1, -1)
        for article_vector in article_vectors:
            article_vector_2d = article_vector.reshape(1, -1)
            similarities.append(similarity_function(query_vector_2d, article_vector_2d)[0][0])
    else:
        raise ValueError("Incorrect metric")

    return similarities
