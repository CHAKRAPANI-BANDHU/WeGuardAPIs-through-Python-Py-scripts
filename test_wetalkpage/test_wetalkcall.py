import pytest
import requests
import payloads as globals, layouts as validations
import test_GETutils as utils
import WeGuardlogger as WeGuard
import globalvariables as globalvar
from _datetime import datetime
import test_jsonnames as jsonnames


Wetalkcallauthtoken_URL = "enterprise/rest/wetalk/video/authtoken"
WeGuard.logger.debug("Video call on portal APIs")

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalkcall_authtoken == 0, reason="wetalk video call from portal is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sanitytest
@pytest.mark.sprint19
@pytest.mark.run(order=10381)
def test_tc_00001_wetalkcall_authtoken(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk video call from portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + Wetalkcallauthtoken_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        call_authtoken = {
            jsonnames.ROOMID: "OPS_" + globalvar.userName + "_" + globals.calldeviceid + "_"+globals.WTtimestamp,
            jsonnames.IDENTIFY: jsonnames.OPS,
            jsonnames.ROOMTYPE: jsonnames.PEER_TO_PEER
        }
        res = requests.post(url=api_URL,json= call_authtoken,headers=headers, timeout=globalvar.timeout)
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
        WeGuard.logger.debug("\n\n--------------------------- wetalk video call from portal PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.debug("Time taken: " + str(now2 - now1))
        WeGuard.logger.debug("Exception : " + str(e))
        pytest.fail("\n\n--------------------------- wetalk video call from portal FAIL ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalkcall_fcm == 0, reason="wetalk video call fcm from portal is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sanitytest
@pytest.mark.sprint19
@pytest.mark.run(order=10383)
def test_tc_00001_wetalkcall_fcm(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk video call fcm from portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + Wetalkcallauthtoken_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        call_authtoken = {
                      jsonnames.TOPIC: "WT_"+globalvar.actcode+"_"+globalvar.pactcode+"_"+ globals.calldeviceid,
                      jsonnames.TYPE: jsonnames.VIDEOCALL,
                      jsonnames.LICENSELEVEL: False,
                      jsonnames.ACTCODE: globalvar.actcode,
                      jsonnames.PACTCODE: globalvar.pactcode,
                      jsonnames.MESSAGE: "OPS_" + globalvar.userName + "_" + globals.calldeviceid + "_"+globals.WTtimestamp,
                      jsonnames.TIMESTAMP: globals.timestamp
        }

        res = requests.post(url=api_URL,json= call_authtoken,headers=headers, timeout=globalvar.timeout)
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
        WeGuard.logger.debug("\n\n--------------------------- wetalk video call fcm from portal PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.debug("Time taken: " + str(now2 - now1))
        WeGuard.logger.debug("Exception : " + str(e))
        pytest.fail("\n\n--------------------------- wetalk video call fcm from portal FAIL ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalkcall_event == 0, reason="wetalk video call initiated event is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sanitytest
@pytest.mark.sprint19
@pytest.mark.run(order=10384)
def test_tc_00001_wetalkcall_event(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk video call initiated event ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + Wetalkcallauthtoken_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        initiated_event ={
                  jsonnames.AGENT: jsonnames.PORTAL,
                  jsonnames.ACTORID : globalvar.userName,
                  jsonnames.POLICYID: None,
                  jsonnames.TYPE: jsonnames.INFO,
                  jsonnames.MSG : "",
                  jsonnames.ACTION: jsonnames.CALL_STARTED,
                  jsonnames.EVENT: jsonnames.VIDEOCALLING,
                  jsonnames.TIMESTAMP:globals.timestamp,
                  jsonnames.SOURCEIP: "",
                  jsonnames.ACTCODE: globalvar.actcode,
                }
        res = requests.post(url=api_URL,json= initiated_event,headers=headers, timeout=globalvar.timeout)
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
        WeGuard.logger.debug("\n\n--------------------------- wetalk video call initiated event PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.debug("Time taken: " + str(now2 - now1))
        WeGuard.logger.debug("Exception : " + str(e))
        pytest.fail("\n\n--------------------------- wetalk video call initiated event FAIL ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_wetalkcall_event == 0, reason="wetalk video call end event is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sanitytest
@pytest.mark.sprint19
@pytest.mark.run(order=10385)
def test_tc_00002_wetalkcall_event(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk video call end event ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + Wetalkcallauthtoken_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        initiated_event ={
            jsonnames.AGENT: jsonnames.PORTAL,
            jsonnames.ACTORID: globalvar.userName,
            jsonnames.POLICYID: None,
            jsonnames.TYPE: jsonnames.INFO,
            jsonnames.MSG: globals.endmsg + globals.calldeviceid,
            jsonnames.ACTION: jsonnames.CALL_ENDED,
            jsonnames.EVENT: jsonnames.VIDEOCALLING,
            jsonnames.TIMESTAMP: globals.timestamp,
            jsonnames.SOURCEIP: "",
            jsonnames.ACTCODE: globalvar.actcode
        }
        res = requests.post(url=api_URL,json= initiated_event,headers=headers, timeout=globalvar.timeout)
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
        WeGuard.logger.debug("\n\n--------------------------- wetalk video call end event PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.debug("Time taken: " + str(now2 - now1))
        WeGuard.logger.debug("Exception : " + str(e))
        pytest.fail("\n\n--------------------------- wetalk video call end event FAIL ---------------------------\n\n")
        assert False