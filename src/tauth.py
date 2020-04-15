import tsecrets
import tweepy

def get_api():
    auth = tweepy.OAuthHandler(tsecrets.consumer_key, tsecrets.consumer_secret)
    auth.set_access_token(tsecrets.access_token, tsecrets.access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    if(api.verify_credentials):
        print("Logged In Successfully")
    else:
        print("Error -- Could not log in with your credentials")
    
    return api
    