import pytest
import requests
from _datetime import datetime
from test_vars import payloads as globals, layouts as validations
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalk_fcm_update == 0, reason="FCM update for all level wetalk message is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10370)
# fcm update for all level wetalk messages
def test_tc_00001_wetalk_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- FCM update for all level wetalk message ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        WeTalk_alllevel_fcm = {
            "topic": globals.wetalk_All_topic,
            "type": "Group",
            "isLicenseLevel": False,
            'actCode': globalvar.actcode,
            'pActCode': globalvar.pactcode,
            "message": "eyJtc2dQYXRoIjoiSFhIWEwvV0VMTC1MMENPNi9UaHJlYWRzIiwidGhyZWFkSWQiOiJOb3RpY2UgIEFsXzE1OTM2MjcyMTg0ODYiLCJzdWJqZWN0IjoiTm90aWNlIEFsbCIsInByaW9yaXR5IjoiTWVkaXVtIiwiaXNUaHJlYWQiOnRydWUsIm1lc3NhZ2UiOiJTdGF5IGhlYWx0aHkgYW5kIGZvY3VzZWQifQ=="
        }
        res = requests.post(url=api_URL, json=WeTalk_alllevel_fcm, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  FCM update for all level wetalk message PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- FCM update for all level wetalk message FAIL ---------------------------\n\n")
        WeGuard.logger.debug("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_wetalk_fcm_update == 0, reason="FCM update for group level wetalk message is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10371)
# fcm update for group level WeTalk message
def test_tc_00002_wetalk_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- FCM update for group level wetalk message ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        WeTalk_grouplevel_fcm = {
            "topic": globals.wetalk_group_topic,
            "type": "Group",
            "isLicenseLevel": False,
            'actCode': globalvar.actcode,
            'pActCode': globalvar.pactcode,
            "message": "eyJtc2dQYXRoIjoiSFhIWEwvV0VMTC1MMENPNi9UaHJlYWRzIiwidGhyZWFkSWQiOiJHcm91cCBOb3RpXzE1OTM2Mjc1MTg0MzIiLCJzdWJqZWN0IjoiR3JvdXAgTm90aWNlIiwicHJpb3JpdHkiOiJIaWdoIiwiaXNUaHJlYWQiOnRydWUsIm1lc3NhZ2UiOiJTdGF5IHNhZmUgYXQgaG9tZSJ9"
        }
        res = requests.post(url=api_URL, json=WeTalk_grouplevel_fcm, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  FCM update for group level wetalk message PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- FCM update for group level wetalk message FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_wetalk_fcm_update == 0, reason="FCM update for individual level wetalk message is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10372)
# fcm update for Individual device level WeTalk message
def test_tc_00003_wetalk_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- FCM update for individual level wetalk message ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        WeTalk_devicelevel_fcm = {
            "topic": globals.wetalk_device_topic,
            "type": "Individual",
            "isLicenseLevel": False,
            'actCode': globalvar.actcode,
            'pActCode': globalvar.pactcode,
            "message": "eyJtc2dQYXRoIjoiSFhIWEwvV0VMTC1MMENPNi9UaHJlYWRzIiwidGhyZWFkSWQiOiJEZXZpY2UgTm90XzE1OTM2Mjc2NzkxMjYiLCJzdWJqZWN0IjoiRGV2aWNlIE5vdGljZSIsInByaW9yaXR5IjoiSGlnaCIsImlzVGhyZWFkIjp0cnVlLCJtZXNzYWdlIjoiU3RheSBoZWFsdGh5In0="
        }
        res = requests.post(url=api_URL, json=WeTalk_devicelevel_fcm, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  FCM update for individual level wetalk message PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- FCM update for individual level wetalk message FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalk_events == 0, reason="All level wetalk message events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10373)
# creating WeTalk message and sending to all devices in admin account
def test_tc_00001_wetalk_events(url):
    WeGuard.logger.error("\n\n--------------------------- All level wetalk message events ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=api_URL, json=globals.wetalk_alllevel_event, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  All level wetalk message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- All level wetalk message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_wetalk_events == 0, reason="Group level wetalk message events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10374)
# creating WeTalk message and sending to policy group level devices in admin account
def test_tc_00002_wetalk_events(url):
    WeGuard.logger.error("\n\n--------------------------- Group level wetalk message events ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=api_URL, json=globals.wetalk_grouplevel_event, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Group level wetalk message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Group level wetalk message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_wetalk_events == 0, reason="Individual device level wetalk message events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10375)
# creating WeTalk message and sending to individual devices in admin account
def test_tc_00003_wetalk_events(url):
    WeGuard.logger.error("\n\n--------------------------- Individual device level wetalk message events ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=api_URL, json=globals.wetalk_devicelevel_event, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  Individual device level wetalk message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Individual device level wetalk message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00004_wetalk_complete_events == 0, reason="Completed wetalk message events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10376)
# creating WeTalk message and sending to individual devices in admin account
def test_tc_00004_wetalk_complete_events(url):
    WeGuard.logger.error("\n\n--------------------------- Completed wetalk message events ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_events_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.post(url=api_URL, json=globals.wetalk_complete_event, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- Completed wetalk message events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Completed wetalk message events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_searchdeviceid == 0, reason="Search imei for Individual device level wetalk message is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10377)
def test_tc_00001_searchdeviceid(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk search IMEI ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.Wetalk_search_URL + globals.wetalkparams
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- wetalk search IMEI PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk search IMEI FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_searchdevices_inwetalkpage == 0, reason="Searching devices in wetalkpage is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.run(order=10377)
def test_tc_00001_searchdevices_inwetalkpage(url):
    WeGuard.logger.error("\n\n--------------------------- Searching devices messages in wetalk page ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.searchdeviceid_URL + "?searchString=" + globals.imei + "&deviceType=" + globals.deviceType
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        print("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- Search devices messages in wetalk page PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Search devices message in wetalk page FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False