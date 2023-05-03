import pytest
import requests
from _datetime import datetime
import globalvariables as globalvar
import test_jsonnames as jsonnames
import layouts as validations, payloads as globals
import test_GETutils as utils

import WeGuardlogger as WeGuard

wetalkcallhistory_URL = "enterprise/rest/wetalk/history/user/"
wetalkcallhistory1_URL = "enterprise/rest/wetalk/history/"

WeGuard.logger.debug("wetalk call history APIs")

#--- Save Twillio call history ---
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalkcallhistory == 0, reason="wetalk call history start on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00001_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for device on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory1_URL
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        data ={
            jsonnames.DEVICEID: globals.calldeviceid,
            jsonnames.CALLID: jsonnames.OPS+"_"+globalvar.userName+"_"+globals.calldeviceid+"_"+globals.WTtimestamp,
            jsonnames.DURATION: None,
            jsonnames.DATE: globals.nowtd,
            jsonnames.DISPLAYNAME: " ",
            jsonnames.TYPE: jsonnames.OPStoDEVICE,
            jsonnames.SOURCE: 1,
            jsonnames.INITIATEDBY: globalvar.userName,
            jsonnames.ACTCODE: globalvar.actcode,
            jsonnames.STATUS: jsonnames.START,
            jsonnames.CREATEDBY: globalvar.userName
        }
        res = requests.post(url=api_URL, json=data, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------wetalk call history start on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history start on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

#--- Save Twillio call history ---
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_wetalkcallhistory == 0, reason="wetalk call history end on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00002_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history end on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory1_URL
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        data ={
            jsonnames.DEVICEID: globals.calldeviceid,
            jsonnames.CALLID: jsonnames.OPS+"_"+globalvar.userName+"_"+globals.calldeviceid+"_"+globals.WTtimestamp,
            jsonnames.DURATION: 3000,
            jsonnames.DATE: globals.nowtd,
            jsonnames.DISPLAYNAME: " ",
            jsonnames.TYPE: jsonnames.OPStoDEVICE,
            jsonnames.SOURCE: 1,
            jsonnames.INITIATEDBY: globalvar.userName,
            jsonnames.ACTCODE: globalvar.actcode,
            jsonnames.STATUS: jsonnames.END,
            jsonnames.CREATEDBY: globalvar.userName
        }
        res = requests.post(url=api_URL, json=data, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------wetalk call history end on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history end on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

#--- Read call history for device ---
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_wetalkcallhistory == 0, reason="wetalk call history for device on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00003_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for device on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory1_URL+ "device/" + globals.calldeviceid
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for device on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history for device on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

#----Read call history for account----
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00004_wetalkcallhistory == 0, reason="wetalk call history for account on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00004_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for account on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory1_URL+ "account/" + globalvar.actcode
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for account on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history for account on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

#---Read call history for account(initiatedby)---------
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00005_wetalkcallhistory == 0, reason="wetalk call history for account user on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00005_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for account user on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory_URL + globalvar.userName + "?page=" + globals.page + "&pageSize=" + globals.pageSize
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200 
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for account user on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False


#---Read call history for account(initiatedby)---------
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00006_wetalkcallhistory == 0, reason="wetalk call history for account user on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00006_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for account user on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory_URL + globalvar.userName + "?page=" + globals.page + "&pageSize=" + globals.pageSize
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for account user on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

# -----Read call history for account(initiated by)--custom date range----
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00007_wetalkcallhistory == 0, reason="wetalk call history for account user in custom date range on portal  is skipped")
@pytest.mark.negativetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10387)
def test_tc_00007_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for account user in custom date range on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory_URL + globalvar.userName + "?page=" + globals.page \
                  + "&pageSize=" + globals.pageSize+"&from="+ globals.startdate +"&to ="+ globals.enddate
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200 
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for account user in custom date range on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history for account user in custom date range on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

# -----Read call history for account(initiated by)--Today date ----
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00008_wetalkcallhistory == 0, reason="wetalk call history for account user with today date on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10389)
def test_tc_00008_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for account user with today date on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory_URL + globalvar.userName + "?page=" \
                  + globals.page + "&pageSize=" + globals.pageSize +globals.todaydate
        print(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200 
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for account user with today date on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history for account user with today date on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

# -----Read call history for account(initiated by)--Yesterday date ----
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00009_wetalkcallhistory == 0, reason="wetalk call history for account user with yesterday date on portal  is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10390)
def test_tc_00009_wetalkcallhistory(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk call history for account user with yesterday date on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + wetalkcallhistory_URL + globalvar.userName + "?page=" + globals.page \
                  + "&pageSize=" + globals.pageSize+ globals.yesterdaydate
        print(api_URL)
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200 
        WeGuard.logger.debug("\n\n---------------------------wetalk call history for account user with yesterday date on portal  PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history for account user with yesterday date on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False