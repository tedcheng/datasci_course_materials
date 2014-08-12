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
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    old_dict = build_dict_from_sentiment_file(sent_file)
    new_dict = {}
    for line in tweet_file:
        tweet = json.loads(line).get("text")
        if tweet != None:
            score = compute_tweet_sentiment_score(old_dict, tweet)
            count = count_sentiment_words(old_dict, tweet)
            if count != 0:
              avg_term_score = float(score) / float(count)
            else:
              avg_term_score = 0

            terms = split_tweet_into_words(tweet)
            for term in terms:
                if old_dict.get(term) == None:
                    if new_dict.get(term) == None:
                        new_dict[term] = [avg_term_score]
                    else:
                        new_dict.get(term).append(avg_term_score)

    for term, scores in new_dict.items():        
        # avg_score = float(sum(scores))/len(scores)
        # line = term + " " + avg_score 
        print term, float(sum(scores))/len(scores)

if __name__ == '__main__':
    main()
