import pymongo
from save import save

save()

client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

news_collection.delete_many({ })
