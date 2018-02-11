import requests
import math
from data import phone_model_data


# Requests the current BTC price and returns both
# the price as well as the price rounded to the hundreds
def get_btc_price():
    print('Getting the current price of BTC...')

    try:
        response = requests.get(
            'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    trueBTCPrice = response.json()['USD']
    roundedBTCPrice = int(math.floor(trueBTCPrice / 100) * 100)

    return (trueBTCPrice, roundedBTCPrice)


# Compares the rounded price against a dict of nokia phone models
# returns the model info and prices
def getNokiaPhone():
    price, roundedPrice = get_btc_price()
    Found = False
    Nokiacoin, NokiacoinName, NokiacoinImg = '', '', ''

    for phone in phone_model_data:
        # - 10k for price increase
        if (phone == (roundedPrice - 10000) and Found == False):
            Found = True
            matchedPhone = nokiaPhones[phone]
            matchedPhoneName = matchedPhone.get('name')
            matchedPhoneImg = matchedPhone.get('image')
        else:
            pass

    return (Found, matchedPhoneName, matchedPhoneImg, roundedPrice, price)
