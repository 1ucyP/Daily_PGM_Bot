import tweepy

#authenticate bot using API Credentials (NOTE: will not work until I get developer access)
auth = tweepy.OAuthHandler("your_api_key", "your_api_secret_key")
auth.set_access_token("your_access_token", "your_access_token_secret")

# Create an instance of the Tweepy API
api = tweepy.API(auth)


