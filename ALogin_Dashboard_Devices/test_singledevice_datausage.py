import pytest
import requests
from datetime import datetime
import payloads as globals, layouts as validations
import test_GETutils as utils
import WeGuardlogger as WeGuard
import globalvariables as globalvar

datausagepiechart_URL = "enterprise/rest/app/device/"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_datausage_devicesview == 0, reason="datausage piechart details in single devices view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sprint20
@pytest.mark.run(order=10064)
def test_tc_00001_datausage_devicesview(url):
    WeGuard.logger.error("\n\n--------------------------- datausage piechart details in single devices view on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        apiUrl = globalvar.BaseURL + datausagepiechart_URL+ globals.calldeviceid
        WeGuard.logger.error(apiUrl)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
            WeGuard.logger.debug(
                "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                    res.status_code) + "\n Response: " + str(res.content))
            WeGuard.logger.debug(
                "\n\n--------------------------- datausage piechart details in single devices view on portal PASS ---------------------------")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- datausage piechart details in single devices view on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

