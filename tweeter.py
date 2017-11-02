from twython import Twython
from config import *

twitter = Twython(TWITTER_CONSUMER_KEY, TWITTER_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

twitter.update_status(status='See how easy using Twython is!')
