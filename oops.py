import tweepy
import json

#stream listener
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        if tweet.author.id != 799767920117161984:
            print(f"{tweet.user.name}:{tweet.text}")
            api.create_favorite(tweet.id)
            author = tweet.author.screen_name
            api.update_status(status="@" + author + " i liked", in_reply_to_status_id=tweet.id)

    def on_error(self, status):
        print("Error detected")
        if status_code == 420:
            return False

#LISTING CREDENTIALS
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#test credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#opens stream and filters for friend's tweets
followers = []
for i in api.followers_ids("TWITTER_HANDLE", stringify_ids = True):
    followers.append(i)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow = followers, is_async=True)
