from datetime import datetime
import requests
import pytest
import globalvariables as globalex
import WeGuardlogger as WeGuard
import Validator as Execute
import groupglobalvar as globalcheck
import test_GETutils as utils
import json
import WeBoxpayloadinfo as qa

events = 'enterprise/rest/weguard/logs/events'

def url_formatter5(actcode, page, limit):
    url5 = "enterprise/rest/weguard-v2/webox/upload/folder/{actcode}/shared?page={page}&limit={limit}".format(actcode=actcode, page=page, limit=limit)
    return url5

def url_formatter6(actcode, page, limit):
    url6 = "enterprise/rest/weguard-v2/webox/upload/folder/{actcode}/group?page={page}&limit={limit}".format(actcode=actcode, page=page, limit=limit)
    return url6

createglobalsharedpolicygroupsfolders='enterprise/rest/weguard-v2/webox/upload/folder/create'

config='enterprise/rest/weguard-v2/webox/upload/config'

def url_formatter7(policyId):
    url7 = 'enterprise/rest/weguard-v2/webox/upload/config/{policyId}/Policy'.format(policyId=policyId)
    return url7

def url_formatter8(foldername, page, limit, start, end):
    url8 = 'enterprise/rest/weguard-v2/webox/upload/files/shared/{foldername}?page={page}&limit={limit}&from={start}&to={end}'.format(foldername=foldername, page=page, limit=limit, start=start, end=end)
    return url8

def url_formatter9(policyId, foldername, page, limit, start, end):
    url9 = 'enterprise/rest/weguard-v2/webox/upload/files/policy/{policyId}/{foldername}?page={page}&limit={limit}&from={start}&to={end}'.format(policyId=policyId, foldername=foldername, page=page, limit=limit, start=start, end=end)
    return url9

def url_formatter10(foldername, page, limit):
    url10 = "enterprise/rest/weguard-v2/webox/upload/files/shared/{foldername}?page={page}&limit={limit}".format(foldername=foldername, page=page, limit=limit)
    return url10

def url_formatter11(policyId, foldername, page, limit):
    url11 = "enterprise/rest/weguard-v2/webox/upload/files/policy/{policyId}/{foldername}?page={page}&limit={limit}".format(policyId=policyId, foldername=foldername, page=page, limit=limit)
    return url11

def url_formatter12(actcode, pactcode):
    url12 = "enterprise/rest/weguard-v2/webox/upload/config/{actcode}/{pactcode}/Shared".format(actcode=actcode, pactcode=pactcode)
    return url12


