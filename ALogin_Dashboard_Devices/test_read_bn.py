import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

bnUrl = "enterprise/rest/bannernotifications/read"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_001_bannerNotification_read == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10015)
def test_tc_008_read_bn(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + bnUrl
        headers = {'Authorization': 'Bearer' + ' ' + globalvar.bearerToken}
        res = requests.get(url= apiUrl, headers=headers, timeout= globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n"  " Response Headers: " + str(
                res.headers)  + " apiUrl: " + apiUrl + " Response code: " + str(res.status_code)  + "\n" + " Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 008 Failed to read banner notification  ---------------------------\n\n")
        assert False

