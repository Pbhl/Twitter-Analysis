from twitter_extract import TwitterDataCollect
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
class SentimentScore:
    def __init__(self,user_name):
        self.tdc = TwitterDataCollect()
        self.tdc.get_data(user_name)
        self.tweets_df = pd.read_csv(user_name+'_tweets.csv')
        self.tweets_df['sentence_score'] = np.random.randn(len(self.tweets_df['text'])) #column to store sentence score
        self.tweet_text = self.tweets_df['text']
        self.tweet_text.dropna(inplace=True)#remove blanks
        self.tweet_text = self.tweet_text.str.split()  #bag of words of tweets
        #get list of positive and negative words
        pos_file="C:\\Users\\parth\\Desktop\\Twitter_nongit\\Twitter\\positive-words.txt"
        neg_file="C:\\Users\\parth\\Desktop\\Twitter_nongit\\Twitter\\negative-words.txt"
        pos_emot="C:\\Users\\parth\\Desktop\\Twitter_nongit\\Twitter\\positive-emot.txt"
        neg_emot="C:\\Users\\parth\\Desktop\\Twitter_nongit\\Twitter\\negative-emot.txt"
        self.pos=self.read_words(pos_file) + self.read_words(pos_emot)
        self.neg=self.read_words(neg_file) + self.read_words(neg_emot)