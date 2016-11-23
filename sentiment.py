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
    def remove_stopwords_feat(self,tweet):
        stopset = set(stopwords.words('english'))
        stopset.add('rt')
        #return dict([(tweet, True) for word in tweet if word not in stopset])
        return [w for w in tweet if not w in stopset]  
    def read_words(self,words_file):
        return [word for line in open(words_file, 'r', encoding="utf8") for word in line.split()]
    def sentence_score(self,tweet):
        score = 0
        for w in tweet:
            if w in self.pos:
                score+= 1
            elif w in self.neg:
                score-= 1
        try:
            score = score/len(tweet)
        except ZeroDivisionError:
            score = 0
        return score
    def score(self):
        self.tweet_text = self.tweet_text.apply(self.remove_stopwords_feat) # remove stopwords
        sent_score = []
        fin_score = 0
        for index, tweet in self.tweet_text.iteritems():
            sent_score.append(self.sentence_score(tweet))
        fin_score = sum(sent_score)/len(sent_score)
        print("The sentiment score is {}".format(fin_score))