import re

class DataCleaner:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.cleaned_data = None

    def clean_data(self):
        cleaned_text = self.clean_text(self.raw_data)

        self.cleaned_data = cleaned_text

    @staticmethod
    def clean_text(text):
        # Usuwanie HTML Tags
        cleaned_text = re.sub(r'<.*?>', '', text)

        # Usuwanie linków
        cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)

        # Usuwanie specjalnych znaków
        cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', cleaned_text)

        # Usuwanie znaków niealfanumerycznych (za wyjątkiem spacji)
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)

        # Zamiana wielu spacji na jedną
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

        return cleaned_text

