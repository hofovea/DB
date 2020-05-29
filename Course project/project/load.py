import json

import pymongo
from bson import ObjectId
from newsapi import NewsApiClient

newsApiClient = NewsApiClient(api_key="193b65d9d7af40e5a26a62acda3e0bdc")
newsApiClient1 = NewsApiClient(api_key="4d2b7f89614f463b91d9310d81f09515")
newsApiClient3 = NewsApiClient(api_key="816339f5a5a748fa8c594881b8cd277e")
# sources = newsApiClient.get_sources(country='us')

sources = 'reddit-r-all,reuters,politico,nfl-news,new-york-magazine,next-big-future,nbc-news,national-geographic'
sources1 = 'cnn,abc-news,associated-press,buzzfeed,new-scientist,wired,vice-news,usa-today,time'
sources3 = 'mtv-news,msnbc,medical-news-today,ign,hacker-news,google-news,fox-sports,fox-news'

client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

inserts_count = 0

all_articles = list()
day = 27
month = 4
for i in range(0, 15):
    if day == 31:
        month = month + 1
        day = day - 30
    for hour in range(0, 4):
        print(month)
        print(day)
        print(hour)
        time_start_str = ''
        time_end_str = ''
        if day > 9:
            if hour == 0:
                time_start_str = '2020-0{}-{}T00:00:00'.format(month, day)
                time_end_str = '2020-0{}-{}T06:00:00'.format(month, day)
            if hour == 1:
                time_start_str = '2020-0{}-{}T06:00:00'.format(month, day)
                time_end_str = '2020-0{}-{}T12:00:00'.format(month, day)
            if hour == 2:
                time_start_str = '2020-0{}-{}T12:00:00'.format(month, day)
                time_end_str = '2020-0{}-{}T18:00:00'.format(month, day)
            if hour == 3:
                time_start_str = '2020-0{}-{}T18:00:00'.format(month, day)
                time_end_str = '2020-0{}-{}T00:00:00'.format(month, day)
        else:
            if hour == 0:
                time_start_str = '2020-0{}-0{}T00:00:00'.format(month, day)
                time_end_str = '2020-0{}-0{}T06:00:00'.format(month, day)
            if hour == 1:
                time_start_str = '2020-0{}-0{}T06:00:00'.format(month, day)
                time_end_str = '2020-0{}-0{}T12:00:00'.format(month, day)
            if hour == 2:
                time_start_str = '2020-0{}-0{}T12:00:00'.format(month, day)
                time_end_str = '2020-0{}-0{}T18:00:00'.format(month, day)
            if hour == 3:
                time_start_str = '2020-0{}-0{}T18:00:00'.format(month, day)
                time_end_str = '2020-0{}-0{}T00:00:00'.format(month, day)

        print(time_start_str)
        print(time_end_str)
        all_articles = all_articles + \
                       newsApiClient1.get_everything(sources=sources, from_param=time_start_str, language='en',
                                                    to=time_end_str, page_size=100,
                                                    sort_by='popularity')['articles']
        all_articles = all_articles + \
                       newsApiClient1.get_everything(sources=sources1, from_param=time_start_str, language='en',
                                                    to=time_end_str, page_size=100,
                                                    sort_by='popularity')['articles']
        all_articles = all_articles + \
                       newsApiClient3.get_everything(sources=sources3, from_param=time_start_str, language='en',
                                                    to=time_end_str, page_size=100,
                                                    sort_by='popularity')['articles']
        for item in all_articles:
            if news_collection.count_documents({ "title": (item['title']) }) == 0:
                news_collection.insert_one(item)
                inserts_count = inserts_count + 1

    day = day + 1

# file = open('data/data.json', 'w')
# file.write(json.dumps(all_articles, indent=4))
# file.close()
#
# print(len(all_articles))

client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

inserts_count = 0
for item in all_articles:
    if news_collection.count_documents({"title": (item['title'])}) == 0:
        news_collection.insert_one(item)
        inserts_count = inserts_count + 1

print('Loaded {} items'.format(inserts_count))
