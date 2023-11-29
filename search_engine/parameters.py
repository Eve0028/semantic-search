NUM_TOPICS = 2
NUM_WORDS = 2
NUM_DOCS = NUM_PRETTY = 16
# import nltk
# nltk.download('wordnet')  # noqa
# from nltk.stem.wordnet import WordNetLemmatizer

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

stemmer = None  # PorterStemmer()

# tokenizer =
