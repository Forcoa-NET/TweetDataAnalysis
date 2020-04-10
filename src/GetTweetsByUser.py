import tweepy
import sys
import codecs
import Secrets
import datetime
import time

auth = tweepy.OAuthHandler(Secrets.consumer_key, Secrets.consumer_secret)
auth.set_access_token(Secrets.access_token, Secrets.access_token_secret)
api = tweepy.API( auth_handler = auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# In this example, the handler is time.sleep(15 * 60),
# but you can of course handle it in any way you want.


def getPersonTweets( personTwitterName ):
    save_file = open('Data/'+personTwitterName+'.txt','a',encoding='utf-8-sig',newline='')

    url = "https://t.co/"

    for status in tweepy.Cursor(api.user_timeline, screen_name = personTwitterName, tweet_mode="extended", include_rts = False).items():
        text = status.full_text
        date = status.created_at
        
        if ( text.rfind(url) > -1 ) :
            parsedText = text[:text.rfind(url)]
            parsedText = parsedText.replace("\n", "")
        else :
            parsedText = text.replace("\n", "")

        # print(parsedText)
        save_file.write( date.strftime('%m/%d/%Y') + ";" + parsedText + "\n")

    save_file.close() 
    return

# use file FakeTargets for test
# file = open('Data/Targets.txt', 'r') 
# for line in file: 
    #getPersonTweets(line.rstrip('\n')) 

getPersonTweets('@jakubplesnik') 

