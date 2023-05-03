from datetime import datetime
import pytest
import requests
import globalvariables as XValues
import test_GETutils as utils
import groupglobalvar as globals
import WeGuardlogger as WeGuard
import Validator as Executors
import WeBoxpayloadinfo as variable

def url_formatter(accountId, start, end, page, size):
     url = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}".format(accountId=accountId, start=start, end=end, page=page, size=size)
     return url

def url_formatter2(accountId, start, end, page, size, type, level):
    url2 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}&level={level}".format(accountId=accountId, start=start, end=end, page=page, size=size, type=type,level=level)
    return url2

def url_formatter3(accountId, start, end, page, size, type):
    url3 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&type={type}".format(accountId=accountId, start=start, end=end, page=page, size=size, type=type)
    return url3

def url_formatter4(accountId, start, end, page, size, level, ack):
    url4 = "notification/rest/alert/account/{accountId}?start={start}&end={end}&page={page}&size={size}&level={level}&ack={ack}".format(accountId=accountId, start=start, end=end, page=page, size=size, level=level, ack=ack)
    return url4

# GET method to get crtical alerts that are not acknowledged by use after clicking on Alert notification icon
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_CriticalAlerts == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10448)
def test_tc_000001_UnacknowledgedCriticalAlerts(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
     pytest.skip("Empty Bearer token. Skipping test")
 try:
     UnacknowledgedCriticalAlerts = url_formatter4(XValues.accountId, variable.isomonth, variable.isoend, globals.page_1, globals.pagesize_10, 'CRITICAL', 'unread')
     apiUrl = XValues.BaseURL + UnacknowledgedCriticalAlerts
     Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
     res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     print(curl_str1)
     print(res.content)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n--------------------------- Displaying Unacknowledged Critical Alerts all alert types and levels ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     WeGuard.logger.error("Exception : " + str(e))
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.debug("\n--------------------------- Not displaying Unacknowledged Critical Alerts all alert types and levels ---------------------------\n")
     assert False
# GET method to GET all level and types alert notifications of Todays
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_TodaysAlerts == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10403)
def test_tc_000001_TodaysAlertsTypesLevelAll(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
     pytest.skip("Empty Bearer token. Skipping test")
 try:
     TodaysAlertsTypesLevelAll = url_formatter(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10)
     apiUrl = XValues.BaseURL + TodaysAlertsTypesLevelAll
     Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
     res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     print(curl_str1)
     print(res.content)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n--------------------------- Displaying Todays all alert types and levels ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     WeGuard.logger.error("Exception : " + str(e))
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.debug("\n--------------------------- Not displaying all alert types and levels ---------------------------\n")
     assert False
# GET method to GET all level and types alert notifications of Yesterday's
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_Yesterday== 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10444)
def test_tc_000001_YesterdaysAlertsTypesLevelAll(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
     pytest.skip("Empty Bearer token. Skipping test")
 try:
     AlertsTypesLevelAllYesterday = url_formatter(XValues.accountId, variable.isoyesterday, variable.isoend, globals.page_1, globals.pagesize_10)
     apiUrl = XValues.BaseURL + AlertsTypesLevelAllYesterday
     Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
     res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     print(curl_str1)
     print(res.content)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n--------------------------- Displaying Yesterday's all alert types and levels ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     WeGuard.logger.error("Exception : " + str(e))
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.debug("\n--------------------------- Not displaying all alert types and levels ---------------------------\n")
     assert False
# GET method to GET all level and types alert notifications of Custom Date Range
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_CustomDateRange == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10445)
def test_tc_000001_CustomDateRangeAlertsTypesLevelAll(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
     pytest.skip("Empty Bearer token. Skipping test")
 try:
     AlertsTypesLevelAllCustomDateRange = url_formatter(XValues.accountId, variable.isocustom, variable.isoend, globals.page_1, globals.pagesize_10)
     apiUrl = XValues.BaseURL + AlertsTypesLevelAllCustomDateRange
     Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
     res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     print(curl_str1)
     print(res.content)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n--------------------------- Displaying Custom Date Range all alert types and levels ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     WeGuard.logger.error("Exception : " + str(e))
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.debug("\n--------------------------- Not displaying all alert types and levels ---------------------------\n")
     assert False
# GET method to GET Alert notifications of type=Battery and level=Low
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_Battery_Low== 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10404)
def test_tc_000001_BatteryLow(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      BatteryLowAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'BATTERY', 'LOW')
      apiUrl = XValues.BaseURL + BatteryLowAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=Battery and level=Low ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=Battery and level=Low ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=Battery and level=Warning
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_Battery_Warning == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10405)
def test_tc_000001_BatteryWarning(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      BatteryWarningAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'BATTERY', 'WARNING')
      apiUrl = XValues.BaseURL + BatteryWarningAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.warning("\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + " \n Response headers: " + str(res.headers) + "\n Request Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=Battery and level=Warning ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=Battery and level=Warning ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=Battery and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_Battery_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10406)
