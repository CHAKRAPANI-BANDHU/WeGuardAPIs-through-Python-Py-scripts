import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils

appresSchema_url = "enterprise/rest/weemm/product/appsRestrictionsSchema"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_appresSchema == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10143)
def test_tc_041_post_appresSchema(url):
    try:
        apiUrl = globalvar.BaseURL + appresSchema_url
        Headers = {'Authorization':'Bearer {}'.format(globalvar.bearerToken) }
        res = requests.post(url= apiUrl, headers=Headers, json=globalvar.appResSchema, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                              res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) )
        assert res.status_code == 200
    except BaseException as e:
        print(e)
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_appresSchema == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10145)
def test_tc_041_get_appresSchema(url):
    try:
        get_appresSchema_url = "enterprise/rest/weemm/product/appRestrictionsSchema/app%3Acom.android.chrome"
        apiUrl = globalvar.BaseURL + get_appresSchema_url
        Headers = {'Authorization':'Bearer {}'.format(globalvar.bearerToken) }
        res = requests.get(url= apiUrl, headers=Headers, timeout=globalvar.timeout)
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
        WeGuard.logger.error("--------------------------- TC 041 app restriction schema failed ---------------------------\n\n")
        assert False
