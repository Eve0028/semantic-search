from sklearn.decomposition import PCA, LatentDirichletAllocation, TruncatedSVD

from search_engine.parameters import SEMANTIZATOR, NUM_TOPICS


def semanticize(vectors, method=SEMANTIZATOR, num_topics=NUM_TOPICS):
    if method == 'lda':
        semantizator = LatentDirichletAllocation(n_components=num_topics)
    elif method == 'pca':
        semantizator = PCA(n_components=num_topics)
    elif method == 'svd':
        semantizator = TruncatedSVD(n_components=num_topics)
    else:
        raise ValueError("Incorrect semantizator")

    topic_vectors = semantizator.fit_transform(vectors)
    return topic_vectors, semantizator