def test_tc_000001_BatteryCritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      BatteryCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'BATTERY', 'CRITICAL')
      apiUrl = XValues.BaseURL + BatteryCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=Battery and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=Battery and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DATA_USAGE and level=Low
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DATA_USAGE_Low == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10407)
def test_tc_000001_DATA_USAGE_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DataUsageLowAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DATA_USAGE', 'LOW')
      apiUrl = XValues.BaseURL + DataUsageLowAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=Data Usage and level=Low ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=Data Usage and level=Low ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DATA_USAGE and level=Warning
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DATA_USAGE_Warning == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10408)
def test_tc_000001_DATA_USAGEWarning(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DataUsageWarningAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DATA_USAGE', 'WARNING')
      apiUrl = XValues.BaseURL + DataUsageWarningAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=Battery and level=Warning ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=Battery and level=Warning ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DATA_USAGE and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DATA_USAGE_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10409)
def test_tc_000001_DATA_USAGECritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DataUsageCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DATA_USAGE', 'CRITICAL')
      apiUrl = XValues.BaseURL + DataUsageCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DATA_USAGE and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DATA_USAGE and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=KIOSK_LOCKED and level=ALL
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_KIOSK_LOCKED_Regular == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10410)
def test_tc_000001_KIOSK_LOCKED_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      KioskLockedAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'KIOSK_LOCKED', 'ALL')
      apiUrl = XValues.BaseURL + KioskLockedAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=KIOSK_LOCKED and level=ALL ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=KIOSK_LOCKED and level=ALL ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=KIOSK_UNLOCKED and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_KIOSK_UNLOCKED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10411)
def test_tc_000001_KIOSK_UNLOCKED_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      KioskUnlockedCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'KIOSK_UNLOCKED', 'CRITICAL')
      apiUrl = XValues.BaseURL + KioskUnlockedCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=KIOSK_UNLOCKED and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=KIOSK_UNLOCKED and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=Admin_LOCKED and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_ADMIN_LOCKED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10412)
def test_tc_000001_ADMIN_LOCKEDCritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      AdminLockedCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'ADMIN_LOCKED', 'CRITICAL')
      apiUrl = XValues.BaseURL + AdminLockedCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=ADMIN_LOCKED and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=ADMIN_LOCKED and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_REBOOTED and level=ALL
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_REBOOTED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10413)
def test_tc_000001_DEVICE_REBOOTED_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceRebootedAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_REBOOTED', 'ALL')
      apiUrl = XValues.BaseURL + DeviceRebootedAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_REBOOTED and level=Low ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_REBOOTED and level=Low ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_WIPED and level=ALL
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_WIPED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10414)
def test_tc_000001_DEVICE_WIPED_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceWipedAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_WIPED', 'ALL')
      apiUrl = XValues.BaseURL + DeviceWipedAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_WIPED and level=ALL ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_WIPED and level=ALL ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_DELETED and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_DELETED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10415)
