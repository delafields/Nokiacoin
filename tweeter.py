from twython import Twython, TwythonError
from config import *
from index import *
from io import BytesIO

twitter = Twython(TWITTER_CONSUMER_KEY, TWITTER_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

def showMeThaTWEETS():
    Found, NokiaModel, PhoneImage, btcPrice = getNokiaPhone()
    print('Found: ', Found, '\nModel: ', NokiaModel, '\nImg: ', PhoneImage, '\nPrice: ', btcPrice)

    try:
        if(Found == True):
            response = requests.get(PhoneImage)
            photo = BytesIO(response.content)
            response = twitter.upload_media(media=photo)
            successTweet = "#BTC is a %s!" % NokiaModel
            twitter.update_status(status=successTweet, media_ids=[response['media_id']])

        else:
            failTweet = 'NO PHONE AT THIS PRICE (%s)' % btcPrice
            twitter.update_status(status =failTweet)
    except TwythonError as e:
        print(e.error_code)


    return

showMeThaTWEETS()
