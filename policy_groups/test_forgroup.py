#devices in a group
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import groupglobalvar as globalcheck
import test_GETutils as utils


def url_formatter(psize, page):
    url = "enterprise/rest/weguard-v2/deviceCount?pageSize={pagize}&page={page}".format(pagize=psize, page=page)
    return url
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_forgroup_pageSize_50== 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10076)
def test_tc_002_forgroup_size50(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    print(globalcheck.android_policy_id)
    try :
        for policyid in globalcheck.android_policy_id:
            forgroupUrl = "enterprise/rest/weguard-v2/devices/forgroup/" + policyid + "?pageSize=" + str(
                globalcheck.pagesize_50) + "&page=" + str(globalcheck.page_1)
            apiUrl = globalvar.BaseURL + forgroupUrl
            print(apiUrl)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
             "-------------------------- TC 002 for group failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_forgroup_pageSize_100== 0, reason="Admin Create User test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10077)
def test_tc_002_forgroup_size_100(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        for policyid in globalcheck.android_policy_id:
            forgroupUrl_100 = "enterprise/rest/weguard-v2/devices/forgroup/" + policyid + "?pageSize=" + str(
                globalcheck.pagesize_100) + "&page=" + str(globalcheck.page_1)
            apiUrl = globalvar.BaseURL + forgroupUrl_100
            print(apiUrl)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 002 for group failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_forgroup_pageSize_200== 0, reason="Admin Create User test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10078)
def test_tc_002_forgroup_size_200(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        for policyid in globalcheck.android_policy_id:
            forgroupUrl_200 = "enterprise/rest/weguard-v2/devices/forgroup/" + policyid+ "?pageSize="+ str(
                    globalcheck.pagesize_200) + "&page=" + str(globalcheck.page_1)
            apiUrl = globalvar.BaseURL + forgroupUrl_200
            print(apiUrl)
            header = 'Bearer' + ' ' + globalvar.bearerToken
            res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
            WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                      + "\nRequest: " + str(res.request) + " Body: " + (
                                          str(res.request.body) if (
                                                      res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                      + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
                res.headers) + "\nResponse: " + str(res.content))
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 002 for group failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_forgroup_pageSize_50_page_0== 0, reason="Admin Create User test is skipped")
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.regressiontest
@pytest.mark.negativetest
@pytest.mark.run(order=10079)
def test_tc_002_forgroup_page_0(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        forgroupUrl_200 = "enterprise/rest/weguard-v2/devices/forgroup/5e9958fb77f85d51483d01fa?pageSize=" + str(
            globalcheck.pagesize_50) + "&page=" + str(globalcheck.page_0)
        apiUrl = globalvar.BaseURL + forgroupUrl_200
        print(apiUrl)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 002 for group failed ---------------------------\n\n")
        assert False