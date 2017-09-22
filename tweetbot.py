import random

import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# i = 0
# api.followers
# for follower in tweepy.Cursor(api.friends).items(0):
#     i += 1
#     if i % 100 == 0:
#         time.sleep(300)
#         print(i)
#     print(follower.screen_name)
# print(i)

"""
followers = api.followers_ids()
friends = api.friends_ids()

for friend in friends:
    if friend not in followers:
        print("Unfollow {0}?".format(api.get_user(friend).screen_name))
        api.destroy_friendship(friend)
"""

"""
Кого читает юзер
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="l4OyPgvx8hOc18S").pages():
    ids.extend(page)
    #time.sleep(60)

screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
print(len(screen_names))
print(screen_names)
"""

followers = api.followers_ids()
friends = api.friends_ids()
other_friends = api.followers_ids(screen_name="VysotskyQuote")

ids = []
n = 0

# for page in tweepy.Cursor(api.followers_ids, screen_name="VysotskyQuote").pages():
#     if page not in followers and id not in friends:
#         ids.extend(page)
#         n += 1
#         if n == 10:
#             break
#

# for id in other_friends:
#     if id not in followers and id not in friends:
#         if len(api.followers_ids(user_id=id)) > 20:
#             api.create_friendship(id)
#             print("Follow {0}".format(api.get_user(id).screen_name))



for friend in friends:
    if friend not in followers:
        api.destroy_friendship(friend)
        print("Unfollow {0}".format(api.get_user(friend).screen_name))
        #time.sleep(random.randint(1, 3))