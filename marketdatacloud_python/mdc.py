from . import headers
from . import InvalidSymbolError
import requests

class MDC(object):
    def __init__(self, symbol):
        self.symbol  = symbol
        self.base_url = "https://marketdata.cloud/api/prices/" + symbol

    def price(self):
        response = requests.get(self.base_url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise InvalidSymbolError(
                    "The symbol does not exist."
                    " "
                    "Please see https://marketdata.cloud/exchanges for a list of exchanges and their securities"
                    )
