from collections import Counter
from collections import OrderedDict
import matplotlib.pyplot as plt
import pymongo
from datetime import timezone, timedelta
import dateutil.parser


client = pymongo.MongoClient('localhost', 40001, retryWrites=False)
db = client['news-db']
news_collection = db['news']
pub_time_str_list = list(news_collection.find({}, {'publishedAt': 1}))
pub_hour_list = list()
time_delta = timedelta(hours=-4)
tz = timezone(time_delta)

for time_str in pub_time_str_list:
    pub_hour_list.append(int(dateutil.parser.parse(time_str['publishedAt']).astimezone(tz).hour))

counted_hours = Counter(pub_hour_list)
sorted_counted_hours = OrderedDict(sorted(counted_hours.items()))
# plt.bar(range(len(counted_hours)), list(counted_hours.values()), align='center')
# plt.xticks(range(len(counted_hours)), list(counted_hours.keys()))
# plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
ax.pie(sorted_counted_hours.values(), labels=sorted_counted_hours.keys(), autopct='%1.2f%%')
plt.show()
