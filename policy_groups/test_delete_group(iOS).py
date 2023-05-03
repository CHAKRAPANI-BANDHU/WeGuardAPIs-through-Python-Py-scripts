#deleting iOS groups
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

delete_groupUrl = "enterprise/rest/ios/profile/" +globalvar.ios_groupid

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_delete_group_iOS == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10120)
def test_tc_026_delete_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        delete_groupUrl = "enterprise/rest/ios/profile/" + globalvar.ios_groupid
        apiUrl = globalvar.BaseURL + delete_groupUrl
        print(apiUrl)
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
        WeGuard.logger.error("-------------------------- TC 026 delete group ios failed ---------------------------\n\n")
        assert False


