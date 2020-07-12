import tweepy
import csv

access_token = 'xxxxx'
access_token_secret = 'xxxxx'
api_key = 'xxxx'
api_secret_key = 'xxxx'

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

csvFile = open('#paracet3.csv', 'a')
#Use csv Writers
csvWriter = csv.writer(csvFile)

# timeline twitter
# timeline = api.home_timeline()
# for tweet in timeline:
#     print(tweet.text)

# setiap user
# user_timeline = api.user_timeline('jokowi', tweet_mode='extended')
# for tweet in user_timeline:
#     print(tweet.full_text)

# berdasar search
since = '2019-01-01'
until = '2019-12-31'
search = 'efek obat'
jml = 1000

query = api.search(q=search,since_id=str(since),count=(jml))
for tweet in tweepy.Cursor(query):
    print(tweet.created_at, tweet.text)
csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

# print (tweet.created_at, tweet.full_text)
#     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