def test_tc_000001_DEVICE_DELETED_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceDeletedCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_DELETED', 'CRITICAL')
      apiUrl = XValues.BaseURL + DeviceDeletedCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_DELETED and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_DELETED and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=ROOTED_ENROLL and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_ROOTED_ENROLL_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10416)
def test_tc_000001_ROOTED_ENROLL_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      RootedDeviceEnrollCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'ROOTED_ENROLL', 'ALL')
      apiUrl = XValues.BaseURL + RootedDeviceEnrollCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=ROOTED_ENROLL and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=ROOTED_ENROLL and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=MEMORY_ALERT and level=Low
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_MEMORY_ALERT_Low == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10417)
def test_tc_000001_MEMORY_ALERT_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      MemoryLowAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'MEMORY_ALERT', 'LOW')
      apiUrl = XValues.BaseURL + MemoryLowAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=Low ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=Low ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=MEMORY_ALERT and level=Warning
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_MEMORY_ALERT_Warning == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10418)
def test_tc_000001_MEMORY_ALERTWarning(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      MemoryWarningAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'MEMORY_ALERT', 'WARNING')
      apiUrl = XValues.BaseURL + MemoryWarningAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=Warning ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=Warning ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=MEMORY_ALERT and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_MEMORY_ALERT_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10419)
def test_tc_000001_MEMORY_ALERTCritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      MemoryCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'MEMORY_ALERT', 'CRITICAL')
      apiUrl = XValues.BaseURL + MemoryCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DISC_USAGE and level=Low
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DISC_USAGE_Low == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10420)
def test_tc_000001_DISC_USAGE_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DiscUsageLowAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DISC_USAGE', 'LOW')
      apiUrl = XValues.BaseURL + DiscUsageLowAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DISC_USAGE and level=Low ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=Low ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DISC_USAGE and level=Warning
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DISC_USAGE_Warning == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10421)
def test_tc_000001_DISC_USAGEWarning(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DiscUsageWarningAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DISC_USAGE', 'WARNING')
      apiUrl = XValues.BaseURL + DiscUsageWarningAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DISC_USAGE and level=Warning ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=Warning ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DISC_USAGE and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DISC_USAGE_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10422)
def test_tc_000001_DISC_USAGECritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DiscUsageCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DISC_USAGE', 'CRITICAL')
      apiUrl = XValues.BaseURL + DiscUsageCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DISC_USAGE and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_FALLEN and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_FALLEN_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10423)
def test_tc_000001_DEVICE_FALLEN_Low(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceFallenCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_FALLEN', 'LOW')
      apiUrl = XValues.BaseURL + DeviceFallenCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_FALLEN and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_FALLEN and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_MARKED_REPLACED and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10424)
def test_tc_000001_DEVICE_MARKED_REPLACED_Critical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceMarkedAsReplacedCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_MARKED_REPLACED', 'CRITICAL')
      apiUrl = XValues.BaseURL + DeviceMarkedAsReplacedCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_MARKED_REPLACED and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_REPLACED and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_MARKED_LOST and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_MARKED_LOST_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10425)
def test_tc_000001_DEVICE_MARKED_LOSTCritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceMarkedAsLostCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_MARKED_LOST', 'CRITICAL')
      apiUrl = XValues.BaseURL + DeviceMarkedAsLostCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_MARKED_LOST and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_LOST and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=KIOSK_LOCKED and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10426)
