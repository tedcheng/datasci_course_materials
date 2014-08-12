import sys
import json

# def hw():
#     print 'Hello, world!'

# def lines(fp):
#     print str(len(fp.readlines()))

def build_dict_from_sentiment_file(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def split_tweet_into_words(tweet):
    new_tweet = ""
    for letter in tweet.lower():
        if letter.isalpha():
            new_tweet += letter
        else:
            new_tweet += " "
    return new_tweet.split()

def compute_tweet_sentiment_score(sent_dict, tweet):
    words = split_tweet_into_words(tweet)
    score = 0
    for word in words:
        word_score = sent_dict.get(word)
        if word_score == None:
            score += 0
        else:
            score += word_score
    return score

# def extract_sentiment_scores_from_tweet_file(tweet_file, sent_dict):
#     for line in tweet_file:
#         tweet = json.loads(line).get("text")
#         if tweet == None:
#             print 0
#         else:
#             print compute_tweet_sentiment_score(sent_dict, tweet)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dict = build_dict_from_sentiment_file(sent_file)
    for line in tweet_file:
        tweet = json.loads(line).get("text")
        if tweet != None:
            print compute_tweet_sentiment_score(dict, tweet)

if __name__ == '__main__':
    main()
