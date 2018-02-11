import requests
import math
import sys
import os
import dotenv # python-dotenv
import random
from collections import namedtuple
from twython import Twython, TwythonError
from io import BytesIO
from data import phone_model_data, tweet_templates

dotenv.load_dotenv('config.env')

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_SECRET_KEY')
twitter_access = os.environ.get('TWITTER_ACCESS_TOKEN')
twitter_secret = os.environ.get('TWITTER_ACCESS_SECRET')


def get_btc_price():
    '''Requests the current BTC price in $s. Returns the price and price rounded to the hundredths'''

    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'

    print('Getting the current price of BTC...\n')

    try:
        response = requests.get(url)
        true_price = response.json()['USD']
        rounded_price = int(math.floor(true_price / 100) * 100)

        print('Price successfully retrieved.\n')
        return (true_price, rounded_price)

    except requests.exceptions.RequestException as e:
        print('Error with price request: {}\n'.format(e))
        sys.exit(1)


def get_nokia_phone(true_price, rounded_price):
    '''Compares the rounded BTC price against nokia phone models. Returns phone name/image and btc price.'''

    matched_phone, phone_name, phone_image = None, None, None
    Found = False

    # Artifically adjust price if it goes north of $10k
    if rounded_price >= 10000 and rounded_price <= 20000:
      rounded_price += 10000

    print('Searching for a phone match...\n')
    for phone in phone_model_data:
      if phone == rounded_price and Found == False:
          matched_phone = phone_model_data[phone]
          phone_name = matched_phone.get('name')
          phone_image = matched_phone.get('image')
          Found = True

    PhoneData = namedtuple('PhoneData', 'found phone_name phone_image')
    tweet_data = PhoneData(found=Found, phone_name=phone_name, phone_image=phone_image)

    return(tweet_data)

twitter = Twython(consumer_key, consumer_secret, twitter_access,
                  twitter_secret)

def fireTweet():
    '''Tweets a short idiom about the current BTC price along with its associated Nokia phone model/image'''

    true_price, rounded_price = get_btc_price()

    Found, phone_name, phone_image = get_nokia_phone(true_price, rounded_price)

    if Found == True:
        try:
            response = requests.get(phone_image)
            streamable_photo = BytesIO(response.content)
            tweetable_photo = twitter.upload_media(media=streamable_photo)

            tweet = random.choice(tweet_templates).format(true_price, phone_name)
            twitter.update_status(status=tweet, media_ids=[tweetable_photo['media_id']])

        except TwythonError as e:
            print('There was an error with the Twitter client: ', e)
    else:
        sys.exit(1)

fireTweet()
