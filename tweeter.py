import os
import dotenv
import random
from twython import Twython, TwythonError
from io import BytesIO
from index import *
from tweetTemplate import tweets

dotenv.load_dotenv('config.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_SECRET_KEY')
twitter_access = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_secret = os.environ.get('TWITTER_ACCESS_SECRET')

twitter = Twython(consumer_key, consumer_secret, twitter_access,
                  twitter_secret)


# If the rounded price matches a phone model,
# tweets that phone's image
def fireTweet():
    Found, phoneModel, phoneImage, roundedPrice, price = getNokiaPhone()
    print(
        "Found: {0} \nModel: {1} \nImg: {2} \nroundedPrice: {3} \nprice: {4}".
        format(Found, phoneModel, phoneImage, roundedPrice, price))

    try:
        if (Found == True):
            response = requests.get(phoneImage)
            photo = BytesIO(response.content)
            response = twitter.upload_media(media=photo)

            successTweet = tweets[random.randrange(0, len(tweets))].format(
                price, phoneModel)
            twitter.update_status(
                status=successTweet, media_ids=[response['media_id']])

        else:
            #pass
            failTweet = 'NO PHONE AT THIS PRICE (%s) 😫' % price
            twitter.update_status(status=failTweet)
    except TwythonError as e:
        print(e)

    return


fireTweet()
