import pymongo
from bson.json_util import dumps

client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

items = list(news_collection.find({ }))

items_str = dumps(items, indent=4)

file = open('data/news-db_save.json', 'w')
file.write(items_str)
file.close()
print('Saved {} items into [news-db_save.json]'.format(len(items)))


def save():
    save_file = open('data/news-db_save.json', 'w')
    save_file.write(items_str)
    save_file.close()
    print('Saved {} items into [news-db_save.json]'.format(len(items)))


save()
