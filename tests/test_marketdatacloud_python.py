from marketdatacloud_python import MDC
from marketdatacloud_python import InvalidSymbolError
import vcr
import pytest

@vcr.use_cassette('tests/vcr_cassettes/mdc-daily.yml', filter_query_parameters=['api_key'])
def test_mdc_info():
    """Tests an API call to get a day of market data"""

    mdc = MDC("US0378331005.NASDAQ")
    response = mdc.price()

    assert isinstance(response, dict)
    assert response["currency"] == "USD"

@vcr.use_cassette('tests/vcr_cassettes/mdc-daily-error.yml', filter_query_parameters=['api_key'])
def test_mdc_error():
    with pytest.raises(InvalidSymbolError):
        """Tests an API call to get an error day of market data"""
        mdc = MDC("US0378331005.NASDA")
        response = mdc.price()
