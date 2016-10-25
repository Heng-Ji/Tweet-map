from sys import stdout
from tweepy import OAuthHandler
from tweepy import Stream
import requests
from tweepy.streaming import StreamListener
import json

ckey=""
csecret=""
atoken=""
asecret=""

class listener(StreamListener):

    def on_status(self, status):
        try:
            if status.coordinates:
                twitter = {'geo': status.coordinates['coordinates'], 'text': status.text}
                url = ''
                r = requests.post(url, json=twitter)
                print json.dumps(twitter)
        except:
            pass
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
while True:
    try:
        twitterStream.filter(locations=[-180,-90,180,90], async=False)
    except:
        pass
