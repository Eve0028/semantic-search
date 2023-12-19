import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from search_engine.parameters import TEST_RESULTS_DIR
from tests import google_results

pd.set_option('display.max_columns', None)
df_google_results = pd.DataFrame(google_results)


def plot_for_semantizator(df, semantizator):
    # Kombinacje kategorii do etykiet na osi x
    df['Combination'] = df['Tokenizer'] + ' ' + df['Similarity_Metric']

    max_precision_df = df.loc[df.groupby(['Tokenizer', 'Similarity_Metric'])['Precision'].idxmax()]
    min_num_topics_df = max_precision_df.loc[
        max_precision_df.groupby(['Tokenizer', 'Similarity_Metric'])['Num_Topics'].idxmin()]

    # Precision
    max_precision_df = min_num_topics_df[['Tokenizer', 'Similarity_Metric', 'Precision']]
    max_precision_df = max_precision_df.reset_index(drop=True)

    # Num_Topics
    min_num_topics_df = min_num_topics_df[['Tokenizer', 'Similarity_Metric', 'Num_Topics']]
    min_num_topics_df = min_num_topics_df.reset_index(drop=True)

    # Utworzenie wykresu
    fig, ax = plt.subplots(figsize=(12, 8))

    # Rysowanie słupków
    for i, row in max_precision_df.iterrows():
        combination = row['Tokenizer'] + ' ' + row['Similarity_Metric']
        min_num_topics = min_num_topics_df.loc[(min_num_topics_df['Tokenizer'] == row['Tokenizer']) & (
                min_num_topics_df['Similarity_Metric'] == row['Similarity_Metric']), 'Num_Topics'].values[0]

        ax.bar(i, row['Precision'], label=f'{combination}',
               color='lightblue' if row['Similarity_Metric'] == 'cosine' else 'purple')
        ax.text(i, row['Precision'] + 0.01, f'Topicki: {min_num_topics}', ha='center', va='center',
                fontsize=12, color='black', rotation=0)

    # Ustawienia wykresu
    ax.set_xticks(np.arange(len(max_precision_df)))
    plt.yticks(fontsize=12)
    ax.set_xticklabels(max_precision_df['Tokenizer'] + '+' + max_precision_df['Similarity_Metric'], fontsize=12,
                       rotation=10)
    ax.set_ylabel('Maksymalna precyzja', fontsize=12)
    ax.set_title(f'Najlepsze wyniki zapytania "{query}" dla {semantizator}', pad=40, fontsize=16)

    # Usunięcie górnej i prawej ramki
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    # Wyświetlenie wykresu
    plt.show()


for query in df_google_results['query'].tolist():
    results_file = f"{TEST_RESULTS_DIR}/results_{query.replace(' ', '_')}.csv"
    results = pd.read_csv(results_file)

    if query == 'asthma in children':
        filtered_results = results.loc[results['Precision'] > 0.5]
    elif query == 'asthma inhaler types':
        filtered_results = results.loc[results['Precision'] > 0.3]

    filtered_results_sorted = filtered_results.sort_values(['Precision', 'Num_Topics'], ascending=[False, True])

    print(f'\n\n{query}')
    # PCA
    # print(f'\nPCA')
    filtered_results_sorted_pca = filtered_results_sorted.loc[filtered_results_sorted['Semantizator'] == 'pca']
    # print(filtered_results_sorted_pca[['Tokenizer', 'Semantizator', 'Num_Topics', 'Similarity_Metric', 'Precision']])
    plot_for_semantizator(filtered_results_sorted_pca, 'PCA')

    # SVD
    # print(f'\nSVD')
    filtered_results_sorted_pca = filtered_results_sorted.loc[filtered_results_sorted['Semantizator'] == 'svd']
    # print(filtered_results_sorted_pca[['Tokenizer', 'Semantizator', 'Num_Topics', 'Similarity_Metric', 'Precision']])
    plot_for_semantizator(filtered_results_sorted_pca, 'SVD')

    # LDiA
    # print(f'\nLDiA')
    filtered_results_sorted_pca = filtered_results_sorted.loc[filtered_results_sorted['Semantizator'] == 'ldia']
    # print(filtered_results_sorted_pca[['Tokenizer', 'Semantizator', 'Num_Topics', 'Similarity_Metric', 'Precision']])
    plot_for_semantizator(filtered_results_sorted_pca, 'LDiA')
