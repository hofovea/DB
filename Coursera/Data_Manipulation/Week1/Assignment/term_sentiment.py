import sys
import json
import re


def main():
    mood_score_data = open(sys.argv[1])

    mood_scores = {}  # initialize an empty dictionary
    for line in mood_score_data:
        word_set, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        mood_scores[word_set] = int(score)  # Convert the score to an integer.

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

            for word in splitted_text:
                if word not in mood_scores:
                    print(word + " " + str(mood_score))


if __name__ == '__main__':
    main()
