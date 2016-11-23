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
    def get_data(self, screen_name):
        alltweets = [] 
        #get first 200 tweets
        new_tweets = self.api.get_user_timeline(
            screen_name=screen_name, count=200)
        alltweets.extend(new_tweets)
        #get id for last tweet but 1
        oldest = alltweets[-1]['id'] - 1
        while len(new_tweets) > 0:
            # all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = self.api.get_user_timeline(
                screen_name=screen_name, count=200, max_id=oldest)
            # save most recent tweets
            alltweets.extend(new_tweets)
            # update the id of the oldest tweet but 1
            oldest = alltweets[-1]['id'] - 1
            #write tweets to csv
        tweets_df = pd.DataFrame(alltweets)
        tweets_df = tweets_df[['text','in_reply_to_screen_name']]
        tweets_df['text'] = tweets_df['text'].apply(self.process_tweet)
        fc = open(screen_name+'_tweets.csv', 'w+', newline='', encoding='utf-8')
        #tweets_df.to_csv(fc, encoding='utf-8')  
        tweets_df.to_csv(fc) 