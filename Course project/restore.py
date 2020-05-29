import pymongo
from bson.json_util import loads
from bson.objectid import ObjectId

# from validate import validate

file = open('data/news-db_save.json', 'r')
str = file.read()

# items = validate('_id', loads(str))

items = loads(str)
print(len(items))

client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

inserts_count = 0
for item in items:
    if news_collection.count_documents({ "_id": ObjectId(item['_id']) }) == 0:
        news_collection.insert_one(item)
        inserts_count = inserts_count + 1

print('Loaded {} items'.format(inserts_count))
