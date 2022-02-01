import tweepy
from src.utils import read_yaml

config = read_yaml(r"./config.yaml")

app_api_key = config["keys"]["api_key"]
app_api_secret_key = config["keys"]["api_secret_key"]

auth = tweepy.AppAuthHandler(app_api_key, app_api_secret_key)
api = tweepy.API(auth)

print(f"API Host: {api.host}")
try:
    api.verify_credentials()
except tweepy.errors.Forbidden:
    print("Error during authentication")

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# search_term = 'bayes'
# tweets = tweepy.Cursor(api.search_30_day(label='tweets', query=search_term))

# retreived_tweets = [tweet.text for tweet in tweets]
# df = pd.json_normalize(retreived_tweets)

# tweets = tw.Cursor(api.search,
#               q=search_query,
#               lang="en",
#               since="2020-09-16").items(50)
