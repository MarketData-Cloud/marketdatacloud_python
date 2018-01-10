from . import headers
import requests

class MDC(object):
    def __init__(self, symbol):
        self.symbol  = symbol
        self.base_url = "https://marketdata.cloud/api/prices/" + symbol

    def price(self):
        response = requests.get(self.base_url, headers=headers)
        return response.json()
