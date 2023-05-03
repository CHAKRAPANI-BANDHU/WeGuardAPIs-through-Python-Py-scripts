#deleting Android group
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import groupglobalvar as globalcheck
import test_GETutils as utils


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_delete_group_android == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10129)
def test_tc_034_delete_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        delete_groupUrl = "enterprise/rest/weguard-v2/" + globalvar.android_groupId + "/group"
        apiUrl = globalvar.BaseURL + delete_groupUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.delete(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                              res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 034 deleting group failed ---------------------------\n\n")
        assert False


