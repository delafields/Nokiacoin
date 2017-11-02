import requests
from nokia import nokia_phones

reqBTCPrice = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
#BTCPrice = int(round(float(reqBTCPrice.text)), -2)
test = reqBTCPrice.text[7:14]

print(test)
