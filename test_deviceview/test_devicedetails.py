import pytest
import requests
from _datetime import datetime
import globalvariables2 as var
import globalvariables as globals1
from test_vars import payloads as globals,layouts as validations
import WeGuardlogger as WeGuard
import test_GETutils as utils

from ALogin_Dashboard_Devices import test_ALogin

test_ALogin.test_tc_001_login('url')

WeGuard.logger.debug("Devices view page APIs")

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_apps == 0, reason="device apps in device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.run(order=10041)
# test case is to get apps using deviceID for active/marked lost/marked stolen/marked replaced device
def test_tc_00001_apps(url):
    WeGuard.logger.error("\n\n--------------------------- Device apps in device details  ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.get_apps_URL + deviceid
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            res = requests.get(url=api_URL, headers=headers, timeout=globals1.timeout)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + api_URL + "\n Response: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
                WeGuard.logger.debug("\n\n---------------------------  Device apps in device details PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Device apps in device details FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url',[""])
@pytest.mark.skipif(validations.run_test_tc_00002_notes == 0, reason="Verifying notes in device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10043)
def test_tc_00002_notes(url):
    WeGuard.logger.error("\n\n--------------------------- Notes in device details ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.notes_URL + "/" + deviceid
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            res = requests.get(url= api_URL, headers=headers, timeout=globals1.timeout)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug(
                "\n Response code: " + str(res.status_code) + "\n apiUrl: " + api_URL + "\n Response Headers: " + str(
                    res.headers) + "\n Response: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
                WeGuard.logger.debug("\n\n---------------------------  Notes in device details PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Notes in device details FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_update == 0, reason="fcm update in devices details view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10040)
def test_tc_00001_fcm_update(url):
    WeGuard.logger.error("\n\n--------------------------- Devices view FCM update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.fcm_URL
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            fcm_update = {
                "topic": deviceid + "_" + globals1.actcode + "_" + globals1.pactcode,
                "type": "FCM_UPDATE",
                "isLicenseLevel": False,
                "pId": "5e9958fb77f85d51483d01fa",
                "actCode": globals1.actcode,
                "pActCode": globals1.pactcode,
                "priority": "high"
            }
            res = requests.post(url= api_URL, json= fcm_update, headers=headers, timeout=globals1.timeout)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + api_URL + "\n Response: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
                WeGuard.logger.debug("\n\n--------------------------- Devices view FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Devices view FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations. run_test_tc_00001_fcm_device_lock == 0, reason="Work Managed/Work profile 'Device lock' fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10050)
def test_tc_00001_fcm_device_lock(url):
    WeGuard.logger.error("\n\n---------------------------Work Managed/work profile 'Device lock' fcm update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == ("ANDROID_WM" or "ANDROID_BYOD"):
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_remoteview, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Work Managed/Work profile 'Device lock' fcm update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n-------------------------- Work Managed/work profile 'Device lock' fcm update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_Kiosk_unlock == 0, reason="kiosk unlock command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10046)
def test_tc_00001_fcm_Kiosk_unlock(url):
    WeGuard.logger.error("\n\n--------------------------- Kiosk unlock command FCM update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.kiosk_unlock, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n---------------------------  Kiosk unlock command FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Kiosk unlock command FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_Kiosk_unlock_events == 0, reason="kiosk unlock command events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10045)
def test_tc_00001_Kiosk_unlock_events(url):
    WeGuard.logger.error("\n\n--------------------------- Kiosk unlock command events ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK':
                    api_URL = globals1.BaseURL + globals.events_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.kiosk_unlock_events, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Kiosk unlock command events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Kiosk unlock command events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_Kiosk_lock == 0, reason="kiosk lock command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10048)
def test_tc_00001_fcm_Kiosk_lock(url):
    WeGuard.logger.error("\n\n--------------------------- Kiosk lock command FCM update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_kiosk_lock, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n---------------------------  Kiosk lock command FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Kiosk lock command FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_Kiosk_lock_events == 0, reason="kiosk lock command events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10049)
def test_tc_00001_Kiosk_lock_events(url):
    WeGuard.logger.error("\n\n--------------------------- Kiosk lock command events ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK':
                    api_URL = globals1.BaseURL + globals.events_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.kiosk_lock_events, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Kiosk lock command events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Kiosk lock command events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_admin_lock == 0, reason="Admin lock command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10051)
def test_tc_00001_fcm_admin_lock(url):
    WeGuard.logger.error("\n\n--------------------------- Admin lock command FCM update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == ('ANDROID_KIOSK' or 'ANDROID_WM'):
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_admin_lock, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n---------------------------  Admin lock command FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Admin lock command FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_admin_lock_events == 0, reason="Admin lock command events is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10049)
def test_tc_00001_admin_lock_events(url):
    WeGuard.logger.error("\n\n--------------------------- Admin lock command events ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == ('ANDROID_KIOSK'or'ANDROID_WM'):
                    api_URL = globals1.BaseURL + globals.events_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.admin_lock_events, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Admin lock command events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Admin lock command events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_admin_unlock == 0, reason="Admin unlock command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10052)
def test_tc_00001_fcm_admin_unlock(url):
    WeGuard.logger.error("\n\n--------------------------- Admin unlock command FCM update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK'or'ANDROID_WM':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_admin_unlock, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Admin unlock command FCM update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Admin unlock command FCM update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_admin_unlock_events == 0, reason="Admin unlock command events is skipped ")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10051)
def test_tc_00001_admin_unlock_events(url):
    WeGuard.logger.error("\n\n--------------------------- Admin unlock command events ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK'or'ANDROID_WM':
                    api_URL = globals1.BaseURL + globals.events_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.admin_unlock_events, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Admin unlock command events PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Admin unlock command events FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_device_wipe == 0, reason="Device wiped command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10055)
def test_tc_00001_fcm_device_wipe(url):
    WeGuard.logger.error("\n\n--------------------------- Device wiped command fcm update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK'or 'ANDROID_WM'or'ANDROID_BYOD':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_wipe_device, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n---------------------------  Device wiped command fcm update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Device wiped command fcm update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_device_wakeup == 0, reason="Device wakeup command fcm update for offline device is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10053)
def test_tc_00001_fcm_device_wakeup(url):
    WeGuard.logger.error("\n\n--------------------------- Device wakeup command fcm update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.fcm_URL
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            res = requests.post(url=api_URL, json=globals.fcm_device_wakeup, headers=headers, timeout=globals1.timeout)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + api_URL + "\n Response: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
                WeGuard.logger.debug("\n\n---------------------------  Device wakeup command fcm update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Device wakeup command fcm update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_device_reboot == 0, reason="Device reboot command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10045)
def test_tc_00001_fcm_device_reboot(url):
    WeGuard.logger.error("\n\n--------------------------- Device reboot command fcm update--------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK'or'ANDROID_WM'or'ANDROID_BYOD':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_reboot, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Device reboot command fcm update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Device reboot command fcm update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_device_poweroff == 0, reason="Device power off command fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10057)
def test_tc_00001_fcm_device_poweroff(url):
    WeGuard.logger.error("\n\n--------------------------- Device power off command fcm update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK' or 'ANDROID_WM' or 'ANDROID_BYOD':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_poweroff, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n--------------------------- Device power off command fcm update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Device power off command fcm update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_fcm_force_stop_app == 0, reason="Force stop an app fcm update is skipped ")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10062)
def test_tc_00001_fcm_force_stop_app(url):
    WeGuard.logger.error("\n\n--------------------------- Force stop an app fcm update ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            for type in var.android_policyname:
                if type == 'ANDROID_KIOSK'or'ANDROID_WM'or'ANDROID_BYOD':
                    api_URL = globals1.BaseURL + globals.fcm_URL
                    headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
                    res = requests.post(url=api_URL, json=globals.fcm_forcestopapp, headers=headers, timeout=globals1.timeout)
                    curl_str1 = utils.getCurlEquivalent(res)
                    print(curl_str1)
                    WeGuard.logger.debug(
                        "\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                            res.request) + "\nBody: " + (str(res.request.body) if (
                                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(
                            res.content))
                    if res.status_code == 404:
                        print("----------Module not found-----------")
                    else:
                        assert res.status_code == 200
                        WeGuard.logger.debug("\n\n---------------------------  Force stop an app fcm update PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Force stop an app fcm update FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_notes == 0, reason="Adding general Notes in device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10042)
def test_tc_00001_notes(url):
    WeGuard.logger.error("\n\n--------------------------- Creating notes in device details  ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.notes_URL
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            res = requests.post(url=api_URL, json=globals.general_notes, headers=headers, timeout=globals1.timeout)
            WeGuard.logger.error(res.content)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + api_URL + "\n Response: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
                WeGuard.logger.debug("\n\n---------------------------  Creating notes in device details PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Creating notes in device details FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_updatedevice == 0, reason="updating tags/ids in device details view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.run(order=10063)
def test_tc_00001_updatedevice(url):
    WeGuard.logger.error("\n\n--------------------------- Update device with tags/ids ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.deviceupdate_URL
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            res = requests.post(url=api_URL, json=globals.update_device_tags_ids, headers=headers, timeout=globals1.timeout)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                res.request) + "\nBody: " + (str(res.request.body) if (
                    res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
            WeGuard.logger.debug("\n\n---------------------------  Update device with tags/ids PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Update device with tags/ids FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_broadcast_messagehistory_fordevice == 0, reason="verifying broadcast message history in device details view is skipped ")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.run(order=10042)
def test_tc_00001_broadcast_messagehistory_fordevice(url):
    WeGuard.logger.error("\n\n---------------------------Broadcast Message history per device  ---------------------------")
    now1 = datetime.now()
    if globals1.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        for deviceid in var.android_devices:
            api_URL = globals1.BaseURL + globals.device_broadcast_URL + deviceid + "?page="+ globals.page+ "&pageSize="+ globals.pageSize + "&type=FCM_MESSAGE"
            headers = {'Authorization': 'Bearer {}'.format(globals1.bearerToken)}
            res = requests.get(url=api_URL, headers=headers, timeout=globals1.timeout)
            curl_str1 = utils.getCurlEquivalent(res)
            print(curl_str1)
            WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + api_URL + "\n Response: " + str(res.content))
            if res.status_code == 404:
                print("----------Module not found-----------")
            else:
                assert res.status_code == 200
                WeGuard.logger.debug("\n\n--------------------------- Broadcast Message history per device PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n---------------------------Broadcast Message history per device FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

