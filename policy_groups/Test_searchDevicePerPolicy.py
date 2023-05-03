# search device in a policy (Android or iOS)
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils
import groupglobalvar as globalcheck

def url_formatter(searchst, devicetype, page, psize):
    url = "enterprise/rest/weguard-v2/search/5e12da3bccc31c1b850a4593?searchString={searchstr}&deviceType={devicetyp}&page={page}&pageSize={pagize}".format(searchstr = searchst, devicetyp= devicetype, page=page, pagize=psize)
    return url

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_search_devices_group_Android_3digits== 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10113)
def test_tc_024_search_device_per_policy_Android(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        search_device_android = url_formatter(357, "Android", globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL +  search_device_android
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
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
        WeGuard.logger.error("-------------------------- TC 024 device search in a policy failed ---------------------------\n\n")
        assert False


# search_device_per_policy_Url_2digits_android = "enterprise/rest/weguard-v2/search/5e12da3bccc31c1b850a4593?searchString=37&deviceType=Android&page=1&pageSize=50"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_search_devices_group_2digits_Android== 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10114)
def test_tc_024_search_device_2digit_per_policy_Android(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        search_device_Url_2digits_android = url_formatter(35, "Android", globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL +  search_device_Url_2digits_android
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
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
        WeGuard.logger.error("-------------------------- TC 024 device search with 2 digits in a policy failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_search_devices_group_1digit_Android== 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10115)
def test_tc_024_search_device__1digit_per_policy_Android(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        search_device_1dig_android_url = url_formatter(3, "Android", globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL +  search_device_1dig_android_url
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
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
        WeGuard.logger.error("-------------------------- TC 024 device search with 1 digit in a policy failed ---------------------------\n\n")
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_search_devices_group_iOS_3strs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10116)
def test_tc_024_search_device__3strs_per_policy_iOS(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        search_device_3strs_iOSUrl =  url_formatter("ccq", "IOS", globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL +  search_device_3strs_iOSUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
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
        WeGuard.logger.error("-------------------------- TC 024 device search with 3 digits in a policy failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_search_devices_group_2strs_iOS== 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10117)
def test_tc_024_search_device__2strs_per_policy_iOS(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        search_device_2strs_iOSUrl =  url_formatter("cc", "IOS", globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL +  search_device_2strs_iOSUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
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
        WeGuard.logger.error("-------------------------- TC 024 device search with 2 digits in a policy failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_search_devices_group_1str_iOS == 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10118)
def test_tc_024_search_device__1str_per_policy_iOS(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        search_device_1str_iOSUrl =  url_formatter("c", "IOS", globalcheck.page_1, globalcheck.pagesize_50)
        apiUrl = globalvar.BaseURL +  search_device_1str_iOSUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 024 device search with 1 digit in a policy failed ---------------------------\n\n")
        assert False