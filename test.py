
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


# Weather API
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"

# Create a function that gets the weather in London and Tweets it
def WeatherTweet():
    """Get Weather in London and Tweet it out."""
    # @TODO: Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    cities = ["London", "Paris", "Shanghai", "Boston", "Moscow"]
    units = "imperial"
    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    
while(True):
    cities = ["London", "Paris", "Shanghai", "Boston", "Moscow"]
    units = "imperial"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    
    for city in cities:
        WeatherTweet()
        
    # @TODO: Perform the API call to get the weather

    # @TODO: Twitter credentials

    # @TODO: Tweet the weather

    # @TODO: Print success message

# @TODO: Set timer to run every 1 hour

