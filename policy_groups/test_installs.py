#Installing an app
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import test_GETutils as utils
import cases_validations as config

installs_Url = "enterprise/rest/weemm/install/5e3ce6c977f85d12cb613270/installs"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_installs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10123)
def test_tc_029_installs(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
        try:
            apiUrl = globalvar.BaseURL + installs_Url
            header = 'Bearer' + ' ' + globalvar.bearerToken
            res = requests.post(url = apiUrl, headers = {'Authorization': header}, json = globalvar.installs, timeout = globalvar.timeout)
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
            WeGuard.logger.error("Exception : " + str(e))
            WeGuard.logger.error("-------------------------- TC 029 install failed ---------------------------\n\n")
            assert False
