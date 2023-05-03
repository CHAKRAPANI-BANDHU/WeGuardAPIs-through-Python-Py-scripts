# search for a system app For Android
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils
import groupglobalvar as globalcheck

def url_formatter(page, pagize):
    url = "enterprise/rest/deviceapps/search/com.android.contacts?page={page}&size={limit}".format(page=page, limit = pagize)
    return url
system_apps_searchUrl = "enterprise/rest/deviceapps/search/com.android.contacts?page=1&limit=10"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_system_apps_limit_10 == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10138)
def test_tc_038_getsystem_apps_10(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        system_apps_searchUrl = url_formatter(globalcheck.page_1, globalcheck.pagesize_10)
        apiUrl = globalvar.BaseURL + system_apps_searchUrl
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
        WeGuard.logger.error("-------------------------- TC 039 systemm apps search failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_system_apps_limit_50 == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10139)
def test_tc_038_getsystemapps_50(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        system_apps_limit_50 = url_formatter(globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL + system_apps_limit_50
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
        WeGuard.logger.error("-------------------------- TC 039 systemm apps search failed ---------------------------\n\n")
        assert False

system_apps_limit_100 = "enterprise/rest/deviceapps/search/com.android.contacts?page=1&limit=100"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_system_apps_limit_100 == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10140)
def test_tc_038_systemapps_100(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        system_apps_limit_100 = url_formatter(globalcheck.page_1, globalcheck.pagesize_100)
        apiUrl = globalvar.BaseURL + system_apps_limit_100
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
        WeGuard.logger.error("-------------------------- TC 039 systemm apps search failed ---------------------------\n\n")
        assert False