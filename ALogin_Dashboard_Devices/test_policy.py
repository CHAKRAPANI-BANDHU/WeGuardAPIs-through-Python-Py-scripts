#opening a policy dialog from devices page by clicking on group name group column
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import groupglobalvar as globalcheck

import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_policy_device == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.usualtest
@pytest.mark.run(order=10021)
def test_tc_010_policy(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    if globalcheck.android_devices == []:
        pytest.skip("No devices in the account. skipping test")
    try:
        policyUrl = "enterprise/rest/weguard-v2/policy/"+ globalcheck.android_policy_id[0]
        apiUrl = globalvar.BaseURL + policyUrl
        headers = {'Authorization': 'Bearer' + ' ' + globalvar.bearerToken}
        res = requests.get(url= apiUrl, headers=headers, timeout= globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 010 unable go to policy dialog from policy page ---------------------------\n\n")
        assert False

policyUrl1 ="enterprise/rest/policy/5e12da3bccc4593"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_policy_device_invalid_policy_id == 0, reason="skip if no devices in the account")
@pytest.mark.negativetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.usualtest
@pytest.mark.run(order=10022)
def test_tc_010_policy_invalidId(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + policyUrl1
        headers = {'Authorization': 'Bearer' + ' ' + globalvar.bearerToken}
        res = requests.get(url= apiUrl, headers=headers, timeout= globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code != 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 010 unable go to policy dialog from policy page ---------------------------\n\n")
        assert False



