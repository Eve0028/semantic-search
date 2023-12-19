import pandas as pd
import dearpygui.dearpygui as dpg

from search_engine.semantic_search import search
from search_engine.parameters import TOKENIZERS, VECTORIZERS, SEMANTIZATORS, NUM_TOPICS, DISTANCES_METRICS, TOKENIZER, \
    VECTORIZER, SEMANTIZATOR, DISTANCE_METRIC, XML_FILE, CSV_FILE, DIR_FILES, NUMS_TOPICS

# Read articles
articles = pd.read_csv(f'{DIR_FILES}/{CSV_FILE}')


def search_callback():
    user_query = dpg.get_value("QueryInput")

    # Optional: Handle choices from the user for tokenization, vectorization, etc.
    tokenizer_choice = dpg.get_value("TokenizerChoice")
    vectorizer_choice = dpg.get_value("VectorizerChoice")
    semantic_method_choice = dpg.get_value("SemantizatorChoice")
    similarity_metric_choice = dpg.get_value("SimilarityMetricChoice")
    num_topic_choice = dpg.get_value("NumTopicChoice")

    # Search
    distances = search(
        user_query,
        articles['clean_content'],
        tokenizer=tokenizer_choice,
        vector_method=vectorizer_choice,
        semantic_method=semantic_method_choice,
        distance_metric=similarity_metric_choice,
        num_topics=int(num_topic_choice),
    )

    # Add 'Similarity' column
    articles["distance"] = distances

    # Sort the articles by 'similarity' desc
    articles_sorted = articles.sort_values(by="distance")
    articles_sorted = articles_sorted[:10]

    # Update results in Dear PyGui
    result_text = "\n".join(articles_sorted["title"].tolist())
    dpg.set_value("ResultsOutput", result_text)


dpg.create_context()
dpg.create_viewport(title='Semantic Search', width=600, height=300)

with dpg.window(label="Search Engine", width=600, height=300):
    dpg.add_input_text(label="Query", tag="QueryInput", width=200)
    dpg.add_combo(label="Tokenizer", items=TOKENIZERS, default_value=TOKENIZER, tag="TokenizerChoice")
    dpg.add_combo(label="Vectorizer", items=VECTORIZERS, default_value=VECTORIZER, tag="VectorizerChoice")
    dpg.add_combo(label="Semantizator", items=SEMANTIZATORS, default_value=SEMANTIZATOR,
                  tag="SemantizatorChoice")
    dpg.add_combo(label="Similarity Metric", items=DISTANCES_METRICS, default_value=DISTANCE_METRIC,
                  tag="SimilarityMetricChoice")
    dpg.add_combo(label="Number of topics", items=NUMS_TOPICS, default_value=NUM_TOPICS,
                  tag="NumTopicChoice")
    dpg.add_button(label="Search", callback=search_callback)
    dpg.add_text("Results:")
    dpg.add_text("", tag="ResultsOutput", wrap=500)

# Run Dear PyGui
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
