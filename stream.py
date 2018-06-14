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
consumer_key = "3JK7Idi0naOx94B7CeCGP73db"
consumer_secret = "PFBP1otinXb7OgdvoLbikHpYuPzE2qs562rTB4I5JvSGcVuH2R"
access_token = "998969501948428290-MsaH5w3HFIzNxQGhxPRtPQT28PeMEaB"
access_token_secret = "rqvjfK7VfYc4Zn2k2rDvznMoLqKIDzOKFHlLIWDluEeMB"
auth = OAuthHandler(consumer_key, consumer_secret)
#setting access token and secret
auth.set_access_token(access_token, access_token_secret)
stream =Stream(auth,listener)
stream.filter(track=['Trump'])
