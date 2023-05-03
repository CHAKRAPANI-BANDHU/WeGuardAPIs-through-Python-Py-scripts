import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils
import groupglobalvar as globalcheck

#DevicecountUrl = "enterprise/rest/weguard-v2/deviceCount?pageSize=10,000&page=1"
def url_formatter(psize, page):
    url = "enterprise/rest/weguard-v2/deviceCount?pageSize={pagize}&page={page}".format(pagize=psize, page=page)
    return url

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_count_pageSize_1000== 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10073)
def test_tc_001_devicescount(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        DevicecountUrl =  url_formatter(globalcheck.pagesize_10000, globalcheck.page_1)
        apiUrl = globalvar.BaseURL + DevicecountUrl
        print("\n\n--------------------------- Device count ---------------------------")
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
            "-------------------------- TC 001 device count failed---------------------------\n\n")
        assert False

#Devicecount_1000_Url = "enterprise/rest/weguard-v2/deviceCount?pageSize=1000&page=1"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_count_pageSize_1000== 0, reason="policy is not opened")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10074)
def test_tc_001_devicescount(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        Devicecount_1000_Url =  url_formatter(globalcheck.pageSize_1000, globalcheck.page_1)
        apiUrl = globalvar.BaseURL + Devicecount_1000_Url
        print("\n\n--------------------------- Device count ---------------------------")
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
            "-------------------------- TC 001 device count failed ---------------------------\n\n")
        assert False

Devicecount_1000_Url_page_0 = "enterprise/rest/weguard-v2/deviceCount?pageSize=1000&page=0"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_count_pageSize_1000_page_0== 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10075)
def test_tc_001_devicescount(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        Devicecount_1000_Url_page_0 =  url_formatter(globalcheck.pageSize_1000, globalcheck.page_0)
        apiUrl = globalvar.BaseURL + Devicecount_1000_Url_page_0
        print("\n\n--------------------------- Device count ---------------------------")
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
            "-------------------------- TC 001 device count failed---------------------------\n\n")
        assert False