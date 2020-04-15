from __future__ import absolute_import, print_function

import tweepy
import sys
import codecs
import tauth

api = tauth.get_api()

owner = "HlidacStatu"
slug = "cz-politici"
api.list_members(owner, slug)

network = {}
uniqueEntities = dict()
targets = []

# Get all politics from list
print("Requesting list of politics")
for member in tweepy.Cursor(api.list_members, 'HlidacStatu', 'cz-politici').items():
    targets.append(member.screen_name)
    network[member.screen_name] = []
    if member.screen_name not in uniqueEntities:
        uniqueEntities[member.screen_name] = len(uniqueEntities.items())

print("Requesting list of politics")
# Contruct network of mentions
for target in targets:
    print(str(uniqueEntities[target]) + " - Requesting data for the user: " + target)
    try:
        for status in tweepy.Cursor(api.user_timeline, screen_name=target, tweet_mode="extended", include_rts = False, count=100).items():
            if len(status.entities['user_mentions']) > 0:
                for mention in status.entities['user_mentions']:
                    network[target].append(mention['screen_name'])
                    if mention['screen_name'] not in uniqueEntities:
                        uniqueEntities[mention['screen_name']] = len(uniqueEntities.items())
    except tweepy.TweepError as e:
        print("Error during processing tweets of " + target)
        continue


print("Savign to file")
# Export network to file
save_file = open('Data/nodes.csv', 'a', encoding='utf-8-sig', newline='')
for k, v in network.items():
    line = str(uniqueEntities[k]) + ";" + k + "\n"
    save_file.write(line)
save_file.close()

save_file = open('Data/edges.csv', 'a', encoding='utf-8-sig', newline='')
for k, v in network.items():
    exported = []
    for neighbour in v:
        if neighbour not in exported and neighbour in network:
            line = str(uniqueEntities[k]) + ";" + str(uniqueEntities[neighbour]) + ";" + str(v.count(neighbour)) + "\n"
            exported.append(exported)
            save_file.write(line)

save_file.close()
