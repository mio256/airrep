import os
import pprint
import json
import tweepy


client = tweepy.Client(os.environ['BEARER_TOKEN'], wait_on_rate_limit=True)

cnt = 0
all = 0

for users_tweets in tweepy.Paginator(
    client.get_users_tweets,
    id=1511906485349265415,
    exclude=['retweets', 'replies'],
    max_results=100,
):
    for tweet in users_tweets.data:
        all += 1
        if '彼女' in tweet.text:
            cnt += 1

print('{}/{}'.format(cnt, all))
