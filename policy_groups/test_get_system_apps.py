# system apps For Android
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils
import groupglobalvar as globalcheck

# system_appsUrl = "enterprise/rest/deviceapps/apps?page=1&limit=10"

def url_formatter(page, psize):
    url = "enterprise/rest/deviceapps/apps?page={page}&limit={lim}".format(page=page, lim=psize)
    return url
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_get_systemapp_10 == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10135)
def test_tc_038_getsystem_apps_10(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        system_appsUrl = url_formatter(globalcheck.page_1, globalcheck.pagesize_10)
        apiUrl = globalvar.BaseURL + system_appsUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
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
        WeGuard.logger.error("-------------------------- TC 038 get systemm apps failed ---------------------------\n\n")
        assert False

# system_appsUrl_limit_50 = "enterprise/rest/deviceapps/apps?page=1&limit=50"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_get_systemapp_50 == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10136)
def test_tc_038_getsystemapps_50(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        system_appsUrl_limit_50 = url_formatter(globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL + system_appsUrl_limit_50
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
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
        WeGuard.logger.error("-------------------------- TC 038 get systemm apps failed ---------------------------\n\n")
        assert False

system_appsUrl_limit_100 = "enterprise/rest/deviceapps/apps?page=1&limit=100"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_get_systemapp_100 == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10137)
def test_tc_038_systemapps_100(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        system_appsUrl_limit_100 = url_formatter(globalcheck.page_1, globalcheck.pagesize_100)
        apiUrl = globalvar.BaseURL + system_appsUrl_limit_100
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
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
        WeGuard.logger.error( "-------------------------- TC 038 get systemm apps failed ---------------------------\n\n")
        assert False


