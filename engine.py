import pandas as pd

from search_engine.semantic_search import search
from search_engine.parameters import TOKENIZER, VECTORIZER, SEMANTIZATOR, NUM_TOPICS, SIMILARITY_METRIC

# Read articles
# TODO: Read articles from the database - Jakub
# - W osobnym katalogu (lub od razu w bazie w osobnej kolumnie) mogą być surowe pliki html lub xml
# - ich wczytanie, preprocessing i wczytanie do bazy;
# - w bazie mogą być już gotowe artykuły od początku (nie musi się odpalać skrypt preprocessignu przy każdym odpaleniu)
articles = pd.DataFrame(
    {'content': ['Tutaj jest artykuł 1', 'A to artykuł numer 2', 'Trzeci artykuł', 'Bla lbabla']})

# Get user query
# TODO: Implement GUI - Kacper
# 1. Wczytanie inputu przez usera
# 2. Ewentualny wybór sposobów semantyzacji
# 3. Wyświetlenie wyników
# W pliku parameters.py są aktualnie zaimplementowane metody:
# tokenizacji, wektoryzacji, semantyzacji i obliczenia podobieństwa
# Można w menu zaimplementować ich wybór
# ewentualnie można też dodać opcję ponownego preprocessingu i dodania do bazy
#    - jeśli dodamy dodatkowe artykuły do bazy/folderu
tokenizer_choice = TOKENIZER
vectorizer_choice = VECTORIZER
semantic_method_choice = SEMANTIZATOR
similarity_metric_choice = SIMILARITY_METRIC
num_topic = NUM_TOPICS

user_query = input("Podaj zapytanie: ")

# Search
similarities = search(user_query, articles, tokenizer=tokenizer_choice, vector_method=vectorizer_choice,
                      semantic_method=semantic_method_choice, similarity_metric=similarity_metric_choice,
                      num_topics=num_topic)

# Add 'Similarity' column
articles['similarity'] = similarities

# Sort the articles by 'similarity' desc
articles_sorted = articles.sort_values(by='similarity', ascending=False)

# List articles from the best ones
print(articles_sorted)

# Find best match article
# best_match_index = similarities.index(max(similarities))
# best_match_article = articles.iloc[best_match_index]['content']

# print("Najbardziej pasujący artykuł: ")
# print(best_match_article)
