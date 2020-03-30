from __future__ import absolute_import, print_function

import tweepy
import sys
import codecs
import Secrets

auth = tweepy.OAuthHandler(Secrets.consumer_key, Secrets.consumer_secret)
auth.set_access_token(Secrets.access_token, Secrets.access_token_secret)

api = tweepy.API(auth)

print(api.me().name)

owner = "HlidacStatu"
slug = "cz-politici"
api.list_members(owner, slug)

print()

# Get all politics from list
for member in tweepy.Cursor(api.list_members, 'HlidacStatu', 'cz-politici').items():
    print(member.screen_name)


# Get all tweets of one politic and find all mentions and retweets

# Construct network 

# Export network to file
