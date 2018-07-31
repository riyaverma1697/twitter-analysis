import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor
from tweepy import Stream


class StdOutListener(tweepy.StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 1
    def on_status(self,status):
        if 'RT @' not in status.text:
            if self.counter<50:
            #data = status.text
                print(self.counter)
                print(status.text)
                with open('streaming_data_Trump_new.txt','a',encoding = 'utf-8') as f:
                    f.write(status.text+'\n')
                self.counter += 1
                #f.write(data)
            else:
                stream.disconnect()
        return True
    def on_error(self,exception):
        print(exception)
    

listener = StdOutListener()
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = OAuthHandler(consumer_key, consumer_secret)
#setting access token and secret
auth.set_access_token(access_token, access_token_secret)
stream =Stream(auth,listener)
stream.filter(track=['NAME'])
