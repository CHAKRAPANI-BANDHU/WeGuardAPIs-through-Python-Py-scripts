#WeBox configs while cloning
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils


webox_config_cloning_androidUrl = "enterprise/rest/weguard-v2/webox/config/5ef34b7c273d1b2ede86623d"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_webox_configs_cloning_Android == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10097)
def test_tc_011_webox_configs_android(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + webox_config_cloning_androidUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.webox_configs_android, timeout=globalvar.timeout)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 011 webox configs failed ---------------------------\n\n")
        assert False

webox_config_cloning_iOSUrl = "enterprise/rest/weguard-v2/webox/config/5ef34be8273d1b2ede86624a?ios=true"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_webox_configs_cloning_iOS == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10098)
def test_tc_011_webox_configs_Ios(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + webox_config_cloning_androidUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.webox_configs_iOS, timeout=globalvar.timeout)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 011 webox configs failed ---------------------------\n\n")
        assert False