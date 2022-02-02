"""
# Extracting twitter data

Uses package tweepy (v4.5.0).

Note that Twitter API was recently updated, and articles like
[this one](https://realpython.com/twitter-bot-python-tweepy/)
are now probably out of date?

References:
    - https://dev.to/twitterdev/a-comprehensive-guide-for-using-the-twitter-api-v2-using-tweepy-in-python-15d9  # noqa


"""

import tweepy
from src.utils import read_yaml
import pandas as pd

config = read_yaml(r"./config.yaml")

bearer_token = config["tokens"]["bearer_token"]

client = tweepy.Client(bearer_token=bearer_token)

query = "from:baddatasciencer"

tweets = client.search_recent_tweets(
    query=query,
    tweet_fields=["context_annotations", "created_at"],
    max_results=100,  # noqa
)


for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)


df_tweets = pd.DataFrame({"tweet_text": tweets.data})
# df_tweets.head()  # todo: why StopIteration exception?
