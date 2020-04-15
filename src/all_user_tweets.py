import tweepy
import sys
import codecs
import datetime
import time
import tauth

def parseTweet( tweet ):
    url = "https://t.co/"
    text = tweet.full_text
    date = tweet.created_at
    
    if ( text.rfind(url) > -1 ) :
        parsedText = text[:text.rfind(url)]
        parsedText = parsedText.replace("\n", "")
    else :
        parsedText = text.replace("\n", "")

    return date.strftime('%m/%d/%Y') + ";" + parsedText + "\n"

def getPersonTweets( personTwitterName, api ):
    
    tweetLines = []
    lastId = 1209235491503169536

    if lastId == 0:
        for status in tweepy.Cursor(api.user_timeline, screen_name = personTwitterName, tweet_mode="extended", include_rts = False, count = 200).items():
            # print(parsedText)
            tweetLines.extend(parseTweet(status))
            lastId = status.id
            print("Last tweet = " + str(lastId))
    else:
        for status in tweepy.Cursor(api.user_timeline, screen_name = personTwitterName, tweet_mode="extended", include_rts = False, count = 200, max_id=lastId).items():
            # print(parsedText)
            tweetLines.extend(parseTweet(status))
            lastId = status.id
            print("Last tweet = " + str(lastId))

    save_file = open('Data/'+personTwitterName+'.txt', 'a', encoding='utf-8-sig', newline='')
    for line in tweetLines:
        save_file.write(line)

    save_file.close()
    pass

if __name__ == '__main__':
# use file FakeTargets for test
    api = tauth.get_api()
    file = open('Data/Targets.txt', 'r') 
    for line in file: 
        getPersonTweets(line.strip('\n'), api) 

