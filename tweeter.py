from twython import Twython
from config import *
from index import *
from io import BytesIO

twitter = Twython(TWITTER_CONSUMER_KEY, TWITTER_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

def showMeThaTWEETS():
    Found, NokiaModel, PhoneImage = getNokiaPhone()
    print('Found: ', Found, '\nModel: ', NokiaModel, '\nImg: ', PhoneImage)

    if(Found == True):
        response = requests.get(PhoneImage)
        photo = BytesIO(response.content)
        response = twitter.upload_media(media=photo)
        tweet = "#BTC is a %s!" % NokiaModel
        twitter.update_status(status=tweet, media_ids=[response['media_id']])

    else:
        twitter.update_status(status ="NO PHONE AT THIS PRICE")

    return

showMeThaTWEETS()
