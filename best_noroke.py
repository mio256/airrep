import os
import tweepy
import datetime

hanya = 1511906485349265415

client = tweepy.Client(
    os.environ['BEARER_TOKEN'],
    os.environ['CONSUMER_KEY'],
    os.environ['CONSUMER_SECRET'],
    os.environ['ACCESS_TOKEN'],
    os.environ['ACCESS_TOKEN_SECRET']
)

best_id = 0
best_score = 0
now = datetime.datetime.now()

for users_tweets in tweepy.Paginator(
    client.get_users_tweets,
    id=hanya,
    exclude=['retweets', 'replies'],
    tweet_fields=['public_metrics'],
    max_results=100,
    start_time=now-datetime.timedelta(days=1)
):
    for tweet in users_tweets.data:
        if '彼女' in tweet.text:
            score = tweet.public_metrics['retweet_count'] * 5
            score += tweet.public_metrics['reply_count'] * 3
            score += tweet.public_metrics['like_count'] * 2
            score += tweet.public_metrics['quote_count'] * 7
            if score > best_score:
                best_score = score
                best_id = tweet.id

if best_id !=0:
    text = '↓直近24時間で一番伸びた惚気ツイート {}↓'.format(datetime.datetime.now())
    client.create_tweet(text=text, quote_tweet_id=best_id)
else:
    print('error')
