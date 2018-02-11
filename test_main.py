import unittest
import requests
from unittest.mock import patch, Mock
from index2 import get_btc_price

class TestGetBTCPrice(unittest.TestCase):

    def test_returns_prices(self):
        with patch('requests.get') as mock_request:
            url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'

            mock_request.return_value.content = {'USD': 8000}

            response =

            self.assertEqual(response.)


if __name__ == '__main__':
    unittest.main()
