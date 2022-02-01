import tweepy
from src.utils import read_yaml

config = read_yaml(r"./config.yaml")

app_api_key = config["keys"]["api_key"]
app_api_secret_key = config["keys"]["api_secret_key"]

auth = tweepy.AppAuthHandler(app_api_key, app_api_secret_key)
api = tweepy.API(auth)

print(f"API Host: {api.host}")

# tweets = tweepy.Cursor(api.search, )
