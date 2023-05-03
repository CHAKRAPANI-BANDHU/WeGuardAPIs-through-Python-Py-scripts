#Updating an android device state(Lost/Stolen/Replaced or to Active)
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import groupglobalvar as globalcheck
import test_GETutils as utils
update_Device = "enterprise/rest/weguard-v2/updateDevice"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_update_device_android== 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.usualtest
@pytest.mark.run(order=10030)
def test_tc_015_update_device(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.android_devices == []:
        pytest.skip("No devices in  the account to update the device state")
    try:
        apiUrl = globalvar.BaseURL + update_Device
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
        WeGuard.logger.error("--------------------------- TC 015 update device failed ---------------------------\n\n")
        assert False

