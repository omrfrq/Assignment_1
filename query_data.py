from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db=client['Assignment']
collection = db['metadata']

print('For searching CONTENT press 1\n')
print('For searching METADATA press 2\n')
val=input("Enter your option=")
if int(val) == 1:

    content=input('Enter query for content=')
    query = {"content": content}
    result = collection.find(query)

    for output in result:
        print('\n',output)

else:

    content=input('Enter query for metadata=')
    query = {"content": content}
    result = collection.find(query)

    for output in result:
        print('\n',output)