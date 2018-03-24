
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime


# In[2]:


# Twitter API Keys
consumer_key = "1hQy7DJNH57HcwzyQwN4QIb7g"
consumer_secret = "Lwj0L5UrqL4RCj5wIaOP2aAGda1NLyAotWRQiVCanS64MTPX0Y"
access_token = "1668216486-awjRspu2pN8Bhd4l5dbXtkr3K7g6ZVXUK1ygo6a"
access_token_secret = "RGHGIaE3Y0WFHx2S9OcB9J7VFytIyhLZ8GzxNtaXmfvHy"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[ ]:


# Send tweets every 60 Seconds to your homepage
tweet_num = 1
while tweet_num < 6:
    api.update_status("Tweet Number :" + str(time.ctime()) + "counter: " + str(tweet_num))
    tweet_num = tweet_num + 1
    time.sleep(60)

