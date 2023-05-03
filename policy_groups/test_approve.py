#approve product list
import pytest
import requests
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import cases_validations as config
import test_GETutils as utils

approve_Url = "enterprise/rest/weemm/product/list/approve"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_approve_after_update == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10125)
def test_tc_031_approve(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + approve_Url
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url = apiUrl, headers = {'Authorization': header}, json = globalvar.approve, timeout = globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        print(e)
        assert False
