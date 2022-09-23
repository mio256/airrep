import os
import tweepy
import datetime

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET']
)

noroke = {}

for users_tweets in tweepy.Paginator(
    client.get_users_tweets,
    id=1511906485349265415,
    exclude=['retweets', 'replies'],
    tweet_fields=['public_metrics'],
    max_results=100,
    start_time=datetime.datetime.now() - datetime.timedelta(days=1)
):
    for tweet in users_tweets.data:
        if '彼女' in tweet.text:
            score = tweet.public_metrics['retweet_count'] * 5
            score += tweet.public_metrics['reply_count'] * 3
            score += tweet.public_metrics['like_count'] * 2
            score += tweet.public_metrics['quote_count'] * 7
            print(tweet.id, score)
            noroke[tweet.id] = score

best_id = sorted(noroke.items(), key=lambda x: -x[1])[0][0]
text = '↓直近24時間で一番伸びた惚気ツイート {}↓'.format(datetime.datetime.now())

client.create_tweet(text=text, quote_tweet_id=best_id)
