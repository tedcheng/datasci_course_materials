import sys
import json
import operator

def lookup_hash_tags_from_tweet(tweet_file_line):
    tags = []
    entities = json.loads(tweet_file_line).get("entities")
    if entities != None:
        hashtags = entities.get("hashtags")
        if hashtags != None:
            for tag in hashtags:
                tags.append(tag.get("text"))
    return tags

def main():
    tweet_file = open(sys.argv[1])
    dict = {}
    for line in tweet_file:
        tags = lookup_hash_tags_from_tweet(line)

        for tag in tags:
            tag_count = dict.get(tag)
            if tag_count != None:
                dict[tag] += 1
            else:
                dict[tag] = 1

    top_ten = sorted(dict.iteritems(), key=operator.itemgetter(1), reverse=True)[0:10]
    
    for tag, count in top_ten:
        print tag, count

if __name__ == '__main__':
    main()