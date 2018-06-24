# these should be the only imports you need
import tweepy
import nltk
from operator import itemgetter, attrgetter
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
import json
import sys
import csv
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter

#Name: John Robert Lint
#Umich uniqname: jrlint

consumer_key = "LlYTJdSpVZzxrlMUgs91jZMbT"
consumer_secret = "bn08ZbBfWQfdvCLDSeDBZh3yLgr0rDplhLvRaBrY8zS5lfuoyZ"
access_key = "1422052052-tDZfbfU2GlUJEnDbv3IYKLb4lFrvWFlNYi2UcXd"
access_secret = "hIDPRtgAaxGq4woKz6wNWXnQWUpHIzwsNlogSBzrQsFsd"


def access_tweets(user, num):
    authorize = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authorize.set_access_token(access_key, access_secret)

    api = tweepy.API(authorize)

    tweets = api.user_timeline(screen_name=user, count=num, tweet_mode='extended')

    return tweets


def each_tweet(tweet):
    words = word_tokenize(tweet)
    partofspeech = nltk.pos_tag(words)
    wordlist = []
    for word in words:
        w1 = word[0]
        if w1.isalpha() and not word.startswith('http') and not word.startswith('RT'):
            wordlist.append(word)
    partofspeech = nltk.pos_tag(wordlist)
    return partofspeech


def get_noun_list(list):
    nouns = []
    count = 0
    for x in list:
        val = x[0][1]
        val = val[:2]
        if val == 'NN':
            temp = [x[0][0], x[1]]
            nouns.append(temp)
            count += 1
    nouns.sort(key=lambda i: i[0].lower())
    nouns.sort(key=lambda i:i[1], reverse=True)

    top5 = nouns[:5]
    return top5


def get_adj_list(list):
    i = 0
    adjs = []
    count = 0
    for x in list:
        val = x[0][1]
        val = val[:2]
        if val == 'JJ':
            temp = [x[0][0], x[1]]
            adjs.append(temp)
            count += 1
    adjs.sort(key=lambda i: i[0].lower())
    adjs.sort(key=lambda i: i[1], reverse=True)

    top5 = adjs[:5]
    return top5


def get_verb_list(list):
    i = 0
    verbs = []
    count = 0
    for x in list:
        val = x[0][1]
        val = val[:2]
        if val == 'VB':
            temp = [x[0][0], x[1]]
            verbs.append(temp)
            count += 1
    verbs.sort(key=lambda i: i[0].lower())
    verbs.sort(key=lambda i: i[1], reverse=True)

    top5 = verbs[:5]
    return top5


def createCsv(nouns):
    with open('noun_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        data = [('Noun', 'Number')]
        writer.writerows(data)
        writer.writerows(nouns)



def main():
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    username = sys.argv[1]
    numTweets = sys.argv[2]
    words_from_all = []
    print("USER:", username)
    print("TWEETS ANALYZED:", numTweets)
    isRetweet = False
    tweets = access_tweets(username, numTweets)
    x=1
    numOriginal = 0
    numFavs = 0
    numRTs = 0
    for tweet in tweets:
        status = tweet
        if 'retweeted_status' in tweet._json:
            isRetweet = True
            finalTweet = tweet._json['retweeted_status']['full_text'].encode("ascii", "ignore").decode('ascii')

        else:
            finalTweet = tweet._json['full_text'].encode("ascii", "ignore").decode('ascii')
            numOriginal += 1
            numFavs += tweet._json['favorite_count']
            numRTs += tweet._json['retweet_count']
        isRetweet = False
        words_from_all.extend(each_tweet(finalTweet))

        words = tweet.full_text.encode("ascii", 'ignore').split()
        x += 1
    words_seen = Counter(words_from_all)
    words_seen = [v for v in sorted(words_seen.items(), key=lambda kv: (-kv[1], kv[0]))]
    verbs = get_verb_list(words_seen)
    print("VERBS: ", end='')
    for x in verbs:
        print(x[0], "(", x[1], ") ", end='', sep='')
    nouns = get_noun_list(words_seen)
    print()
    print("NOUNS: ", end='')
    for x in nouns:
        print(x[0], "(", x[1], ") ", end='', sep='')
    adjs = get_adj_list(words_seen)
    print()
    print("ADJECTIVES: ", end='')
    for x in adjs:
        print(x[0], "(", x[1], ") ", end='', sep='')
    print()
    print("ORIGINAL TWEETS:", numOriginal)
    print("TIMES FAVORITED (ORIGINAL TWEETS ONLY):", numFavs)
    print("TIMES RETWEETED (ORIGINAL TWEETS ONLY):", numRTs)
    createCsv(nouns)

if __name__ == "__main__":
    main()

# usage should be python3 part1.py <username> <num_tweets>
