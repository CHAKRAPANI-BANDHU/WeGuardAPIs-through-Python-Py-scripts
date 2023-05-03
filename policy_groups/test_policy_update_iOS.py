#updating or saving the policy
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils

policy_updateUrl = "enterprise/rest/ios/profile/5e3bef5577f85d12cb610674"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_update_group_iOS == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10109)
def test_tc_020_policy_update(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        print("\n-------------------Policy Update-------------------------")
        apiUrl = globalvar.BaseURL + policy_updateUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.put(url = apiUrl, headers = {'Authorization': header}, json = globalvar.update_policy_iOS, timeout = globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug( "\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
            + "\nRequest: " + str(res.request) + " Body: " + (
                str(res.request.body) if (res.request.method == 'POST' or res.request.method == 'PUT') else "")
            + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
                res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 020 update policy  failed ---------------------------\n\n")
        assert False



