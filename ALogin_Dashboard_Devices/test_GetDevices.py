import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import groupglobalvar as globalcheck
import test_GETutils as utils


def url_formatter(psize, page):
    url = "enterprise/rest/weguard-v2/getDevices?pageSize={pagize}&page={page}".format(pagize=psize, page=page)
    return url
def urlformatter(psize, page):
    url = "enterprise/rest/weguard-v2/devices/all?pageSize={pagize}&page={page}".format(pagize=psize, page=page)
    return url


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_get_devices== 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.usualtest
@pytest.mark.run(order=10016)
def test_tc_getdevices(url):
  if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
  try:
        getDevicesURL = url_formatter(globalcheck.pagesize_50, globalcheck.page_1)
        apiUrl = globalvar.BaseURL + getDevicesURL
        print("\n\n--------------------------- Devices ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        response = requests.get(url=apiUrl, headers={'Authorization': header})
        print(response.content)
        curl_str1 = utils.getCurlEquivalent(response)
        print(curl_str1)
        deviceslist = json.loads(response.content)['entity']['enterprise']
        androiddeviceCount = json.loads(response.content)['entity']['enterpriseDeviceCount']
        iOSdeviceCount = json.loads(response.content)['entity']['iosDeviceCount']
        print(androiddeviceCount)
        print(iOSdeviceCount)
        # Android devices to get based on policy type
        if androiddeviceCount != 0:
            devicetype1 = []
            deviceids1 = []
            for policy in deviceslist:
                devicetype1.append(policy.get('policyType'))
                deviceids1.append(policy.get('deviceID'))
            merged_list2 = [(devicetype1[i], deviceids1[i]) for i in range(0, len(devicetype1))]
            globalcheck.android_devices = deviceids1
            Not_none_values = filter(None.__ne__,globalcheck.android_devices)
            globalcheck.android_devices = list(Not_none_values)
            for key, value in merged_list2:
                if key == 'ANDROID_KIOSK':
                    globalcheck.kiosk_devices.append(value)
                elif key == 'ANDROID_WM':
                    globalcheck.wm_devices.append(value)
                else:
                    globalcheck.wp_devices.append(value)
            Not_none_values = filter(None.__ne__, globalcheck.kiosk_devices)
            globalcheck.kiosk_devices = list(Not_none_values)
            Not_none_values = filter(None.__ne__, globalcheck.wm_devices)
            globalcheck.wm_devices = list(Not_none_values)
            Not_none_values = filter(None.__ne__, globalcheck.wp_devices)
            globalcheck.wp_devices = list(Not_none_values)
        else:
            print("No Android devices in the account")

        # to get ios device ids based on policy type
        if iOSdeviceCount != 0:
            devicetype = []
            deviceids = []
            for deviceTypeName in deviceslist:
                devicetype.append(deviceTypeName.get('type'))
                deviceids.append(deviceTypeName.get('serialNumber'))
            merged_list = [(devicetype[i], deviceids[i]) for i in range(0, len(devicetype))]
            globalcheck.iosdevices = deviceids
            for key, value in merged_list:
                if key == 'IOS_NONDEP':
                    globalcheck.non_dep_devices.append(value)
                else:
                    globalcheck.dep_devices.append(value)
            Not_none_values = filter(None.__ne__, globalcheck.non_dep_devices)
            globalcheck.non_dep_devices = list(Not_none_values)
            Not_none_values = filter(None.__ne__, globalcheck.dep_devices)
            globalcheck.dep_devices = list(Not_none_values)
        else:
            print("No ios devices in this account")
        print(globalcheck.android_devices)
        print(globalcheck.kiosk_devices)
        print(globalcheck.wp_devices)
        print(globalcheck.wm_devices)
        print(globalcheck.iosdevices)
        print(globalcheck.non_dep_devices)
        print(globalcheck.dep_devices)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert response.status_code == 200
  except BaseException as e:
        print(e)
        assert False

#getAllDevicesUrl = "enterprise/rest/weguard-v2/devices/all?pageSize=50&page=1"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_get_devices_size_50 == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.usualtest
@pytest.mark.run(order=10017)
def test_tc_009_getdevices(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        getAllDevicesUrl = urlformatter(globalcheck.pagesize_50,globalcheck.page_1)
        apiUrl = globalvar.BaseURL + getAllDevicesUrl
        print("\n\n--------------------------- Devices ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 009 Failed to get devices ---------------------------\n\n")
        assert False

#DevicesUrl1 = "enterprise/rest/weguard-v2/devices/all?pageSize=100&page=1"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_get_devices_size_100 == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.raretest
@pytest.mark.run(order=10018)
def test_tc_009_getdevices_Increment_size(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        DevicesUrl1 = urlformatter(globalcheck.pagesize_100,globalcheck.page_1)
        apiUrl = globalvar.BaseURL + DevicesUrl1
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 009 Failed to get devices ---------------------------\n\n")
        assert False

#DevicesUrl3 = "enterprise/rest/weguard-v2/devices/all?pageSize=200&page=1"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_get_devices_size_200 == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.raretest
@pytest.mark.run(order=10019)
def test_tc_009_getdevices_size_200(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        DevicesUrl3 = urlformatter(globalcheck.pagesize_200,globalcheck.page_1)
        apiUrl = globalvar.BaseURL + DevicesUrl3
        print("\n\n--------------------------- Devices ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 009 Failed to get devices ---------------------------\n\n")
        assert False

DevicesUrl2 = "enterprise/rest/weguard-v2/devices/all?pageSize=100&page=0"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_002_get_devices_size_100_size_0 == 0, reason=" test is skipped")
@pytest.mark.negativetest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.raretest
@pytest.mark.run(order=10020)
def test_tc_009_getdevices_Invalid_size(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        DevicesUrl2 = urlformatter(globalcheck.pagesize_100,globalcheck.page_0)
        apiUrl = globalvar.BaseURL + DevicesUrl2
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 009 Failed to get devices ---------------------------\n\n")
        assert False