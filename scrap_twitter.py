import tweepy
import csv
import pandas as pd

####input your credentials here
consumer_key = '5s0DnVLEDskTi8MAz8lLvvc1Q'
consumer_secret = 'rVMrZB4NXuZ8nPYNqvHVdXRI0VqNIEHa4h3FLFDr5TPoVqIHQf'
access_token = '1150637746488107010-SLeTteFjZdyZKriKnrv1JSkx2tpSUs'
access_token_secret = 'inmbtFmxvNRZkBtiTFofCTZq1QDb8xB2VL' \
                      'cpFnqViw2La'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('#paracet4.csv', 'a')
#Use csv Writers
csvWriter = csv.writer(csvFile)
# search
search = "efek paracetamol"

for tweet in tweepy.Cursor(api.search,
                           q=search,
                           count=1000,
                           lang="id",
                           since="2019-01-08",
                           until="2019-12-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])