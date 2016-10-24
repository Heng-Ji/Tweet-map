
    
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from flask import request
from sys import stdout
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json


def main():
    # Authentication information for Twitter API
    ckey=""
    csecret=""
    atoken=""
    asecret=""

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    twitter_stream = Stream(auth, Listener())
    twitter_stream.filter(locations=[-180,-90,180,90])


class Listener(StreamListener):

    def on_data(self, data):
        d = json.loads(data)
        try:
            if d['coordinates']:
                twitter = {'name':d['user']['name'], 'geo': d['coordinates']['coordinates'], 'text': d['text']}
                url = 'http://search-ccbigdata-vflc3fpahmprze34myukffb7fq.us-west-2.es.amazonaws.com/twitter/tweets'
                r = requests.post(url, json=twitter)
                print json.dumps(twitter)
        except:
            pass
        return True

    def on_error(self, status):
        print status


if __name__ == "__main__":
    main()