import sys
import json
from collections import Counter


def main():
    tweet_data = open(sys.argv[1])
    hashtags_set = {}
    for line in tweet_data:
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            hashtags_per_line = entities["hashtags"]

            for hashtag in hashtags_per_line:
                text = hashtag["text"]
                if text in hashtags_set.keys():
                    hashtags_set[text] += 1
                else:
                    hashtags_set[text] = 1

    sorted_hashtags = Counter(hashtags_set)
    top_ten = sorted_hashtags.most_common(10)
    for top in top_ten:
        print(top[0] + " " + str(top[1]))


if __name__ == '__main__':
    main()
