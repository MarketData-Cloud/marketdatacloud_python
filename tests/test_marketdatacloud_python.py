from marketdatacloud_python import MDC
import vcr

@vcr.use_cassette('tests/vcr_cassettes/mdc-daily.yml', filter_query_parameters=['api_key'])
def test_mdc_info():
    """Tests an API call to get a day of market data"""

    mdc = MDC("US0378331005.NASDAQ")
    response = mdc.price()

    assert isinstance(response, dict)
    assert response["currency"] == "USD"
