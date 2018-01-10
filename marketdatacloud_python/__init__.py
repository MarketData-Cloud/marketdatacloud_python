import os
import requests

MDC_API_KEY = os.environ.get('MDC_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

class InvalidSymbolError(Exception):
    pass

if MDC_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://marketdata.cloud/dashboard?tab=token."
        )

headers = { "Authentication": MDC_API_KEY, "Acccept": "application/vnd.marketdatawizards.v1+json" }

from .mdc import MDC
