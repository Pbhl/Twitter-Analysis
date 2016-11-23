import pandas as pd
from twython import *
import json
from nltk import *
import string
#from nltk.twitter.util import json2csv
import csv
import re
class TwitterDataCollect:
    def __init__(self):
        import tweepy
        from tweepy import OAuthHandler
        # V. IMPORTANT DO I NEED ACCESS TOKEN
        TWITTER_APP_KEY = 'qQfX6GH7VAXeKmCp2MsayL2wr'
        TWITTER_APP_KEY_SECRET = 'hquhesVieC9Zb582MgjbODLMXoqJjhncmvpwJaz18QIK2o4F8w'
        TWITTER_ACCESS_TOKEN = '2842073465-NcwSRO6gUQjhKMD77oIe2stt5gtzmiHtLLGFjgJ'
        TWITTER_ACCESS_TOKEN_SECRET = '0aLJAH0zn9ImxqpBtfC65ffcC9GVxkvyGcnZNmQI36p7j'

        self.api = Twython(app_key=TWITTER_APP_KEY,
                           app_secret=TWITTER_APP_KEY_SECRET,
                           oauth_token=TWITTER_ACCESS_TOKEN,
                           oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
     def read_words(self,words_file):
            return [word for line in open(words_file, 'r', encoding="utf8") for word in line.split()]  
     def strip_non_ascii(self, txt):
        stripped = (c for c in txt if ((c in self.emot) or (0 < ord(c) < 127)))
        return ''.join(stripped)
     def process_tweet(self, tweet):
        #Remove non-ascii characters
        tweet = self.strip_non_ascii(tweet)
        # Convert to lower case
        tweet = tweet.lower()
        #Remove b' leading characters
        #tweet = tweet[2:]
        # Convert www.* or https?://* to blank
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', tweet)
        # Convert @username to blank
        tweet = re.sub('@[^\s]+', '', tweet)
        # Replace #word with word
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        #Remove repeating characters
        tweet = re.sub(r'(.)\1\1+', r'\1', tweet)
        #Remove words starting with numbers
        tweet = re.sub(r'(\s)\d\w+', '', tweet)
        # Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        # trim
        tweet = tweet.strip('\'"')
        return tweet