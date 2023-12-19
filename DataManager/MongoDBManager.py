from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, database_name, collection_name, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert_data(self, title, content, clean_content):
        data = {
            'title': title,
            'content': content,
            'clean_content': clean_content
        }
        self.collection.insert_one(data)


    def close_connection(self):
        self.client.close()