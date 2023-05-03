# list is the api which calls when policy dialog is opened
import pytest
import json
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

disable_appsUrl = "enterprise/rest/disabledapps/5e3ce6c977f85d12cb613271"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_disable_apps== 0, reason="Admin Create User test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10082)
def test_tc_005_disableapps(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + disable_appsUrl
        WeGuard.logger.debug("\n\n--------------------------- Disable Apps ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, json= globalvar.disable_apps_post , timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        # json_resp = json.loads(res.content.decode())
        # disable_listids = json_resp.get('entities')
        # for item in disable_listids:
        #     globalvar.disable_apps_put_data.append(item.get('id'))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 005 disable apps ---------------------------\n\n")
        assert False

disable_apps_InvalidpolicyidUrl = "enterprise/rest/disabledapps/5e12da3bb850a4593"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_invalid_disable_apps == 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10083)
def test_tc_005_invalid_poliyid_disableapps(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + disable_apps_InvalidpolicyidUrl
        WeGuard.logger.debug("\n\n---------------------------Invalid policy id Disable Apps ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug( "\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
            + "\nRequest: " + str(res.request) + " Body: " + (
                str(res.request.body) if (res.request.method == 'POST' or res.request.method == 'PUT') else "")
            + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
                res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 005 disable apps ---------------------------\n\n")
        assert False

disable_apps_put = "enterprise/rest/disabledapps/5f31356ffce9664744905686"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_put_disable_apps== 0, reason="Admin Create User test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10084)
def test_tc_005_put_disableapps(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + disable_apps_put
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        # Data1 = {'Output': 'Result {}'.format(globalvar.disable_apps_put)}
        res = requests.put(url=apiUrl, headers=Headers, data= globalvar.disable_apps_put_data, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 005 disable apps ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_delete_disable_apps== 0, reason="Admin Create User test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10085)
def test_tc_005_delete_disabledAppsID(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        disable_apps_delete = "enterprise/rest/disabledapps/" + globalvar.disable_apps_put_data
        apiUrl = globalvar.BaseURL + disable_apps_delete
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.delete(url= apiUrl, headers= {'Authorization': header}, timeout= globalvar.timeout)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 005 disable apps ---------------------------\n\n")
        assert False

disable_apps_posturl = "enterprise/rest/disabledapps"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_post_disable_apps== 0, reason="Admin Create User test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10086)
def test_tc_005_postDisabledApps(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + disable_apps_posturl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url= apiUrl, headers= {'Authorization': header}, json= globalvar.disable_apps_post, timeout=globalvar.timeout)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 005 disable apps ---------------------------\n\n")
        assert False
