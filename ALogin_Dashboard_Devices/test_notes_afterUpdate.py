#Transferring device from devices page
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import groupglobalvar as globalcheck
import  test_GETutils as utils

notes = "enterprise/rest/notes"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_notes_devices_page_android_iOS == 0, reason="Skip test")
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.run(order=10032)
def test_tc_017_notes_after_update(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.android_devices == []:
        pytest.skip("No devices in the account. Skipping test")
    try:

        apiUrl = globalvar.BaseURL + notes
        headers = {'Authorization': 'Bearer' + ' ' + globalvar.bearerToken}
        res = requests.post(url= apiUrl, headers=headers, json= globalvar.Notes, timeout= globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 017 Notes failed ---------------------------\n\n")
        assert False