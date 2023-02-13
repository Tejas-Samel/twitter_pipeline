import tweepy
import pandas as pd
from datetime import datetime
import os
from azure.storage.blob import BlobClient
import time

def run_twitter_etl():
    key= ''
    secret_key = ""
    acc_token = ""
    acc_token_secret = ""

    #Authentication
    auth = tweepy.OAuthHandler(key,secret_key)
    auth.set_access_token(acc_token,acc_token_secret)
    
    #API object
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='@elonmusk',
                                count=200,
                                #retweets
                                include_rts =False,
                                tweet_mode='extended')

    print(len(tweets))
    tweet_list = []

    for tweet in tweets:
        text =tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        "text":text,
                        "favourite_count": tweet.favorite_count,
                        "retweet_count": tweet.retweet_count,
                        "created_at":tweet.created_at}

        tweet_list.append(refined_tweet)
    filename= datetime.now().date().__str__()
    
    sas = 'https://twitter00data.blob.core.windows.net/twitter-data/'+filename+'--elon.csv?sp=r&st=2022-11-18T16:38:05Z&se=2022-11-20T00:38:05Z&sv=2021-06-08&sr=c&sig=iVW1BYlvmOyVtKNjhQxHUFGJwO5p%2FzN%2BXDkU%2F5LdCfQ%3D'

    
    df = pd.DataFrame(tweet_list)
    print(filename)
    df.to_csv(filename+'--elon.csv')
    with open('./' +filename+'--elon.csv','rb') as f:
        BlobClient.from_blob_url(sas).upload_blob(f)

    # print(tweets)
    os.remove('./'+ filename +'--elon.csv')
run_twitter_etl()