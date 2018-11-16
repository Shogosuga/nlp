import tweepy
import time

#tweepyをインポート　
CONSUMER_KEY = '8qqYKpCmhHz12maFnAZtH1Tiq'
CONSUMER_SECRET = 'OVsabb6XA6wXSBwcBrgjb5ZkZbRDkgoEfo3qRHlNygbDrFoPGk'
ACCESS_TOKEN = '1430529673-8DKgzTYLxQJSsNl3R4cr7ojFagvGHXgWG4K3oEw'
ACCESS_SECRET = 'Y1twCN883RURgdR1BZmRbMEvbHmlZ851eO42BAzvWNCaE'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

ids = []

for page in tweepy.Cursor(api.followers_ids, screen_name="tyksgk").pages(): 

    ids.extend(page) 

    time.sleep(2) 



print (ids)