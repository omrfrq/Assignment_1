from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db=client['Assignment']
collection = db['metadata']

search_query =input("Search query=")
results = collection.find({"$text": {"$search": search_query}})
for result in results:
    print('\n',result)