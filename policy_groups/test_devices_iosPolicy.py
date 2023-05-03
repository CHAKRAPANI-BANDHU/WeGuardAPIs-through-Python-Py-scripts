#devices in a iOS group
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils
import groupglobalvar as globalcheck

def url_formatter(page, psize):
    url = "enterprise/rest/devices/ios/profile/5eda5312273d1b2ede5ab3ad?page={page}&size={pagize}".format(page=page, pagize=psize)
    return url
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_group_iOS == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10106)
def test_tc_018_devicescount_policy(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        devices_groupUrl = url_formatter(globalcheck.page_0, globalcheck.pageSize_1000)
        apiUrl = globalvar.BaseURL + devices_groupUrl
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
            "-------------------------- TC 018 devices in apolicy failed ---------------------------\n\n")
        assert False

#10080
# devices_group_2Url = "enterprise/rest/devices/ios/profile/5eda5312273d1b2ede5ab3ad?page=1&size=1000"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_devices_group_iOS_1000_size_1 == 0, reason=" test is skipped")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10107)
def test_tc_018_devicescount_policy(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        devices_group_2Url = url_formatter(globalcheck.page_1, globalcheck.pageSize_1000)
        apiUrl = globalvar.BaseURL + devices_group_2Url
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
            "-------------------------- TC 018 devices in apolicy failed ---------------------------\n\n")
        assert False