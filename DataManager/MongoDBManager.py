from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, database_name, collection_name, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def insert_data(self, data):
        self.collection.insert_one({'klucz': data})

    def close_connection(self):
        self.client.close()