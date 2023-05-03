import pytest
import requests
from _datetime import datetime
from test_vars import payloads as globals, layouts as validations
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import globalvariables2 as var
import test_GETutils as utils


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_auth == 0, reason="Verifying auth for live view connection in device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10057)
def test_tc_00001_auth(url):
    WeGuard.logger.error("\n\n--------------------------- Live view Auth ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
         api_URL = globalvar.BaseURL + globals.auth_URL
         headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
         res = requests.get(url=api_URL, headers=headers, timeout=10)
         curl_str1 = utils.getCurlEquivalent(res)
         WeGuard.logger.debug(curl_str1)
         WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
         for deviceid in var.android_devices:
          var.android_devices.append(deviceid.get(var.kioskIds))
         assert res.status_code == 200
         WeGuard.logger.debug("\n\n---------------------------  Live view Auth Pass ---------------------------\n\n")
    except BaseException as e:
         now2 = datetime.now()
         WeGuard.logger.error('Error at %s', 'BaseException', 'e')
         WeGuard.logger.error("Time taken: " + str(now2 - now1))
         pytest.fail("\n\n--------------------------- Live view Auth FAIL ---------------------------\n\n")
         WeGuard.logger.error("Exception : " + str(e))
         assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_webrtc_stream == 0, reason="Initiating live view from device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10058)
def test_tc_00001_webrtc_stream(url):
    WeGuard.logger.error("\n\n--------------------------- Live view webrtc_stream  ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
            api_URL = globalvar.BaseURL + globals.webrct_stream_URL + globals.topic
            headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=api_URL, headers=headers, timeout=10)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
            for deviceid in var.android_devices:
                var.android_devices.append(deviceid.get(var.kioskIds))
            assert res.status_code == 200
            WeGuard.logger.debug("\n\n---------------------------  Live view webrtc_stream PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Live view webrtc_stream FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_screensharehistory == 0, reason="Started live view Screen share history in device detials view is skipped ")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10059)
def test_tc_00001_screensharehistory(url):
    WeGuard.logger.error("\n\n--------------------------- Started live view Screensharehistory  ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
            api_URL = globalvar.BaseURL + globals.screesharehistory_URL
            headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.post(url=api_URL, json=globals.screensharehistory_starteddata, headers=headers, timeout=10)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
            for deviceid in var.android_devices:
                var.android_devices.append(deviceid.get(var.kioskIds))
            assert res.status_code == 200
            WeGuard.logger.debug("\n\n---------------------------  Started live view Screensharehistory PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Started live view Screensharehistory  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_screensharehistory == 0, reason="Ended live view Screen share history in device detials view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10060)
def test_tc_00002_screensharehistory(url):
    WeGuard.logger.error("\n\n--------------------------- Ended live view Screensharehistory ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
            api_URL = globalvar.BaseURL + globals.screesharehistory_URL
            headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.post(url=api_URL, json=globals.screensharehistory_endeddata, headers=headers, timeout=10)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
            for deviceid in var.android_devices:
                var.android_devices.append(deviceid.get(var.kioskIds))
            assert res.status_code == 200
            WeGuard.logger.debug("\n\n---------------------------  Ended live view Screensharehistory PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Started live view Screensharehistory  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_screensharehistory == 0, reason="Aborted live view Screen share history in device detials view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10061)
def test_tc_00003_screensharehistory(url):
    WeGuard.logger.error("\n\n--------------------------- Aborted live view Screensharehistory ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
            api_URL = globalvar.BaseURL + globals.screesharehistory_URL
            headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.post(url=api_URL, json=globals.screensharehistory_aborted, headers=headers, timeout=10)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
            for deviceid in var.android_devices:
                var.android_devices.append(deviceid.get(var.kioskIds))
            assert res.status_code == 200
            WeGuard.logger.debug("\n\n---------------------------  Aborted live view Screensharehistory PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Aborted live view Screensharehistory  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_screensharehistory == 0, reason="Live view screen share history of device in device details view is skipped ")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10044)
def test_tc_00001_screensharehistory(url):
    WeGuard.logger.error("\n\n--------------------------- Screensharehistory(get) ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
            api_URL = globalvar.BaseURL + globals.screesharehistory_device_URL
            headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
            res = requests.get(url=api_URL, headers=headers, timeout=10)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
            for deviceid in var.android_devices:
                var.android_devices.append(deviceid.get(var.kioskIds))
            assert res.status_code == 200
            WeGuard.logger.debug("\n\n---------------------------  Screensharehistory(get) PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Screensharehistory(get) FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
