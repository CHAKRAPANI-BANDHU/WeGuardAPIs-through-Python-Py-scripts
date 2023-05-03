#uninstallating an app
import pytest
import requests
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import cases_validations as config
import test_GETutils as utils

uninstalls_Url = "enterprise/rest/weemm/install/5e69cc0e77f85d7c96b0d9d2/uninstalls"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_uninstalls == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10124)
def test_tc_030_unstalls(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + uninstalls_Url
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url = apiUrl, headers = {'Authorization': header}, json = globalvar.uninstalls, timeout = globalvar.timeout)
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
        WeGuard.logger.error("-------------------------- TC 030 uninstall failed ---------------------------\n\n")
        assert False
