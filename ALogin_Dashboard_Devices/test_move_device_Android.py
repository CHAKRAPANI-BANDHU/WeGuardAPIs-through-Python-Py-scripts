#Transferring device from devices page for Android
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import groupglobalvar as globalcheck
import test_GETutils as utils

movedeviceUrl = "enterprise/rest/weguard-v2/movedevice"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_move_device_android == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.usualtest
@pytest.mark.run(order=10023)
def test_tc_011_move_device(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.android_devices == []:
        pytest.skip("No devices in the account. Skipping test")
    try:
        apiUrl = globalvar.BaseURL + movedeviceUrl
        headers = {'Authorization': 'Bearer' + ' ' + globalvar.bearerToken}
        res = requests.post(url= apiUrl, headers=headers, json= globalvar.move_device, timeout= globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 011 Device transfer failed ---------------------------\n\n")
        assert False
