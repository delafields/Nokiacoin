from twython import Twython, TwythonError
from config import *
from index import *
from io import BytesIO
import time

twitter = Twython(TWITTER_CONSUMER_KEY, TWITTER_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

# If the rounded price matches a phone model,
# tweets that phone's image
def fireTweet():
    Found, phoneModel, phoneImage, roundedPrice, price = getNokiaPhone()
    print("Found: {0} \nModel: {1} \nImg: {2} \nroundedPrice: {3} \nprice: {4}".format(Found, phoneModel, phoneImage, roundedPrice, price))

    try:
        if(Found == True):
            response = requests.get(phoneImage)
            photo = BytesIO(response.content)
            response = twitter.upload_media(media=photo)

            successTweet = "At {0}, #BTC is a {1}".format(price, phoneModel)
            twitter.update_status(status=successTweet, media_ids=[response['media_id']])

        else:
            pass
            #failTweet = 'NO PHONE AT THIS PRICE (%s)' % roundedPrice
            #twitter.update_status(status =failTweet)
    except TwythonError as e:
        print(e.error_code)

    return

while True:
    fireTweet()
    time.sleep(28800)