#GET method to get Global shared folders is available in Device Uploads for Android policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_GlobalSharedFolders == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10232)
def test_tc_000001_SharedFolders(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     sharedgroupfolders = url_formatter5(globalex.actcode, globalcheck.page_1, globalcheck.pagesize_30)
     apiUrl = globalex.BaseURL + sharedgroupfolders
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Global shared folders are available in Device Uploads ---------------------------")
     qa.sharedfolderslist = json.loads(res.content)['entities']
     sharedfolderslist = []
# To get sharedgroupfolderslist (files in folders under shared group)
     for files in qa.sharedfolderslist:
         sharedfolderslist.append(files.get('name'))
     qa.sharedfolderslist = sharedfolderslist
     WeGuard.logger.debug(qa.sharedfolderslist)
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Global shared folders are not available in Device Uploads ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#GET method to get Policy Groups folders is available in Device Uploads for Android policy
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGroupsFolders == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.parametrize('url', [""])
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10233)
def test_tc_000001_PolicyGroupsFolders(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     policygroupfolders = url_formatter6(globalex.actcode, globalcheck.page_1, globalcheck.pagesize_30)
     apiUrl = globalex.BaseURL + policygroupfolders
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Policy Groups folders are available in Device Uploads ---------------------------")
     qa.policyfolderslist = json.loads(res.content)['entities']
     policyfolderslist = []
     for name in qa.policyfolderslist:
           policyfolderslist.append(name.get('name'))
     qa.policyfolderslist = policyfolderslist
     WeGuard.logger.debug(qa.policyfolderslist)
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Policy Groups folders are not available in Device Uploads ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method to create Global shared folders is available in Device Uploads for Android policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_CreateGlobalSharedFolders == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10234)
def test_tc_000001_CreateglobalsharedFolders(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalex.BaseURL + createglobalsharedpolicygroupsfolders
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     qa.createglobalfolders["actCode"] = globalex.actcode
     res = requests.post(url=apiUrl, headers=Headers, json=qa.createglobalfolders, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Global Shared folder created successfully ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Global Shared folder is failed to create ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method to create Policy Groups folders is available in Device Uploads for Android policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_CreatePolicyGroupsFolders == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10235)
def test_tc_000001_Createpolicygroupsfolders(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalex.BaseURL + createglobalsharedpolicygroupsfolders
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     qa.createpolicyfolders["policyId"] = globalcheck.android_policy_id[0],
     qa.createpolicyfolders["policyName"] = globalcheck.android_policyname
     qa.createpolicyfolders["policyType"] = globalcheck.policytype
     qa.createpolicyfolders["actCode"] = globalex.actcode
     res = requests.post(url=apiUrl, headers=Headers, json=qa.createpolicyfolders, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Policy Groups folder created successfully ---------------------------")
     if (res.status_code == 200):
        print("The request was a success!")
      # Code here will only run if the request is successful
     elif (res.status_code == 400):
        print("Result not found!")
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Policy Groups folder is failed to create ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#GET method for WeBox upload configs in policy groups and global shared folder under Device Uploads for Android policy
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_WeBoxuploadconfigingroupsfolder == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10236)
def test_tc_000001_WeBoxuploadconfigingroupfolder(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalcheck.android_policy_id:
         WeBoxuploadconfigingroupsfolder = url_formatter7(policyId)
         #WeBoxuploadconfiginpolicygroupsfolder = url_formatter7(globalcheck.android_policy_id[0])
         apiUrl = globalex.BaseURL + WeBoxuploadconfigingroupsfolder
         Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
         res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
         curl_str1 = utils.getCurlEquivalent(res)
         WeGuard.logger.debug(curl_str1)
         WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
         print("\n\n--------------------------- WeBox upload configs in policy groups folder available---------------------------")
         assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Not available WeBox upload configs in policy groups folder ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Policy Groups Folders WeBox upload config without sign
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGorupFolders_WeBoxuploadconfigwithoutsign == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10237)
def test_tc_000001_PolicyGroupsFoldersWeBoxuploadconfigwithoutsign(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalex.BaseURL + config
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     #qa.PolicygroupconfigwithoutSign["policyId"] = globalcheck.android_policy_id[0]
     res = requests.post(url=apiUrl, headers=Headers, json=qa.PolicygroupconfigwithoutSign, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Policy Groups Folders WeBox upload config without sign passed ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Policy Groups Folders WeBox upload config without sign failed ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Policy Groups Folders WeBox upload config with sign
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGorupFolders_WeBoxuploadconfigwithsign == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10238)
def test_tc_000001_PolicyGroupsFoldersWeBoxuploadconfigwithsign(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalex.BaseURL + config
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     #qa.PolicygroupconfigwithSign["policyId"] = globalcheck.android_policy_id[0]
     res = requests.post(url=apiUrl, headers=Headers, json=qa.PolicygroupconfigwithSign, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Policy Groups Folders WeBox upload config with sign passed ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- WeBox upload config with sign failed ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Shared FoldersWeBox upload config without sign
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithoutsign == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10181)
def test_tc_000001_SharedFoldersWeBoxuploadconfigwithoutsign(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalex.BaseURL + config
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     res = requests.post(url=apiUrl, headers=Headers, json=qa.SharedFolderconfigwithoutSign, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Shared Folders WeBox upload config without sign passed  ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Shared Folders WeBox upload config without sign failed ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#Post method for Shared Folders WeBox upload config with sign
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithsign == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10185)
def test_tc_000001_SharedFoldersWeBoxuploadconfigwithsign(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     apiUrl = globalex.BaseURL + config
     Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
     qa.SharedFolderconfigwithSign["activationCode"] = globalex.actcode
     res = requests.post(url=apiUrl, headers=Headers, json=qa.SharedFolderconfigwithSign, timeout=globalex.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     print("\n\n--------------------------- Shared Folders WeBox upload config with sign passed ---------------------------")
     assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Shared Folders WeBox upload config with sign failed ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#GET method to view WeBox upload files in policy for global shared folders
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_GlobalSharedFolders_viewfilesinsharedfolder == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10239)
def test_tc_000001_ViewFilesinSharedFolderafterclickingeyeicon(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for name in qa.sharedfolderslist:
         viewfoldersinsharedfolder = url_formatter8(name, globalcheck.page_1, globalcheck.pagesize_100, qa.isostart, qa.isoend)
         apiUrl = globalex.BaseURL + viewfoldersinsharedfolder
         Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
         res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
         curl_str1 = utils.getCurlEquivalent(res)
         WeGuard.logger.debug(curl_str1)
         WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
         print("\n\n--------------------------- Files are available in globals shared folder ---------------------------")
         assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Files are not available in globals shared folder ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#GET method to view WeBox upload files in policy for policy group folders
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGroupsFolders_viewfilesinpolicyfolder == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10240)
def test_tc_000001_ViewFilesinPolicyFoldersafterclickingoneyeicon(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalcheck.android_policy_id:
         for name in qa.policyfolderslist:
             viewfilesinpolicyfolders = url_formatter9(policyId, name, globalcheck.page_1, globalcheck.pagesize_100, qa.isostart, qa.isoend)
             #viewfilesinpolicyfolders = url_formatter9(globalcheck.android_policy_id[0], 'AI Documents', globalcheck.page_1, globalcheck.pagesize_100, qa.isostart, qa.isoend)
             apiUrl = globalex.BaseURL + viewfilesinpolicyfolders
             Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
             res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
             curl_str1 = utils.getCurlEquivalent(res)
             print(curl_str1)
             WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
             print("\n\n--------------------------- Files are available in policy groups folder ---------------------------")
             assert res.status_code == 200
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Files are not available in policy groups folder ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False
#GET method to view files in policy for global shared folders upon clicking on clear
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_GlobalSharedFolders_filesbyclickingonclearinsharedfolders == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10241)
def test_tc_000001_FilesinGlobalSharedFolders(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for name in qa.sharedfolderslist:
         sharedgroupfiles = url_formatter10(name, globalcheck.page_1, globalcheck.pagesize_100)
         apiUrl = globalex.BaseURL + sharedgroupfiles
         Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
         res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
         curl_str1 = utils.getCurlEquivalent(res)
         WeGuard.logger.debug(curl_str1)
         WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
         print("\n\n--------------------------- Files are available upon clicking on clear in group shared folders ---------------------------")
         assert res.status_code == 200
 except BaseException as e:
         now2 = datetime.now()
         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
         WeGuard.logger.error("\n\n--------------------------- Files are not available upon clicking on clear in group shared folders ---------------------------\n\n")
         WeGuard.logger.error("Exception : " + str(e))
         assert False
#GET method to view files in policy for policy group folders upon clicking on clear
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_PolicyGroupsFolders_filesbyclickingonclearinpolicyfolders == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10242)
def test_tc_000001_FilesinPolicyGroupFolders(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalcheck.android_policy_id:
         for name in qa.policyfolderslist:
             policygroupfiles = url_formatter11(policyId, name, globalcheck.page_1, globalcheck.pagesize_100)
         #policygroupfiles = url_formatter11(globalcheck.android_policy_id[0], 'AI Documents', globalcheck.page_1, globalcheck.pagesize_100)
             apiUrl = globalex.BaseURL + policygroupfiles
             Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
             res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
             curl_str1 = utils.getCurlEquivalent(res)
             print(curl_str1)
             WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
             print("\n\n--------------------------- Files are available upon clicking on clear in policy group folders ---------------------------")
             assert res.status_code == 200
 except BaseException as e:
             now2 = datetime.now()
             WeGuard.logger.warning("Time taken: " + str(now2 - now1))
             WeGuard.logger.error("\n\n--------------------------- Files are not available upon clicking on clear in policy group folders ---------------------------\n\n")
             WeGuard.logger.error("Exception : " + str(e))
             assert False
#GET method to configs of shared folders upon clicking on setting icon(view config)
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_DeviceUploads_SharedFolders_config == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10244)
def test_tc_000001_SharedFoldersConfig(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
         sharedgroupconfig = url_formatter12(globalex.actcode, globalex.pactcode)
         apiUrl = globalex.BaseURL + sharedgroupconfig
         Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
         res = requests.get(url=apiUrl, headers=Headers, timeout=globalex.timeout)
         curl_str1 = utils.getCurlEquivalent(res)
         WeGuard.logger.debug(curl_str1)
         WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
         print("\n\n--------------------------- Get the configs of Shared Folders Pass ---------------------------")
         assert res.status_code == 200
 except BaseException as e:
         now2 = datetime.now()
         WeGuard.logger.warning("Time taken: " + str(now2 - now1))
         WeGuard.logger.error("\n\n--------------------------- Get the configs of Shared Folders Pass Fail ---------------------------\n\n")
         WeGuard.logger.error("Exception : " + str(e))
         assert False
#POST method to download pdf
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_WeBox_DeviceUploads_pdf== 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10243)
def test_tc_000001_DownloadPDF(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
             pdf = 'uploader/download/pdf'
             apiUrl = globalex.BaseURL + pdf
            # compact_obj = json.dumps(qa.pdf)
             Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
             res = requests.post(url=apiUrl, headers=Headers, json=qa.pdf, timeout=globalex.timeout)
             curl_str1 = utils.getCurlEquivalent(res)
             print(curl_str1)
             WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + "\n" +" apiUrl: " + apiUrl + "\n" + " Response headers: " + str(res.headers) + "\n" + " Response : " + str(res.content))
             print("\n\n--------------------------- PDF file is downloaded successfully ---------------------------")
             assert res.status_code == 200
 except BaseException as e:
             now2 = datetime.now()
             WeGuard.logger.warning("Time taken: " + str(now2 - now1))
             WeGuard.logger.error("\n\n--------------------------- PDF file is not downloaded successfully ---------------------------\n\n")
             WeGuard.logger.error("Exception : " + str(e))
             assert False
#POST method to download zip
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Execute.test_tc_001_WeBox_DeviceUploads_zip == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.sprint19
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.webox
@pytest.mark.regressiontest
@pytest.mark.run(order=10447)
def test_tc_000001_DownloadZIP(url):
 now1 =datetime.now()
 if globalex.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
             zip = 'uploader/download/zip'
             apiUrl = globalex.BaseURL + zip
            # testing = jsonpickle.encode(qa.zip)
             Headers = {'Authorization': 'Bearer {}'.format(globalex.bearerToken)}
             res = requests.post(url=apiUrl, headers=Headers, json=qa.zip, timeout=globalex.timeout)
             curl_str1 = utils.getCurlEquivalent(res)
             print(curl_str1)
             WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + "\n" +" apiUrl: " + apiUrl + "\n" + " Response headers: " + str(res.headers) + "\n" + " Response : " + str(res.content))
             print("\n\n--------------------------- ZIP file is downloaded successfully ---------------------------")
             assert res.status_code == 200
 except BaseException as e:
             now2 = datetime.now()
             WeGuard.logger.warning("Time taken: " + str(now2 - now1))
             WeGuard.logger.error("\n\n--------------------------- ZIP file is not downloaded successfully ---------------------------\n\n")
             WeGuard.logger.error("Exception : " + str(e))
             assert False