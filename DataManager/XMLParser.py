import xml.etree.ElementTree as ET
class XMLParser:
    def __init__(self, file_path):
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()

    def extract_data(self):
        data_list = []

        for element in self.root.iter('element'):
            data = {}
            data['attribute'] = element.get('attribute_name')
            data['text_content'] = element.text
            data_list.append(data)

        return data_list