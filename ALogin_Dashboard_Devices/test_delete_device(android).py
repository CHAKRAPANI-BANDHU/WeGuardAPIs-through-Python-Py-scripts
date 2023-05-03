import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import groupglobalvar as globalcheck
import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_delete_device_android == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.raretest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.run(order=10034)
def test_tc_019_deleteDevice_android(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.android_devices == []:
        pytest.skip("Device doesn't exist in this account. Skipping test")
    if globalcheck.android_devices != []:
        pytest.skip("Device doesn't exist in this account. Skipping test")
    try:
        delete_deviceUrl = "enterprise/rest/weguard-v2/delete/" + globalcheck.android_devices[0] +"?suspend=false"
        apiUrl = globalvar.BaseURL + delete_deviceUrl
        Headers = {'Authorization':'Bearer {}'.format(globalvar.bearerToken) }
        res = requests.delete(url=apiUrl, headers=Headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 018 delete device failed ---------------------------\n\n")
        assert False

