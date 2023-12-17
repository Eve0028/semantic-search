import xml.etree.ElementTree as ET
import re


NAMESPACE = {'mw': 'http://www.mediawiki.org/xml/export-0.10/'}


def parse_wikipedia_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    articles = []

    for page in root.findall('.//mw:page', NAMESPACE):
        title = page.find('.//mw:title', NAMESPACE).text
        content = page.find('.//mw:text', NAMESPACE).text

        articles.append({
            'title': title,
            'content': content
        })

    return articles


# Przykład użycia
xml_file_path = 'asthma_7.xml'
parsed_articles = parse_wikipedia_xml(xml_file_path)


def preprocess_article(text):
    # Usuń referencje w <ref></<ref> tags
    text = re.sub(r"<ref>.*?</ref>", '', text)

    # Usuń oznaczenia w formie {{...}}
    text = re.sub(r'\{\{.*?\}\}', '', text, flags=re.DOTALL)

    # Usuń tagi HTML
    text = re.sub(r'<.*?>', '', text)

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


# Przykład użycia
article_text = parsed_articles[0]['content']
cleaned_text = preprocess_article(article_text)
print(cleaned_text)
