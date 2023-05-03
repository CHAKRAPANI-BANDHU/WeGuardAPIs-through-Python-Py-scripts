import json
import pytest
import requests
from test_vars import payloads as globals, \
    layouts as validations
from _datetime import datetime
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_broadcast_messagehistory == 0, reason="verifying of broadcast messages history in broadcast page is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10245)
def test_tc_00001_broadcast_messagehistory(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast message history ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.messagehistory_URL + "?page=" + globals.page + "&pageSize=" + globals.pageSize
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        messagehistory ={
            'actcode':globalvar.actcode,
            'pactcode':globalvar.pactcode,
            'type':globals.type
        }
        res = requests.post(url=api_URL, json=messagehistory, headers=headers, timeout=10)
        historylist = json.loads(res.content)['entity']['licenses']
        reqid=[]
        bc_devieid = []
        for reqID in historylist:
            reqid.append(reqID.get('reqID'))
            globals.reqID = reqid
        for BC_deviceID in historylist:
            reqid.append(BC_deviceID.get('deviceID'))
            globals.BC_deviceID = bc_devieid
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(historylist))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- Broadcast message history PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast message historyFAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.test_tc_00001_broadcast_messagehistory_withreqID == 0, reason="verifying broadcast message history of acknowledged devices is skipped ")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.run(order=10246)
def test_tc_00001_broadcast_messagehistory_withreqID(url):
    WeGuard.logger.error("\n\n---------------------------Broadcast Message history ack by device  ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        for reqID in globals.historylist:
            api_URL = globalvar.BaseURL + globals.msghis_devices_URL + reqID + "?page=" + globals.page + "&pageSize=" + globals.pageSize
            headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=api_URL, headers=headers, timeout=10)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
            assert res.status_code == 200
            WeGuard.logger.debug("\n\n--------------------------- Broadcast Message history ack by device PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n---------------------------Broadcast Message history ack by device FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_bc_searchdeviceid == 0, reason="Search string with device id in broadcast page is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10251)
