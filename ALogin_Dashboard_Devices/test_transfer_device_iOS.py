#Transferring an iOS device from devices page
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import groupglobalvar as globalcheck
import test_GETutils as utils

transfer_device_iOSUrl= "enterprise/rest/devices/ios/transfer"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_transfer_device_iOS == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10029)
def test_tc_014_transfer_device_iOS(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.iosdevices == []:
        pytest.skip("NO Devices in the account to Transfer. Skipping test")
    try:
        apiUrl = globalvar.BaseURL + transfer_device_iOSUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url= apiUrl, headers= {'Authorization': header}, json= globalvar.transfer_device_iOS, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 014 device transfer on devices page failed ---------------------------\n\n")
        assert False

