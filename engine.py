import pandas as pd
import dearpygui.dearpygui as dpg

from DataManager.tempParser import get_parsed_articles, parse_articles_to_csv
from search_engine.semantic_search import search
from search_engine.parameters import TOKENIZERS, VECTORIZERS, SEMANTIZATORS, NUM_TOPICS, DISTANCES_METRICS, TOKENIZER, \
    VECTORIZER, SEMANTIZATOR, DISTANCE_METRIC, XML_FILE, CSV_FILE

# Read articles
# TODO: Read articles from the database - Jakub
# - W osobnym katalogu (lub od razu w bazie w osobnej kolumnie) mogą być surowe pliki html lub xml
# - ich wczytanie, preprocessing i wczytanie do bazy;
# - w bazie mogą być już gotowe artykuły od początku (nie musi się odpalać skrypt preprocessignu przy każdym odpaleniu)

    # articles = pd.DataFrame(get_parsed_articles(file))
articles = pd.read_csv(CSV_FILE)

user_query = 'asthma in children'

similarities = search(
        user_query,
        articles,
        tokenizer=TOKENIZER,
        vector_method=VECTORIZER,
        semantic_method=SEMANTIZATOR,
        similarity_metric=DISTANCE_METRIC,
        num_topics=NUM_TOPICS,
    )
articles["similarity"] = similarities
articles_sorted = articles.sort_values(by="similarity", ascending=False)
print(articles_sorted)


def search_callback():
    user_query = dpg.get_value("QueryInput")

    # Optional: Handle choices from the user for tokenization, vectorization, etc.
    tokenizer_choice = dpg.get_value("TokenizerChoice")
    vectorizer_choice = dpg.get_value("VectorizerChoice")
    semantic_method_choice = dpg.get_value("SemantizatorChoice")
    similarity_metric_choice = dpg.get_value("SimilarityMetricChoice")

    # Search
    similarities = search(
        user_query,
        articles,
        tokenizer=tokenizer_choice,
        vector_method=vectorizer_choice,
        semantic_method=semantic_method_choice,
        similarity_metric=similarity_metric_choice,
        num_topics=NUM_TOPICS,
    )

    # Add 'Similarity' column
    articles["similarity"] = similarities

    # Sort the articles by 'similarity' desc
    articles_sorted = articles.sort_values(by="similarity", ascending=False)

    # Update results in Dear PyGui
    result_text = "\n".join(articles_sorted["content"].tolist())
    dpg.set_value("ResultsOutput", result_text)


# Find best match article
# best_match_index = similarities.index(max(similarities))
# best_match_article = articles.iloc[best_match_index]['content']
#
# print("Najbardziej pasujący artykuł: ")
# print(best_match_article)


# dpg.create_context()
# dpg.create_viewport(title='Semantic Search', width=600, height=300)
#
# with dpg.window(label="Search Engine", width=600, height=300):
#     dpg.add_input_text(label="Query", tag="QueryInput", width=200)
#     dpg.add_combo(label="Tokenizer", items=TOKENIZERS, default_value=tokenizer_choice, tag="TokenizerChoice")
#     dpg.add_combo(label="Vectorizer", items=VECTORIZERS, default_value=vectorizer_choice, tag="VectorizerChoice")
#     dpg.add_combo(label="Semantizator", items=SEMANTIZATORS, default_value=semantic_method_choice,
#                   tag="SemantizatorChoice")
#     dpg.add_combo(label="Similarity Metric", items=SIMILARITY_METRICS, default_value=similarity_metric_choice,
#                   tag="SimilarityMetricChoice")
#     dpg.add_button(label="Search", callback=search_callback)
#     dpg.add_text("Results:")
#     dpg.add_text("", tag="ResultsOutput", wrap=500)
#
# # Run Dear PyGui
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()
