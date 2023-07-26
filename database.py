from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db=client['Assignment']
collection = db['metadata']

def insert_and_index(content, metadata):

    count=len(content)
    for x in range(count):
        
        cont=content[x]
        meta=metadata[x]
        for key, val in meta.items():
            if key == "resourceName":
                filename=val

        data = {
        'filename': filename,
        'content': cont,
        'metadata': meta,
        }
        collection.insert_one(data)

    collection.create_index("filename") 
    collection.create_index([("content","text")])  
    collection.create_index("metadata")





