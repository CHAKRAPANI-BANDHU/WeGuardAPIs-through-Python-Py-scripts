from datetime import datetime
import requests
import pytest
import globalvariables as globalvarX
import groupglobalvar as globalvars
import WeGuardlogger as WeGuard
import Validator as Executor
import WeBoxpayloadinfo as payload
import test_GETutils as utils

def url_formatter3(policyId):
    url3 = "enterprise/rest/weguard-v2/webox/config/{policyId}".format(policyId=policyId)
    return url3

#WeBoxAndroidPolicy = url_formatter3('5e69cc0e77f85d7c96b0d9d2')
WeBoxiOSPolicy = url_formatter3('5e8c5a0577f85d53bb4410ac')
undosave = 'enterprise/rest/weguard-v2/fcmUpdate'

#Get WeBox configs for iOS (Undo and Save)
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBox_undosave == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10184)
def test_tc_000001_undosave(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
  pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalvarX.BaseURL + undosave
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/undosave.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.undosave, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Undo and Save is passed ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 =datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Undo and Save is failed---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
# WeBox Android Policy GET
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBox_AndroidPolicy == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10186)
def test_tc_000001_WeBoxAndroidPolicy(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
    pytest.skip("Empty Bearer token Skipping test")
 try:
      for policyId in globalvars.android_policy_id:
        url3 = url_formatter3(policyId)
      apiUrl = globalvarX.BaseURL + url3
      Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
      res = requests.get(url=apiUrl, headers=Headers, timeout=globalvarX.timeout)
      curl_str1 = utils.getCurlEquivalent(res)
      WeGuard.logger.debug(curl_str1)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
      WeGuard.logger.debug("\n\n--------------------------- Android Policy configs ---------------------------")
      assert res.status_code == 200
 except BaseException as e:
      now2 =datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.error("\n\n--------------------------- No configs for Android Policy  ---------------------------\n\n")
      WeGuard.logger.error("Exception : " + str(e))
      assert False
# Post method for disabled "Allowdownload" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBox_AllowDownload == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10187)
def test_tc_000001_WeBoxAllowDownload(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledallowdownload.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledallowdownload, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- WeBoxAllowDownload ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBoxAllowDownload is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for disabled "AllowFileView" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBox_AllowFileView == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10188)
def test_tc_000001_WeBox_AllowFileView(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledallowfileview.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledallowfileview, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- WeBox_AllowFileView ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox_AllowFileView is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for disabled "Open With" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBox_OpenWith == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10189)
def test_tc_000001_WeBoxOpenWith(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledopenwith.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledopenwith, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- WeBox OpenWith ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox OpenWith is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for disabled "Show links" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBox_ShowLinks == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10190)
def test_tc_000001_WeBoxconfigsShowLinks(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledshowlinks.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledshowlinks, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- WeBox_ShowLinks ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox_ShowLinks is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for disabled "Allow Download, Allow file view, open with, Show links" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_noWeBoxConfigs == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10191)
def test_tc_000001_noWeBoxConfigs(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/noWeBoxConfigs.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.noWeBoxConfigs, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- disabled Allow Download, Allow file view, open with, Show links ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- disabled Allow Download, Allow file view, open with, Show links ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "Allow Download" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBoxEnabledAllowDownload == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10192)
def test_tc_000001_WeBoxEnabledAllowDownload(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledallowdownload.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledallowdownload, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- WeBoxEnabledAllowDownload ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- AllowDownload is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "Allow File View" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBoxEnabledAllowFileView == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10193)
def test_tc_000001_WeBoxEnabledAllowFileView(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledfileview.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledfileview, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     now1 = datetime.now()
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n---------------------------Enabled AllowFileView ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox_AllowFileView is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "OpenWith" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBoxEnabledOpenWith == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10194)
def test_tc_000001_WeBoxEnabledOpenWith(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledopenwith.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledopenwith, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- EnabledOpenWith ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox_ShowLinks is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "ShowLinks" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBoxEnabledShowLinks == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10195)
def test_tc_000001_WeBoxEnabledShowLinks(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledshowlinks.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledshowlinks, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- EnabledShowLinks ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox_ShowLinks is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Disabled "ServiceTypes" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_WeBoxDisabledServiceTypes == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10196)
def test_tc_000001_WeBoxDisabledServiceTypes(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledservicetypes.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledservicetypes, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- DisabledServiceTypes ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox_DisabledServiceTypes is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Disabled "WeBoxPasscode" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_DisabledWeBoxPasscode == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10197)
def test_tc_000001_WeBoxDisabledWeBoxPasscode(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/disabledweboxpasscode.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.disabledweboxpasscode, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- DisabledWeBoxPasscode ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not DisabledWeBoxPasscode ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "WeBox Passcode" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_EnabledWeBoxPasscode == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10198)
def test_tc_000001_WeBoxEnabledWeBoxPasscode(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledweboxpasscode.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledweboxpasscode, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- EnabledWeBoxPasscode ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not EnabledWeBoxPasscode ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
#Post method for Disabled "WeBox Passcode" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_EnabledServiceTypes == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10199)
def test_tc_000001_WeBoxEnabledServiceTypes(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enabledservicetypes.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enabledservicetypes, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- EnabledServiceTypes ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- EnabledServiceTypes ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "Google Drive and Dropbox" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_EnabledGoogleDriveDropbox == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10200)
def test_tc_000001_WeBoxEnabledGoogleDriveDropbox(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enablegdrivedropbox.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enableddrivedropbox, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- EnabledGoogleDriveDropbox---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not EnabledGoogleDriveDropbox ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Enabled "SD card and Amazon S3" on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_EnabledSDcardAmazonS3 == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10201)
def test_tc_000001_WeBoxEnabledSDcardAmazonS3(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/enableds3sdcard.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.enableds3sdcard, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Enabled SD card and Amazon S3 ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not Enabled SD card and Amazon S3 ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False

#Post method for Adding a folder for SD Card on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AddingfoldersforSDcard == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10222)
def test_tc_000001_AddingfoldersforSDcard(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingSDCardFolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingSDCardFolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Created SD card folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not created SD card folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Adding a folder for Google Drive on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AddingfoldersforGoogleDrive == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10223)
def test_tc_000001_AddingfoldersforGoogleDrive(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingGoogleDrivefolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingGoogleDrivefolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Created Google Drive folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not created Google Drive folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AddingfoldersforAmazonS3 == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10224)
def test_tc_000001_AddingfoldersforAmazonS3(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingAmazonS3folder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingAmazonS3folder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Created Amazon S3 folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not created AmazonS3 folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AddingfoldersforDropbox == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10225)
def test_tc_000001_AddingfoldersforDropbox(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingDropboxfolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingDropboxfolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Created Dropbox folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not created Dropbox folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Disabled "SD card and Amazon S3" on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_DisabledSDcardAmazonS3 == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10226)
def test_tc_000001_WeBoxDisabledSDcardAmazonS3(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DisabledSDcardAmazonS3.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.DisabledSDcardAmazonS3, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Disabled SD card and Amazon S3 ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not Disabled SD card and Amazon S3 ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Disabled "Google Drive and Dropbox" on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_DisabledGoogleDriveDropbox == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10227)
def test_tc_000001_WeBoxDisabledGoogleDriveDropbox(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DisabledGoogleDriveDropbox.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.DisabledGoogleDriveDropbox, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Disabled Google Drive and Dropbox---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not Disabled Google Drive and Dropbox ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Adding a folder for SD Card on portal for Android Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AddingfoldersforSDcard == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10228)
def test_tc_000001_AddingfoldersforSDcard(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/AddingSDCardFolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.AddingSDCardFolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Created SD card folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not created SD card folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Deleting a folder for Google Drive on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_DeletingfoldersforGoogleDrive == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10229)
def test_tc_000001_DeletingfoldersforGoogleDrive(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DeletingGoogleDriveFolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.DeletingGoogleDriveFolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Deleted Google Drive folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not deleted Google Drive folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_DeletingfoldersforSDCard == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10230)
def test_tc_000001_DeletingfoldersforSDCard(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DeletingSDCardFolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.DeletingSDCardFolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Deleted SD Card folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not deleted SD Card folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Adding a folder for Amazon S3 on portal for Android/iOS Policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_DeletingfoldersforDropbox == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10231)
def test_tc_000001_DeletingfoldersforDropbox(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/DeletingDropboxFolder.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.DeletingDropboxFolder, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Deleted Dropbox folder successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not deleted Dropbox folder successfully ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_Webox_filespost == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10185)
def test_tc_000001_WeBoxfilespost(url):
 now1 = datetime.now()
 if globalvarX.bearerToken == '':
  pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvarX.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvarX.bearerToken)}
     # file1 = open("zAuditLogsWeBoxLogout/Payloadinfo/Weboxfiles.txt", "r")
     # req = json.loads(file1.read())
     res = requests.post(url=apiUrl, headers=Headers, json=payload.WeBoxFiles, timeout=globalvarX.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug(" Response code: " + str(res.status_code) + " apiUrl: " + apiUrl + " Response headers: " + str(res.headers) + " Request Payload: " + str(res.content))
     WeGuard.logger.debug("Response headers: " + str(res.headers) + "\n")
     WeGuard.logger.debug("\n\n--------------------------- WeBoxfilespost ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
      now2 =datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.error("\n\n--------------------------- WeBoxfilespost---------------------------\n\n")
      WeGuard.logger.error("Exception : " + str(e))
      assert False