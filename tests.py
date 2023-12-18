from sklearn.metrics import precision_score, recall_score, f1_score
import csv
import pandas as pd

from search_engine.parameters import STEMMERS, VECTORIZERS, SEMANTIZATORS, TOKENIZERS, DISTANCES_METRICS, \
    CSV_FILE, TEST_FILE, DIR_FILES, NUMS_TOPICS
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
def calculate_metrics_for_parameters(queries, labels, articles: pd.Series, output_file):
    results = []

    for i in range(len(queries)):
        query = queries[i]
        true_labels = labels[i]

        for stemmer in STEMMERS:
            for tokenizer in TOKENIZERS:
                for vectorizer in VECTORIZERS:
                    for semantizator in SEMANTIZATORS:
                        for num_topics in NUMS_TOPICS:
                            for similarity_metric in DISTANCES_METRICS:
                                # Wywołaj funkcję search z odpowiednimi parametrami
                                distances = search(query, articles, tokenizer=tokenizer,
                                                   vector_method=vectorizer,
                                                   semantic_method=semantizator, num_topics=num_topics,
                                                   similarity_metric=similarity_metric)

                                sorted_distances = sorted(distances)

                                # Przekształć wyniki na etykiety binarne
                                # threshold = 0.0
                                threshold_idx = 10
                                predicted_labels = [1 if distance < sorted_distances[threshold_idx] else 0 for distance
                                                    in distances]

                                # Oblicz metryki
                                precision, recall, f1 = calculate_metrics(true_labels, predicted_labels)

                                # Zapisz wyniki
                                result = {
                                    'Query': query,
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
articles = pd.read_csv(f'{DIR_FILES}/{CSV_FILE}')
results_file = f'{TEST_FILE}'

# pd.set_option('display.max_colwidth', None)
# print(articles['title'])
# print(articles.loc[articles['title'] == 'Acute severe asthma'])

google_results = [
    {
        'query': 'asthma in children',
        'titles': {'Asthma', 'Epidemiology of asthma', 'Acute severe asthma', 'Asthma trigger', 'Allergies in children',
                   'Pathophysiology of asthma', 'Asthma-related microbes', 'Reactive airway disease', 'Bronchiolitis',
                   'Wheeze'}
    },
    {
        'query': 'asthma inhaler types',
        'titles': {'Inhaler', 'Dry-powder inhaler', 'Metered-dose inhaler', 'Salbutamol', 'Formoterol',
                   'Pulmonary drug delivery', 'Bronchodilator', 'Asthma', 'Budesonide/formoterol',
                   'Inhaler spacer'}
    }]

query_results = []

for result in google_results:
    query = result['query']
    google_results_titles = result['titles']
    query_results_titles = articles['title'].tolist()

    labels = tuple(map(lambda article_title: article_title in google_results_titles, query_results_titles))

    query_results.append({
        'query': query,
        'titles': query_results_titles,
        'labels': labels
    })

print(query_results[0]['titles'])
df_query_results = pd.DataFrame(query_results)

# df_google_results = pd.DataFrame(google_results)
# queries = df_google_results['query'].tolist()
# google_titles = df_google_results['titles'].tolist()
# articles = pd.read_csv(f'{DIR_FILES}/{CSV_FILE}')
# articles = articles['clean_content']

# Wywołaj funkcję do obliczania metryk dla różnych parametrów
calculate_metrics_for_parameters(df_query_results['query'].tolist(),
                                 df_query_results['labels'].tolist(),
                                 articles['clean_content'],
                                 output_file=results_file)
