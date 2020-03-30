import tweepy
import sys
import codecs
import Secrets

auth = tweepy.OAuthHandler(Secrets.consumer_key, Secrets.consumer_secret)
auth.set_access_token(Secrets.access_token, Secrets.access_token_secret)
api = tweepy.API(auth)

save_file = open('Data/AndrejBabis.txt','a',encoding='utf-8-sig',newline='')

url = "https://t.co/"

for status in tweepy.Cursor(api.user_timeline, screen_name='@AndrejBabis', tweet_mode="extended", include_rts = False).items():
    text = status.full_text
    
    if ( text.rfind(url) > -1 ) :
        parsedText = text[:text.rfind(url)]
        parsedText = parsedText.replace("\n", "")
    else :
        parsedText = text.replace("\n", "")

    # print(parsedText)
    save_file.write(parsedText + "\n")

save_file.close() 