def test_tc_00001_bc_searchdeviceid(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast search IMEI ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_url = globalvar.BaseURL + globals.searchimei_URL + "searchString=" + globals.imei + "&page=" + globals.page + "&pageSize=" + globals.pageSize
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_url, headers=headers, timeout=10)
        if res.content == b'{"successful":true,"result":"NO ENTRIES","statusCode":14,"entity":"","entities":[],"count":0}':
            print("\n-------Device is not available from :" + globalvar.userName + "-----------")
        else:
            BC_imei = json.loads(res.content)['entity']['devices'][0]['deviceID']
            pid = json.loads(res.content)['entity']['devices'][0]['policyId']
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug(
                "\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_url + " Response headers: " + str(
                    res.headers) + "\n" + " Request Payload: " + str(res.content))
            globals.BC_deviceid = BC_imei
            globals.pId = pid
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Broadcast search IMEI PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast search IMEI FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_bc_fcm_update == 0, reason="All level broadcast message fcm is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10247)
#fcm update for all level broadcast messages
def test_tc_00001_bc_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast All level message FCM update ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        bc_all_fcm = {'topic': globals.broadcast_All_topic,
                      'type': globals.type,
                      'isLicenseLevel': True,
                      'actCode':globalvar.actcode,
                      'pActCode':globalvar.pactcode,
                      'message': "{\"bgColor\":\"#000000\",\"textColor\":\"#ffffff\",\"title\":\"Notice all\",\"body\":\"Stay safe at home\"}",
                      'pId': None,
                      'priority': "high"}
        res = requests.post(url=api_URL, json=bc_all_fcm, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Broadcast All level message FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast All level message FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
#creating broadcast message and sending to all devices in admin account
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_bc_fcm_update == 0, reason="Group level broadcast message fcm is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10249)
# fcm update for group level WeTalk message
def test_tc_00002_bc_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast group level message FCM update ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        bc_group_fcm = {'topic': globals.broadcast_group_topic,
                        'type': globals.type,
                        'isLicenseLevel': True,
                        'actCode':globalvar.actcode,
                        'pActCode':globalvar.pactcode,
                        'message': "{\"bgColor\":\"#000000\",\"textColor\":\"#ffffff\",\"title\":\"Group Notice\",\"body\":\"Stay safe at home\"}",
                        'pId': globals.policyid ,
                        'priority': "high"}
        res = requests.post(url=api_URL, json=bc_group_fcm, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Broadcast group level message FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast group level message FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_bc_fcm_update == 0, reason="Individual device level broadcast message fcm is skipped")
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10252)
# fcm update for device level WeTalk message
def test_tc_00003_bc_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast device level message FCM update ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        bc_individual_fcm = {
            'topic': globals.broadcast_device_topic,
            'type': globals.type,
            'isLicenseLevel': False,
            'actCode': globalvar.actcode,
            'pActCode': globalvar.pactcode,
            'message': "{\"bgColor\":\"#000000\",\"textColor\":\"#ffffff\",\"title\":\"Device Notice\",\"body\":\"Stay safe at Home\"}",
            'pId': globals.pId,
            "priority": "high"
        }
        res = requests.post(url=api_URL, json=bc_individual_fcm, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Broadcast device level message FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast device level message FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_bc_events == 0, reason="All level broadcast message events is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.broadcast
@pytest.mark.run(order=10248)
# creating broadcast message and sending to all devices in admin account
def test_tc_00001_bc_events(url):
    WeGuard.logger.error("\n\n-------------------------- Broadcast All level message events ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_url = globalvar.BaseURL + globals.events_URL
        WeGuard.logger.error(api_url)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        bc_events1 = {
            'agent': "PORTAL",
            'actorId': globalvar.userName,
            'policyId': None,
            'type': "Info",
            'msg': '{\"title\":\"Message broadcasted to All\",\"body\":{\"topic\":\"'+globalvar.actcode+'_'+globalvar.pactcode+'\",\"type\":\"FCM_MESSAGE\",\"isLicenseLevel\":true,\"actCode\":\"'+globalvar.actcode+'\",\"pActCode\":\"'+globalvar.pactcode+'\",\"message\":\"{\\\"bgColor\\\":\\\"#000000\\\",\\\"textColor\\\":\\\"#ffffff\\\",\\\"title\\\":\\\"Notice all\\\",\\\"body\\\":\\\"Stay safe at home\\\"}\",\"pId\":null,\"priority\":\"high\"}}',
            'action': "-",
            'event': "Broadcast",
            'sentTime': 1593623039420,
            'sourceIP': ""
        }
        res = requests.post(url=api_url, json=bc_events1, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_url + " Response headers: " + str(
            res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Broadcast All level message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast All level message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_bc_events == 0, reason="Group level broadcast message events is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10250)
# creating WeTalk message and sending to policy group level devices in admin account
def test_tc_00002_bc_events(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast group level message events --------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_url = globalvar.BaseURL + globals.events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        bc_events2 = {
            'agent': "PORTAL",
            'actorId': globalvar.userName,
            'policyId': None,
            'type': "Info",
            'msg': "{\"title\":\"Message broadcasted to group Boston Users\",\"body\":{\"topic\":\"5e9958fb77f85d51483d01fa_HXHXL\",\"type\":\"FCM_MESSAGE\",\"isLicenseLevel\":true,\"actCode\":\"HXHXL\",\"pActCode\":\"WELL-L0CO6\",\"message\":\"{\\\"bgColor\\\":\\\"#000000\\\",\\\"textColor\\\":\\\"#ffffff\\\",\\\"title\\\":\\\"Group Notice\\\",\\\"body\\\":\\\"Stay safe at home\\\"}\",\"pId\":\"5e9958fb77f85d51483d01fa\",\"priority\":\"high\"}}",
            'action': "-",
            'event': "Broadcast",
            'sentTime': 1593623240376,
            'sourceIP': ""
        }
        res = requests.post(url=api_url, json=bc_events2, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_url + " Response headers: " + str(
            res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- Broadcast group level message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast group level message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_bc_events == 0, reason="Individual device level broadcast message events is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10253)
# creating WeTalk message and sending to individual devices in admin account
def test_tc_00003_bc_events(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast device level message events ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_url = globalvar.BaseURL + globals.events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        bc_events3 = {
            'agent': "PORTAL",
            'actorId': globalvar.userName,
            'policyId': None,
            'type': "Info",
            'msg': "{\"title\":\"Message broadcasted to device 5979869587579\",\"body\":{\"topic\":\"6467575768686_HXHXL_WELL-L0CO6\",\"type\":\"FCM_MESSAGE\",\"isLicenseLevel\":false,\"actCode\":\"HXHXL\",\"pActCode\":\"WELL-L0CO6\",\"message\":\"{\\\"bgColor\\\":\\\"#000000\\\",\\\"textColor\\\":\\\"#ffffff\\\",\\\"title\\\":\\\"Device Notice\\\",\\\"body\\\":\\\"Stay safe at Home\\\"}\",\"pId\":\"5e9958fb77f85d51483d01fa\",\"priority\":\"high\"}}",
            'action': "-",
            'event': "Broadcast",
            'sentTime': 1593623346677,
            'sourceIP': ""
        }
        res = requests.post(url=api_url, json=bc_events3, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_url + " Response headers: " + str(
            res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- Broadcast device level message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast device level message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_bc_uploadimage == 0, reason="upload image event is skipped")
@pytest.mark.positivetest
@pytest.mark.broadcast
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10254)
def test_tc_00001_bc_uploadimage(url):
    WeGuard.logger.error("\n\n--------------------------- Broadcast upload image event ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        upload_image = {
            "agent": "PORTAL",
            "actorId": globalvar.userName,
             "type": "Info",
             "msg": "{\"title\":\"logo[1].png is uploaded in undefined policy\"}",
             "action": "-",
             "event": "Upload",
             "sentTime": 1595508325799,
             "sourceIP": "",
             "activationCode": "0LY18"}
        res = requests.post(url=api_URL, json=upload_image, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Broadcast upload image event PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Broadcast upload image event FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False