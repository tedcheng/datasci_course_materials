import sys
import json

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

def count_sentiment_words(sent_dict, tweet):
    words = split_tweet_into_words(tweet)
    count = 0
    for word in words:
        word_score = sent_dict.get(word)
        if word_score == None:
            count += 0
        else:
            count += 1
    return count

def main():
    tweet_file = open(sys.argv[1])
    dict = {}
    for line in tweet_file:
        tweet = json.loads(line).get("text")
        if tweet != None:
            terms = split_tweet_into_words(tweet)
            for term in terms:
                if dict.get(term) == None:
                    dict[term] = 1
                else:
                    dict[term] += 1
    
    total_occurs = 0
    for term, occurances in dict.items():
        total_occurs += occurances

    for term, occurances in dict.items():        
        # avg_score = float(sum(scores))/len(scores)
        # line = term + " " + avg_score 
        print term, float(occurances)/float(total_occurs)

if __name__ == '__main__':
    main()