import requests
from nokia import nokiaPhones

# Requests the current BTC price and returns both
# the price as well as the price rounded to the hundreds
def getBTCPrice():
    print('Getting the current price of BTC...')

    resBTCPrice = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    actualBTCPrice = resBTCPrice.json()['USD']
    roundedBTCPrice = int(round(resBTCPrice.json()['USD'] / 100) * 100)

    return(actualBTCPrice, roundedBTCPrice)

# Compares the rounded price against a dict of nokia phone models
# returns the model info and prices
def getNokiaPhone():
    #price, roundedPrice = getBTCPrice()
    price = 8008135
    roundedPrice = 7100
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
