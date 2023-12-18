from sklearn.metrics import precision_score, recall_score, f1_score
import csv
import pandas as pd

from search_engine.parameters import STEMMERS, VECTORIZERS, SEMANTIZATORS, TOKENIZERS, NUM_TOPICS, SIMILARITY_METRICS, \
    CSV_FILE, TEST_FILE, DIR_FILES
from search_engine.semantic_search import search


def calculate_metrics(true_labels, predicted_labels):
    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)
    return precision, recall, f1


# Funkcja do zapisu wyników do pliku CSV
def write_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Stemmer', 'Tokenizer', 'Vectorizer', 'Semantizator', 'Num_Topics', 'Similarity_Metric',
                      'Precision', 'Recall', 'F1']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for result in results:
            writer.writerow(result)


# Funkcja do obliczania metryk dla różnych parametrów
def calculate_metrics_for_parameters(query, articles, true_labels, output_file):
    results = []

    for stemmer in STEMMERS:
        for tokenizer in TOKENIZERS:
            for vectorizer in VECTORIZERS:
                for semantizator in SEMANTIZATORS:
                    for num_topics in NUM_TOPICS:
                        for similarity_metric in SIMILARITY_METRICS:
                            # Wywołaj funkcję search z odpowiednimi parametrami
                            similarities = search(query, articles, true_labels, tokenizer=tokenizer,
                                                  vector_method=vectorizer,
                                                  semantic_method=semantizator, num_topics=num_topics,
                                                  similarity_metric=similarity_metric)

                            # Przekształć wyniki na etykiety binarne
                            threshold = 0.0
                            predicted_labels = [1 if similarity > threshold else 0 for similarity in similarities]

                            # Oblicz metryki
                            precision, recall, f1 = calculate_metrics(true_labels, predicted_labels)

                            # Zapisz wyniki
                            result = {
                                'Stemmer': stemmer,
                                'Tokenizer': tokenizer,
                                'Vectorizer': vectorizer,
                                'Semantizator': semantizator,
                                'Num_Topics': num_topics,
                                'Similarity_Metric': similarity_metric,
                                'Precision': precision,
                                'Recall': recall,
                                'F1': f1
                            }

                            results.append(result)

    # Zapisz wyniki do pliku CSV
    write_results_to_csv(results, output_file)


# Przykładowe dane testowe
user_query = 'asthma in children'
articles = pd.read_csv(f'{DIR_FILES}/{CSV_FILE}')
results_file = f'{TEST_FILE}'
true_labels = []

# pd.set_option('display.max_colwidth', None)
# print(articles.loc[articles['title'] == 'Acute severe asthma'])

query_results = [{
    'query': 'asthma in children',
    'titles': [],
    'labels': []
}, {

}, {

}]

# Wywołaj funkcję do obliczania metryk dla różnych parametrów
# calculate_metrics_for_parameters(user_query, articles, true_labels, output_file=results_file)
