import requests
from nokia import nokia_phones

def getBTCPrice():
    reqBTCPrice = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
    BTCPrice = int(round(reqBTCPrice.json()['USD'] / 100) * 100)
    return BTCPrice

def getNokiaPhone():
    price = getBTCPrice()
    Found = False
    Nokiacoin, NokiacoinName, NokiacoinImg = '', '', ''

    for phone in nokia_phones:
        if(phone == price and Found == False):
            Found = True
            Nokiacoin = nokia_phones[phone]
            NokiacoinName = Nokiacoin.get('name')
            NokiacoinImg = Nokiacoin.get('image')

    return(Found, NokiacoinName, NokiacoinImg)
