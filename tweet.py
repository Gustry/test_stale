import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "X9sK8ww3caNbl5CcROp2b8x8M")
auth.set_access_token("ACCESS_TOKEN", "1381813333037174788-qS3AiR2NBa12OcgzwpKwif36WwEq2V")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
