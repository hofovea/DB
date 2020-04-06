import sys
import json
import re


def main():
    mood_score_data = open(sys.argv[1])

    mood_scores = {}
    for line in mood_score_data:
        word_set, score = line.split("\t")
        mood_scores[word_set] = int(score)

    tweet_data = open(sys.argv[2])
    for line in tweet_data:
        tweet = json.loads(line)
        if "text" in tweet:
            tweet_text = tweet["text"]
            splitted_text = re.split(r"[\s\.,\?\:]+", tweet_text)
            mood_score = 0

            for word in splitted_text:
                if word in mood_scores:
                    mood_score = mood_score + mood_scores[word]

            print(mood_score)


if __name__ == '__main__':
    main()
