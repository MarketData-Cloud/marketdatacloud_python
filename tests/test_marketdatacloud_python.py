from marketdatacloud_python import MDC

def test_mdc_info():
    """Tests an API call to get a day of market data"""

    mdc = MDC("BC074-099A8-963B5-BD650")
    response = mdc.price("US0378331005.NASDAQ")

    assert isinstance(response, dict)
    assert response == 1396, "The ID should be in the response"