def test_tc_000001_DEVICE_MARKED_STOLENCritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceMarkedAsStolenCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_MARKED_STOLEN', 'CRITICAL')
      apiUrl = XValues.BaseURL + DeviceMarkedAsStolenCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_MARKED_STOLEN and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_STOLEN and level=Critical ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_CONNECTED_BACK and level=Critical
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10427)
def test_tc_000001_DEVICE_CONNECTED_BACKCritical(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DeviceConnectedBackCriticalAlert = url_formatter2(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_CONNECTED_BACK', 'CRITICAL')
      apiUrl = XValues.BaseURL + DeviceConnectedBackCriticalAlert
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_CONNECTED_BACK and level=Critical ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_CONNECTED_BACK and level=Critical ---------------------------\n")
      assert False
# Types are different and level is ALL
# GET method to GET Alert notifications of type=Battery and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_BATTERY_ALL== 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10428)
def test_tc_000001_BATTERY_ALL(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      BATTERYALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'BATTERY')
      apiUrl = XValues.BaseURL + BATTERYALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=Battery and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=Battery and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=KIOSK_LOCKED and level=Warning
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DATA_USAGE_Warning == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10429)
def test_tc_000001_DATA_USAGE(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DATA_USAGEALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DATA_USAGE')
      apiUrl = XValues.BaseURL + DATA_USAGEALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DATA_USAGE and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DATA_USAGE and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=KIOSK_LOCKED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_KIOSK_LOCKED== 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10430)
def test_tc_000001_KIOSK_LOCKED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      KIOSK_LOCKEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'KIOSK_LOCKED')
      apiUrl = XValues.BaseURL + KIOSK_LOCKEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=KIOSK_LOCKED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=KIOSK_LOCKED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=KIOSK_UNLOCKED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_KIOSK_UNLOCKED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10431)
def test_tc_000001_KIOSK_UNLOCKED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      KIOSK_UNLOCKEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'KIOSK_UNLOCKED')
      apiUrl = XValues.BaseURL + KIOSK_UNLOCKEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=KIOSK_UNLOCKED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=KIOSK_UNLOCKED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=ADMIN_LOCKED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_ADMIN_LOCKED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10432)
def test_tc_000001_ADMIN_LOCKED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      ADMIN_LOCKEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'ADMIN_LOCKED')
      apiUrl = XValues.BaseURL + ADMIN_LOCKEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=ADMIN_LOCKED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=ADMIN_LOCKED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_REBOOTED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_REBOOTED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10433)
def test_tc_000001_DEVICE_REBOOTED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_REBOOTEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_REBOOTED')
      apiUrl = XValues.BaseURL + DEVICE_REBOOTEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_REBOOTED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_REBOOTED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_WIPED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_WIPED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10434)
def test_tc_000001_DEVICE_WIPED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_WIPEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_WIPED')
      apiUrl = XValues.BaseURL + DEVICE_WIPEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_WIPED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_WIPED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_DELETED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_DELETED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10435)
def test_tc_000001_KIOSK_DEVICE_DELETED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_DELETEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_DELETED')
      apiUrl = XValues.BaseURL + DEVICE_DELETEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_DELETED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_DELETED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=ROOTED_ENROLL and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_ROOTED_ENROLL_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10436)
def test_tc_000001_ROOTED_ENROLL(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      ROOTED_ENROLLALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'ROOTED_ENROLL')
      apiUrl = XValues.BaseURL + ROOTED_ENROLLALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=ROOTED_ENROLL and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=ROOTED_ENROLL and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=MEMORY_ALERT and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_MEMORY_ALERT_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10437)
def test_tc_000001_MEMORY_ALERT(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      MEMORY_ALERTALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'MEMORY_ALERT')
      apiUrl = XValues.BaseURL + MEMORY_ALERTALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=MEMORY_ALERT and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=MEMORY_ALERT and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DISC_USAGE and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DISC_USAGE_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10438)
def test_tc_000001_DISC_USAGE(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DISC_USAGEALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DISC_USAGE')
      apiUrl = XValues.BaseURL + DISC_USAGEALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DISC_USAGE and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DISC_USAGE and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_FALLEN and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_FALLEN_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10439)
def test_tc_000001_DEVICE_FALLEN(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_FALLENALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_FALLEN')
      apiUrl = XValues.BaseURL + DEVICE_FALLENALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_FALLEN and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_FALLEN and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_MARKED_REPLACED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10440)
