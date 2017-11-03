import requests
import math
from nokia import nokiaPhones

# Requests the current BTC price and returns both
# the price as well as the price rounded to the hundreds
def getBTCPrice():
    print('Getting the current price of BTC...')

    try:
        resBTCPrice = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

    actualBTCPrice = resBTCPrice.json()['USD']
    roundedBTCPrice = int(math.floor(resBTCPrice.json()['USD'] / 100) * 100)

    return(actualBTCPrice, roundedBTCPrice)

# Compares the rounded price against a dict of nokia phone models
# returns the model info and prices
def getNokiaPhone():
    price, roundedPrice = getBTCPrice()
    Found = False
    Nokiacoin, NokiacoinName, NokiacoinImg = '', '', ''

    for phone in nokiaPhones:
        if(phone == roundedPrice and Found == False):
            Found = True
            matchedPhone = nokiaPhones[phone]
            matchedPhoneName = matchedPhone.get('name')
            matchedPhoneImg = matchedPhone.get('image')
        else:
            pass

    return(Found, matchedPhoneName, matchedPhoneImg, roundedPrice, price)
