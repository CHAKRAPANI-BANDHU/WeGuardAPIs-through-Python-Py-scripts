import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils
import groupglobalvar as globalcheck

def url_formatter(page, psize):
    url = "enterprise/rest/weguard-v2/messageHistory?page={page}&pageSize={pagize}".format(page=page, pagize=psize)
    return url

#msg_historyUrl = "enterprise/rest/weguard-v2/messageHistory?page=1&pageSize=10000"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_msg_history == 0, reason="when group is not opened")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10087)
def test_tc_006_msg_history(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        msg_historyUrl =  url_formatter(globalcheck.page_1, globalcheck.pagesize_10000)
        apiUrl = globalvar.BaseURL + msg_historyUrl
        print("\n\n---------------------------Msg History ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.msg_history, timeout=globalvar.timeout)
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
            "-------------------------- TC 006 message history failed ---------------------------\n\n")
        assert False


#msg_historyUrl1 = "enterprise/rest/weguard-v2/messageHistory?page=1&pageSize=1000"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_msg_history_page_1000 == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10088)
def test_tc_006_msg_history(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        msg_historyUrl1 = url_formatter(globalcheck.page_1, globalcheck.pageSize_1000)
        apiUrl = globalvar.BaseURL + msg_historyUrl1
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json= globalvar.msg_history, timeout=globalvar.timeout)
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
            "-------------------------- TC 006 message history failed ---------------------------\n\n")
        assert False

# msg_historyUrl2 = "enterprise/rest/weguard-v2/messageHistory?page=1&pageSize=100"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_msg_history_page_100 == 0, reason="skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10089)
def test_tc_006_msg_history(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        msg_historyUrl2 = url_formatter(globalcheck.page_1, globalcheck.pagesize_100)
        apiUrl = globalvar.BaseURL + msg_historyUrl2
        #f = open('Files/msg_history.txt', 'r')
        #request_json = json.loads(f.read())
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json= globalvar.msg_history, timeout=globalvar.timeout)
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
            "-------------------------- TC 006 message history failed ---------------------------\n\n")
        assert False

# msg_historyUrl3 = "enterprise/rest/weguard-v2/messageHistory?page=0&pageSize=100"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_msg_history_page_100_page_0 == 0, reason="skip test")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10090)
def test_tc_006_msg_history(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
       msg_historyUrl3 = url_formatter(globalcheck.page_0, globalcheck.pagesize_100)
       apiUrl = globalvar.BaseURL + msg_historyUrl3
       header = 'Bearer' + ' ' + globalvar.bearerToken
       res = requests.post(url=apiUrl, headers={'Authorization': header}, json=globalvar.msg_history, timeout = globalvar.timeout)
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
            "-------------------------- TC 006 message history failed ---------------------------\n\n")
        assert False
