import sys
import json
import operator

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

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_dict = build_dict_from_sentiment_file(sent_file)
    state_scores = {}
    for line in tweet_file:
        line_object = json.loads(line)
        tweet = line_object.get("text")
        place = line_object.get("place")
        if (tweet != None) and (place != None):
            country = place.get("country")
            place_type = place.get("place_type")
            name = place.get("full_name")
            if (country == "United States") and (place_type == "city"):
                score = compute_tweet_sentiment_score(sent_dict, tweet)
                state = name[-2:]
                if state_scores.get(state) == None:
                    state_scores[state] = [score]
                else:
                    state_scores[state].append(score)
    
    state_score = {}
    for state, scores in state_scores.items():
        avg_score = sum(scores)/len(scores)
        # print state, avg_score
        state_score[state] = avg_score

    happiest_state = sorted(state_score.iteritems(), key=operator.itemgetter(1), reverse=True)[0:1]
    print happiest_state[0][0]

if __name__ == '__main__':
    main()
