# STOPWORDS = 'a an and or the do are with from for of on in by if at to into them'.split()
# STOPWORDS += 'to at it its it\'s that than our you your - -- " \' ? , . !'.split()
STOPWORDS = []

# SYNONYMS = dict(zip(
#     'wolv people person women woman man human he  we  her she him his hers'.split(),
#     'wolf her    her    her   her   her her   her her her her her her her'.split()))
# SYNONYMS.update(dict(zip(
#     'ate pat smarter have had isn\'t hasn\'t no  got get become been was were wa be sat seat sit smaller'.split(),
#     'eat pet smart   has  has not    not     not has has is     is   is  is   is is sit sit  sit small'.split())))
# SYNONYMS.update(dict(zip(
#     'i me my mine our ours catbird bird birds birder tortoise turtle turtles turtle\'s don\'t'.split(),
#     'i i  i  i    i   i    bird    bird birds bird   turtle   turtle turtle  turtle    not'.split())))
SYNONYMS = {}

STEMMERS = ['porter', 'snowball']
STEMMER = STEMMERS[0]

TOKENIZERS = ['treebank', 'casual', 'biobert', 'punkt']
TOKENIZER = TOKENIZERS[2]

VECTORIZERS = ['tfidf', 'bow']
VECTORIZER = VECTORIZERS[0]

SEMANTIZATORS = ['pca', 'ldia', 'svd']
SEMANTIZATOR = SEMANTIZATORS[0]

NUMS_TOPICS = [3, 5, 7]
NUM_TOPICS = NUMS_TOPICS[0]

SIMILARITY_METRICS = ['cosine', 'chebyshev', 'manhattan', 'euclidean']
SIMILARITY_METRIC = SIMILARITY_METRICS[0]

DIR_FILES = 'DataManager'
XML_FILE = 'asthma_40.xml'
CSV_FILE = 'parsed_articles.csv'
TEST_FILE = 'results.csv'
