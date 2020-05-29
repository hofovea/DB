from collections import Counter
import matplotlib.pyplot as plt
import pymongo
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

stop_words = set(stopwords.words('english'))

client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']

news_list = list(news_collection.find({ }, { 'title': 1, 'description': 1 }))
print(len(news_list))
words_str = ''
for article in news_list:
    if article['description'] is not None:
        words_str = ' '.join([words_str, article['description']])
    if article['title'] is not None:
        words_str = ' '.join([words_str, article['title']])

words_list = word_tokenize(words_str)
valid_words_list = list()
for word in words_list:
    if word.isalnum() and word not in stop_words and len(word) > 4:
        valid_words_list.append(word)
words_count = Counter(valid_words_list)

print(len(words_count.keys()))
top_words = words_count.most_common(15)

top_words_dict = { }
for word in top_words:
    top_words_dict.update({ word[0]: word[1] })

plt.bar(range(len(top_words_dict)), list(top_words_dict.values()), align='center')
plt.xticks(range(len(top_words_dict)), list(top_words_dict.keys()))
plt.show()
