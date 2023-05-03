 #delete ios devices
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import groupglobalvar as globalcheck
import test_GETutils as utils


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_delete_device_iOS == 0, reason="Skip test")
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.positivetest
@pytest.mark.raretest
@pytest.mark.run(order=10033)
def test_tc_018_delete_device(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.iosdevices == []:
        pytest.skip("Device doesn't exist in this account. Skipping test")
    if globalcheck.iosdevices != []:
        pytest.skip("Skipping Device deletion test")
    delete_deviceurl = "enterprise/rest/devices/ios/" + globalcheck.dep_devices[0]
    try:
        apiUrl = globalvar.BaseURL + delete_deviceurl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.delete(url=apiUrl, headers={'Authorization': header}, timeout=10)
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
