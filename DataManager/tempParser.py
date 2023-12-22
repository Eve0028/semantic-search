import xml.etree.ElementTree as ET
import re
import csv

from DataManager.MongoDBManager import MongoDBManager
from search_engine.parameters import XML_FILE, DIR_FILES, CSV_FILE

WIKI = {'mw': 'http://www.mediawiki.org/xml/export-0.10/'}


def parse_wikipedia_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    articles = []

    for page in root.findall('.//mw:page', WIKI):
        title = page.find('.//mw:title', WIKI).text
        content = page.find('.//mw:text', WIKI).text

        articles.append({
            'title': title,
            'content': content
        })

    return articles


def preprocess_article(text):
    # Usuń referencje w <ref></<ref> tags
    text = re.sub(r"<ref>.*?</ref>", '', text)

    # Usuń oznaczenia w formie {{...}}
    text = re.sub(r'\{\{.*?\}\}', '', text, flags=re.DOTALL)

    # Usuń tagi HTML
    text = re.sub(r'<.*?>', '', text)

    # Usuń wszystko po References, See also, External links
    text = re.sub(r'==\s*References\s*==.*', '', text, flags=re.DOTALL)
    text = re.sub(r'==\s*External links\s*==.*', '', text, flags=re.DOTALL)
    text = re.sub(r'==\s*See also\s*==.*', '', text, flags=re.DOTALL)

    # Usuń sekcje kategorii
    text = re.sub(r'\[\[Category:.*?\]\]', '', text)

    # Usuń == z tytułów
    text = re.sub(r'==', '', text, flags=re.DOTALL)

    # Usuń oznaczenia w formie [[...]], zachowując tytuł i opis zdjęcia
    text = re.sub(r'\[\[File:(?P<title>.*?)\(\d+\).jpg\|thumb\|\[(?P<description>.*?)\]\]',
                  lambda match: f'{match.group("title")} {match.group("description")}', text)

    # Usuń oznaczenia w formie [[...|...]], zachowując tylko drugie wyrażenie po '|'
    text = re.sub(r'\[\[(?P<term>.*?)\|(?P<word>.*?)\]\]', lambda match: match.group("word"), text)

    # Usuń pozostałe nawiasy kwadratowe
    text = re.sub(r'\[', '', text)
    text = re.sub(r']', '', text)

    # Usuń __TOC__
    text = re.sub(r'__TOC__', '', text)

    # Usuń znaczniki wokół textu '''text'''
    text = re.sub(r"'''", '', text)

    return text.strip()


def get_parsed_articles(xml_file_path):
    parsed_articles = parse_wikipedia_xml(xml_file_path)
    for parsed_article in parsed_articles:
        parsed_article['clean_content'] = preprocess_article(parsed_article['content'])
    # cleaned_articles = [preprocess_article(parsed_article['content']) for parsed_article in parsed_articles]
    return parsed_articles


def parse_articles_to_mongodb(xml_file, database_name, collection_name, host='localhost', port=27017):
    mongo_db_manager = MongoDBManager(database_name, collection_name, host, port)
    parsed_articles = get_parsed_articles(xml_file)

    for parsed_article in parsed_articles:
        mongo_db_manager.insert_data(parsed_article['title'], parsed_article['content'], parsed_article['clean_content'])

    #mongo_db_manager.close_connection()


def dicts_to_csv(dicts, name_of_file):
    exclude_key = 'content'
    [dicti.pop(exclude_key, None) for dicti in dicts]
    # new_dict = {k: dicts[k] for k in set(list(dicts.keys())) - set(exclude_keys)}
    keys = dicts[0].keys()

    with open(name_of_file, 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dicts)


def parse_articles_to_csv(xml_file=f'{DIR_FILES}/{XML_FILE}', csv_file=f'{DIR_FILES}/{CSV_FILE}'):
    parsed = get_parsed_articles(xml_file)
    dicts_to_csv(parsed, csv_file)


# Parse and save new articles to csv
parse_articles_to_csv()


xml_file_path = 'asthma_40.xml'
database_name = 'semantic_search'
collection_name = 'articles'

# Parse and save new articles to Mongo
# parse_articles_to_mongodb(xml_file_path, database_name, collection_name)