def test_tc_000001_DEVICE_MARKED_REPLACED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_MARKED_REPLACEDALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_MARKED_REPLACED')
      apiUrl = XValues.BaseURL + DEVICE_MARKED_REPLACEDALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_MARKED_REPLACED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_REPLACED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_MARKED_LOST and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_MARKED_LOST_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10441)
def test_tc_000001_DEVICE_MARKED_LOST(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_MARKED_LOSTALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_MARKED_LOST')
      apiUrl = XValues.BaseURL + DEVICE_MARKED_LOSTALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_MARKED_LOST and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_LOST and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_MARKED_STOLEN and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10442)
def test_tc_000001_DEVICE_MARKED_STOLEN(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_MARKED_STOLENALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_MARKED_STOLEN')
      apiUrl = XValues.BaseURL + DEVICE_MARKED_STOLENALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_MARKED_STOLEN and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_MARKED_STOLEN and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=DEVICE_CONNECTED_BACK and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_DEVICE_CONNECTED_BACK(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      DEVICE_CONNECTED_BACKALL = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'DEVICE_CONNECTED_BACK')
      apiUrl = XValues.BaseURL + DEVICE_CONNECTED_BACKALL
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=DEVICE_CONNECTED_BACK and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=DEVICE_CONNECTED_BACK and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=SIM_LOCK_CHANGED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_SIM_LOCK_CHANGED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_SIM_LOCK_CHANGED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      SIM_LOCK_CHANGED = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'SIM_LOCK_CHANGED')
      apiUrl = XValues.BaseURL + SIM_LOCK_CHANGED
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type = SIM_LOCK_CHANGED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type =SIM_LOCK_CHANGED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=RESET_PASSWORD and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_RESET_PASSWORD_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_RESET_PASSWORD(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      RESET_PASSWORD = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'RESET_PASSWORD')
      apiUrl = XValues.BaseURL + RESET_PASSWORD
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type = RESET_PASSWORD and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type = RESET_PASSWORD and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=SIM_REMOVED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_SIM_REMOVED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_SIM_REMOVED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      SIM_REMOVED = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'SIM_REMOVED')
      apiUrl = XValues.BaseURL + SIM_REMOVED
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=SIM_REMOVED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=SIM_REMOVED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=SIM_CHANGED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_SIM_CHANGED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_SIM_CHANGED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      SIM_CHANGED = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'SIM_CHANGED')
      apiUrl = XValues.BaseURL + SIM_CHANGED
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=SIM_CHANGED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=SIM_CHANGED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=SIM_ADDED and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_SIM_ADDED_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_SIM_ADDED(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      SIM_ADDED = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'SIM_ADDED')
      apiUrl = XValues.BaseURL + SIM_ADDED
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=SIM_ADDED and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=SIM_ADDED and level=All ---------------------------\n")
      assert False
# GET method to GET Alert notifications of type=UNINSTALL_WEGUARD and level=All
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executors.test_tc_001_AlertsModule_UNINSTALL_WEGUARD_Critical == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.alerts
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_tc_000001_UNINSTALL_WEGUARD(url):
 now1 =datetime.now()
 if XValues.bearerToken == '':
      pytest.skip("Empty Bearer token. Skipping test")
 try:
      UNINSTALL_WEGUARD = url_formatter3(XValues.accountId, variable.isostart, variable.isoend, globals.page_1, globals.pagesize_10, 'UNINSTALL_WEGUARD')
      apiUrl = XValues.BaseURL + UNINSTALL_WEGUARD
      Headers = {'Authorization': 'Bearer {}'.format(XValues.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=XValues.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      print(curl_str1)
      print(res.content)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n--------------------------- Alert notifications of type=UNINSTALL_WEGUARD and level=All ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      WeGuard.logger.error("Exception : " + str(e))
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.debug("\n--------------------------- Not available alert notifications of type=UNINSTALL_WEGUARD and level=All ---------------------------\n")
      assert False