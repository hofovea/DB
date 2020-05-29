from collections import Counter
import sys

import dateutil.parser
import matplotlib.pyplot as plt
import pymongo
from nltk import word_tokenize

word_to_analyze = 'coronavirus'

if len(sys.argv) > 1:
    word_to_analyze = sys.argv[1]


client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

news_list = list(news_collection.find({ }, { 'source.id': 1, 'publishedAt': 1 }))

day_pub_list = []
for day in news_list:
    day_pub_list.append((dateutil.parser.parse(day['publishedAt']).date()))

day_counter = Counter(day_pub_list)
dates_l = day_counter.keys()
# print(sorted(dates_l))
key_occurrence_per_day_d = { }

for date in dates_l:
    list_w_key_word = []
    if int(date.day) == 30:
        list_w_key_word = list(
            news_collection.find(
                { "publishedAt": { "$gt": "2020-{:02d}-{:02d}T00:00:00".format(int(date.month), int(date.day)),
                                   "$lt": "2020-05-01T00:00:00" } }, { 'title': 1, 'description': 1 }))
    else:
        list_w_key_word = list(
            news_collection.find(
                { "publishedAt": { "$gt": "2020-{:02d}-{:02d}T00:00:00".format(int(date.month), int(date.day)),
                                   "$lt": "2020-{:02d}-{:02d}T00:00:00".format(int(date.month),
                                                                               int(date.day) + 1) } },
                { 'title': 1, 'description': 1 }))
    str_to_analyze = ''
    for article in list_w_key_word:
        if article['description'] is not None:
            str_to_analyze = ' '.join([str_to_analyze, article['description']])
        if article['title'] is not None:
            str_to_analyze = ' '.join([str_to_analyze, article['title']])
    words_list = word_tokenize(str_to_analyze)
    print(words_list.count(word_to_analyze))
    if words_list.count(word_to_analyze) != 0:
        key_occurrence_per_day_d.update({ date: words_list.count(word_to_analyze) })

print(key_occurrence_per_day_d)

for key in key_occurrence_per_day_d.keys():
    print(key_occurrence_per_day_d[key])


plt.plot(list(key_occurrence_per_day_d.keys()), list(key_occurrence_per_day_d.values()))
plt.show()