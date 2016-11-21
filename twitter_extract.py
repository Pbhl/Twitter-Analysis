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