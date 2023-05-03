import json
import pytest
import requests
from test_vars import payloads as globals, \
    layouts as validations, varsparam as globals1
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import test_GETutils as utils
from _datetime import datetime


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_getdevice == 0, reason=" all devices in devicespage  ")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.run(order=10040)
def test_tc_00001_getdevice(url):
    WeGuard.logger.error("\n\n---------------------------Broadcast Message history per device  ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + globals.getdevices_URL + "?page=" + globals.page + "&pageSize=" + globals.pageSize
        WeGuard.logger.error("\n\n--------------------------- Devices ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        deviceslist = json.loads(res.content)['entity']['enterprise']
        ids = []
        ids2 = []
        policytype = []
        for device in deviceslist:
            if ((device['deleted']) is False and (device['isProvisioned']) is True):
                ids.append(device.get('id15'))
                globals1.android_devices = ids
        for item in globals1.android_devices:
            if item == None:
                globals1.android_devices.remove(item)
        for device in deviceslist:
            policytype.append(device.get('policyType'))
            globals1.android_policytype = policytype
        for item in globals1.android_devices:
            if item == None:
                globals1.android_policytype.remove(item)
        for device in deviceslist:
            ids2.append(device.get('serialNumber'))
            globals1.iosdevices = ids2
        for item in globals1.iosdevices:
            if item == None:
                globals1.iosdevices.remove(item)
        WeGuard.logger.debug("\n apiUrl: " + apiUrl + "\n Method: " + res.request.method + "\n Request: " + str(res.request) + " Body: " + (str(res.request.body) if (res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(res.status_code) + " response headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.debug("Time taken: " + str(now2 - now1))
        WeGuard.logger.debug("Exception : " + str(e))
        pytest.fail("\n\n---------------------------Broadcast Message history per device FAIL ---------------------------\n\n")
        assert False