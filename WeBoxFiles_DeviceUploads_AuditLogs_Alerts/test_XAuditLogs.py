from datetime import datetime
import requests
import pytest
import globalvariables as values
import WeGuardlogger as WeGuard
import WeBoxpayloadinfo as variable
import Validator as Executor
import test_GETutils as utils

def url_formatter(action, actorId, event, page, size, policyId, type, start, end):
    url = "enterprise/rest/weguard/logs/eventsByAction?action={action}&actorId={actorId}&event={event}&page={page}&pageSize={size}&policyId={policyId}&type={type}&startDate={start}&endDate={end}".format(action=action, actorId=actorId, event=event, page=page, size=size, policyId=policyId, type=type, start=start, end=end)
    return url

def url_formatter2(searchString, deviceType):
    url2 = "enterprise/rest/weguard-v2/searchimei?searchString={searchString}&deviceType={deviceType}".format(searchString=searchString, deviceType=deviceType)
    return url2

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyALL == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10257)
def test_tc_000001_filtersbyALL(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyALL = url_formatter('All', values.userName, '', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyALL
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------------------------- filtersbyeventsloglevelALL ---------------------------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------------------------- filtersbyeventsloglevelALL is failed ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoALL == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10258)
def test_tc_0003_filtersbyinfoALL(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoALL = url_formatter('All', values.userName, '', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoALL
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoALL--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoALL is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnALL == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10259)
def test_tc_0002_filtersbywarnALL(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnALL = url_formatter('All', values.userName, '', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnALL
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnALL--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydwarnALL is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorALL == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10260)
def test_tc_0004_filtersbyerrorALL(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorALL = url_formatter('All', values.userName, '', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorALL
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorALL--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorALL is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallLogin == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10261)
def test_tc_0005_filtersbyallLogin(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallLogin = url_formatter('All', values.userName, 'Login', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallLogin
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallLogin--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallLogin is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyalllogout == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10262)
def test_tc_0005_filtersbyalllogout(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyalllogout = url_formatter('All', values.userName, 'Logout', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyalllogout
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyalllogout--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyalllogout is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallSimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10263)
def test_tc_0005_filtersbyallSimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallSimper = url_formatter('All', values.userName, 'Start%20Impersonate', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallSimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallSimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallSimper is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallEimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10264)
def test_tc_0005_filtersbyallEimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallEimper = url_formatter('All', values.userName, 'End%20Impersonate', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallEimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallEimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallEimper is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyalldevice == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10265)
def test_tc_0005_filtersbyalldevice(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyalldevice = url_formatter('All', values.userName, 'Device', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyalldevice
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyalldevice--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyalldevice is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallgroups == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10266)
def test_tc_0005_filtersbyallgroups(url):
  now1 = datetime.now()
  if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
  try:
        filtersbyallgroups = url_formatter('All', values.userName, 'Group', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallgroups
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallgroups--------")
        assert res.status_code == 200
  except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallgroups is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallupload == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10267)
def test_tc_0005_filtersbyallupload(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallupload = url_formatter('All', values.userName, 'Upload', 1, 100, '', 'All', variable.start_timestamp,variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallupload
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallupload--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallupload is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallcommands == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10268)
def test_tc_0005_filtersbyallcommands(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallcommands = url_formatter('All', values.userName, 'Command', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallcommands
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallcommands--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallcommands is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallwetalk == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10269)
def test_tc_0005_filtersbyallwetalk(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallwetalk = url_formatter('All', values.userName, 'WeTalk', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallwetalk
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallwetalk--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallwetalk is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallweboxpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10270)
def test_tc_0005_filtersbyallweboxpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallweboxpass = url_formatter('All', values.userName, 'Webox%20passcode', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallweboxpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallweboxpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallweboxpass is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallkioskpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10271)
def test_tc_0005_filtersbyallkioskpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallkioskpass = url_formatter('All', values.userName, 'Kiosk%20passcode', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallkioskpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallkioskpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallkioskpass is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyAllyesterday == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10272)
def test_tc_0005_filtersbyAllyesterday(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyAllyesterday = url_formatter('All', values.userName, '', 1, 100, '', 'All', variable.yesterday_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyAllyesterday
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyAllyesterday--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyAllyesterday is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_searchAndroidimei == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10273)
def test_tc_0005_searchAndroidimei(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        searchAndroidimei = url_formatter2('358', 'android')
        apiUrl = values.BaseURL + searchAndroidimei
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------Android searchimei--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------Android searchimei is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_searchiOSimei == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10274)
def test_tc_0005_searchiOSimei(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        searchiOSimei = url_formatter2('FFN', 'ios')
        apiUrl = values.BaseURL + searchiOSimei
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------iOS searchimei--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------iOS searchimei is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbykiosklockunlock == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10275)
def test_tc_0005_kiosklockunlock(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbykiosklockunlock = url_formatter('All','869881036785080', 'KIOSK%20LOCK/UNLOCK%20EVENT', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL +  filtersbykiosklockunlock
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------kiosklockunlock--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------kiosklockunlock is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbypollevents == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10276)
def test_tc_0005_pollevents(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbypollevents = url_formatter('All', '869881036785080', 'POLL%20EVENT', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbypollevents
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------pollevents--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------pollevents is failed--------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbygetlicense == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10277)
def test_tc_0005_getlicense(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbygetlicense = url_formatter('All', '869881036785080', 'GET%20LICENSE', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbygetlicense
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------getlicense--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------getlicense is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyprovisioningprofile == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10278)
def test_tc_0005_provisioningprofile(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyprovisioningprofile = url_formatter('All', '869881036785080', 'PROVISION%20PROFILE%20LICENSE', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyprovisioningprofile
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------provisioningprofile--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------provisioningprofile is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbylicenseactivation == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10279)
def test_tc_0005_licenseactivation(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbylicenseactivation = url_formatter('All', '869881036785080', 'LICENSE%20ACTIVATION', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbylicenseactivation
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------licenseactivation--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------licenseactivation is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbycrashevent == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10280)
def test_tc_0005_crashevent(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbycrashevent = url_formatter('All', '869881036785080', 'CRASH%20REPORT%20EVENT', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbycrashevent
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------crashevent--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------crashevent is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywipeevent == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10281)
def test_tc_0005_wipeevent(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywipeevent = url_formatter('All', '869881036785080', 'WIPE%20EVENT', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywipeevent
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------wipeevent--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------wipeevent is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydatausage == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10282)
def test_tc_0005_datausage(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydatausage = url_formatter('All', '869881036785080', 'DATA%20USAGE%20EVENT', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydatausage
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------datausage--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------datausage is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbypusheevents == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10283)
def test_tc_0005_pusheevents(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbypusheevents = url_formatter('All', '869881036785080', 'PUSH%20EVENTS', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbypusheevents
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------pusheevents--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------pusheevents is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyWeGuardappevent == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10284)
def test_tc_0005_WeGuardappevent(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyWeGuardappevent = url_formatter('All', '869881036785080', 'WeGuard%20APP', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyWeGuardappevent
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------WeGuardappevent--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------WeGuardappevent is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyotherevent == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10285)
def test_tc_0005_otherevent(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyotherevent = url_formatter('All', '869881036785080', 'OTHER%20EVENTS', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyotherevent
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------otherevent--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------otherevent is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfologin == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10286)
def test_tc_0005_filtersbyinfologin(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfologin = url_formatter('All', values.userName, 'Login', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfologin
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfologin--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfologin is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnlogin == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10287)
def test_tc_0005_filtersbywarnlogin(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnlogin = url_formatter('All', values.userName, 'Login', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnlogin
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filterbywarnlogin--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filterbywarnlogin is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorlogin == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10287)
def test_tc_0005_filtersbydebuglogin(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorlogin = url_formatter('All', values.userName, 'Login', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorlogin
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filterbydebuglogin--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filterbydebuglogin is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfologout == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10288)
def test_tc_0005_filtersbyinfologout(url):

 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfologout = url_formatter('All', values.userName, 'Logout', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfologout
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfologout--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfologout is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnlogout == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10289)
def test_tc_0005_filtersbywarnlogout(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnlogout = url_formatter('All', values.userName, 'Logout', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnlogout
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filterbywarnlogout--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filterbywarnlogout is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebuglogout == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10290)
def test_tc_0005_filtersbydebuglogout(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebuglogout = url_formatter('All', values.userName, 'Logout', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebuglogout
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filterbydebuglogout--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filterbydebuglogout is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorlogout == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10291)
def test_tc_0005_filtersbyerrorlogout(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorlogout = url_formatter('All', values.userName, 'Logout', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorlogout
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorlogout--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorlogout is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoSimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10292)
def test_tc_0005_filtersbyinfoSimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoSimper = url_formatter('All', values.userName, 'Start%20Impersonate', 1, 100,'', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoSimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoSimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoSimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnSimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10293)
def test_tc_0005_filtersbywarnSimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnSimper = url_formatter('All', values.userName, 'Start%20Impersonate', 1, 100,'','WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnSimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnSimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnSimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugSimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10294)
def test_tc_0005_filtersbydebugSimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugSimper = url_formatter('All', values.userName, 'Start%20Impersonate', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugSimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugSimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugSimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorSimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10295)
def test_tc_0005_filtersbyerrorSimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorSimper = url_formatter('All', values.userName, 'Start%20Impersonate', 1, 100,'', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorSimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorSimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorSimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoEimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10296)
def test_tc_0005_filtersbyinfoEimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoEimper = url_formatter('All', values.userName, 'End%20Impersonate', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoEimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoEimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoEimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnSimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10297)
def test_tc_0005_filtersbywarnEimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnEimper = url_formatter('All', values.userName, 'End%20Impersonate', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnEimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnEimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnEimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugEimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10298)
def test_tc_0005_filtersbydebugEimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugEimper = url_formatter('All', values.userName, 'End%20Impersonate', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugEimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugEimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugEimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorEimper == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10299)
def test_tc_0005_filtersbyerrorEimper(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorEimper = url_formatter('All', values.userName, 'End%20Impersonate', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorEimper
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorEimper--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorEimper is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfopolicy == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10300)
def test_tc_0005_filtersbyinfopolicy(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfopolicy = url_formatter('All', values.userName, 'Policy', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfopolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfopolicy--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfopolicy is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnpolicy == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10301)
def test_tc_0005_filtersbywarnpolicy(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnpolicy = url_formatter('All', values.userName, 'Policy', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnpolicy--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnpolicy is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugpolicy == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10302)
def test_tc_0005_filtersbydebugpolicy(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugpolicy = url_formatter('All', values.userName, 'Policy', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugpolicy--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugpolicy is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorpolicy == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10303)
def test_tc_0005_filtersbyerrorpolicy(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorpolicy = url_formatter('All', values.userName, 'Policy', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorpolicy--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorpolicy is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfodevice == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10304)
def test_tc_0005_filtersbyinfodevice(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfodevice = url_formatter('All', values.userName, 'Policy', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfodevice
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfodevice--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfodevice is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarndevice == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10305)
def test_tc_0005_filtersbywarndevice(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarndevice = url_formatter('All', values.userName, 'Device', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarndevice
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarndevice--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarndevice is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugdevice == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10306)
def test_tc_0005_filtersbydebugdevice(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugdevice = url_formatter('All', values.userName, 'Device', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugdevice
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugdevice--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugdevice is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrordevice == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10307)
def test_tc_0005_filtersbyerrordevice(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrordevice = url_formatter('All', values.userName, 'Device', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrordevice
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrordevice--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrordevice is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfogroup == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10308)
def test_tc_0005_filtersbyinfogroup(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfogroup = url_formatter('All', values.userName, 'Group', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfogroup
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfogroup--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfogroup is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarngroup == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10309)
def test_tc_0005_filtersbywarngroup(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarngroup = url_formatter('All', values.userName, 'Group', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarngroup
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarngroup--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarngroup is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebuggroup == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10310)
def test_tc_0005_filtersbydebuggroup(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebuggroup = url_formatter('All', values.userName, 'Group', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebuggroup
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebuggroup--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebuggroup is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorgroup == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10311)
def test_tc_0005_filtersbyerrorgroup(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorgroup = url_formatter('All', values.userName, 'Group', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorgroup
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorgroup--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorgroup is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoupload == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10312)
def test_tc_0005_filtersbyinfoupload(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoupload = url_formatter('All', values.userName, 'Upload', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoupload
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoupload--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoupload is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnupload == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10313)
def test_tc_0005_filtersbywarnupload(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnupload = url_formatter('All', values.userName, 'Upload', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnupload
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnupload--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnupload is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugupload == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10314)
def test_tc_0005_filtersbydebugupload(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugupload = url_formatter('All', values.userName, 'Upload', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugupload
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugupload--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugupload is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorupload == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10315)
def test_tc_0005_filtersbyerrorupload(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorupload = url_formatter('All', values.userName, 'Upload', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorupload
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorupload--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorupload is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfocommand == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10316)
def test_tc_0005_filtersbyinfocommand(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfocommand = url_formatter('All', values.userName, 'Command', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfocommand
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfocommand--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfocommand is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarncommand == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10317)
def test_tc_0005_filtersbywarncommand(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarncommand = url_formatter('All', values.userName, 'Command', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarncommand
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarncommand--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarncommand is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugcommand == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10318)
def test_tc_0005_filtersbydebugcommand(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugcommand = url_formatter('All', values.userName, 'Command', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugcommand
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugcommand--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugcommand is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorcommand == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10319)
def test_tc_0005_filtersbyerrorcommand(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorcommand = url_formatter('All', values.userName, 'Command', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorcommand
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorcommand--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorcommand is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfobroadcast == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10320)
def test_tc_0005_filtersbyinfobroadcast(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfobroadcast = url_formatter('All', values.userName, 'Broadcast', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfobroadcast
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfobroadcast--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfobroadcast is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnbroadcast == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10321)
def test_tc_0005_filtersbywarnbroadcast(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnbroadcast = url_formatter('All', values.userName, 'Broadcast', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnbroadcast
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnbroadcast--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnbroadcast is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugbroadcast == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10322)
def test_tc_0005_filtersbydebugbroadcast(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugbroadcast = url_formatter('All', values.userName, 'Broadcast', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugbroadcast
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugbroadcast--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugbroadcast is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorbroadcast == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10323)
def test_tc_0005_filtersbyerrorbroadcast(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorbroadcast = url_formatter('All', values.userName, 'Broadcast', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorbroadcast
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorbroadcast--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorbroadcast is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfowetalk == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10324)
def test_tc_0005_filtersbyinfowetalk(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfowetalk = url_formatter('All', values.userName, 'WeTalk', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfowetalk
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfowetalk--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfowetalk is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnwetalk == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10325)
def test_tc_0005_filtersbywarnwetalk(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnwetalk = url_formatter('All', values.userName, 'WeTalk', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnwetalk
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnwetalk--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnwetalk is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugwetalk == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10326)
def test_tc_0005_filtersbydebugwetalk(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugwetalk = url_formatter('All', values.userName, 'WeTalk', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugwetalk
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugwetalk--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugwetalk is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorwetalk == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10326)
def test_tc_0005_filtersbyerrorwetalk(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorwetalk = url_formatter('All', values.userName, 'WeTalk', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorwetalk
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorwetalk--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorwetalk is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoweboxpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10327)
def test_tc_0005_filtersbyinfoweboxpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoweboxpass = url_formatter('All', values.userName, 'Webox%20passcode', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoweboxpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoweboxpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoweboxpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnweboxpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10328)
def test_tc_0005_filtersbywarnweboxpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnweboxpass = url_formatter('All', values.userName, 'Webox%20passcode', 1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnweboxpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnweboxpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnweboxpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugweboxpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10329)
def test_tc_0005_filtersbydebugweboxpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugweboxpass = url_formatter('All', values.userName, 'Webox%20passcode', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugweboxpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugweboxpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugweboxpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorweboxpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10330)
def test_tc_0005_filtersbyerrorweboxpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorweboxpass = url_formatter('All', values.userName, 'Webox%20passcode', 1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorweboxpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorwetalk--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorwetalk is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfokioskpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10331)
def test_tc_0005_filtersbyinfokioskpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfokioskpass = url_formatter('All', '869881036785080', 'Kiosk%20passcode', 1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfokioskpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfokioskpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfokioskpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnkioskpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10332)
def test_tc_0005_filtersbywarnkioskpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnkioskpass = url_formatter('All', '869881036785080', 'Kiosk%20passcode', 1, 100,'', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnkioskpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnkioskpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnkioskpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugkioskpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10333)
def test_tc_0005_filtersbydebugkioskpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugkioskpass = url_formatter('All', '869881036785080', 'Kiosk%20passcode', 1, 100,'', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugkioskpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugkioskpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugkioskpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorkioskpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10334)
def test_tc_0005_filtersbyerrorkioskpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorkioskpass = url_formatter('All', '869881036785080', 'Kiosk%20passcode', 1, 100,'', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorkioskpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorkioskpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorkioskpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
# iOS Device Logs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfodevinfo == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10335)
def test_tc_0005_filtersbyinfodevinfo(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfodevinfo = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceInformation',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfodevinfo
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfodevinfo--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfodevinfo is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarndevinfo == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10336)
def test_tc_0005_filtersbywarndevinfo(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarndevinfo = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceInformation',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarndevinfo
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarndevinfo--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarndevinfo is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugdevinfo == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10337)
def test_tc_0005_filtersbydebugdevinfo(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugdevinfo = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceInformation',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugdevinfo
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugdevinfo--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugdevinfoo is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrordevinfo == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10338)
def test_tc_0005_filtersbyerrordevinfo(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrordevinfo = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceInformation',1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrordevinfo
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrordevinfo--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrordevinfo is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoclrpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10339)
def test_tc_0005_filtersbyinfoclrpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoclrpass = url_formatter('All', 'FFNQ5S75G5MN', 'ClearPasscode',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoclrpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoclrpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoclrpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnclrpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10340)
def test_tc_0005_filtersbywarnclrpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnclrpass = url_formatter('All', 'FFNQ5S75G5MN', 'ClearPasscode',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnclrpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnclrpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnclrpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugclrpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10341)
def test_tc_0005_filtersbydebugclrpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugclrpass = url_formatter('All', 'FFNQ5S75G5MN', 'ClearPasscode',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugclrpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugclrpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugclrpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorclrpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10342)
def test_tc_0005_filtersbyerrorclrpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorclrpass = url_formatter('All', 'FFNQ5S75G5MN', 'ClearPasscode',1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorclrpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorclrpass--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorclrpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfodevlock == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10343)
def test_tc_0005_filtersbyinfodevlock(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfodevlock = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceLock',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfodevlock
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfodevlock--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfodevlock is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarndevlock == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10344)
def test_tc_0005_filtersbywarndevlock(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarndevlock = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceLock',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarndevlock
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarndevlock--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarndevlock is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugdevlock == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10345)
def test_tc_0005_filtersbydebugdevlock(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugdevlock = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceLock',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugdevlock
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugdevlock--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugdevlock is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrordevlock == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10346)
def test_tc_0005_filtersbyerrordevlock(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrordevlock = url_formatter('All', 'FFNQ5S75G5MN', 'DeviceLock',1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrordevlock
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrordevlock--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrordevlock is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoinstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10347)
def test_tc_0005_filtersbyinfoinstallapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoinstallapp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallApplication',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoinstallapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoinstallapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoinstallapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorinstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10348)
def test_tc_0005_filtersbyerrorinstallapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorinstallapp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallApplication',1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorinstallapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoinstallapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoinstallapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarninstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10349)
def test_tc_0005_filtersbywarninstallapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarninstallapp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallApplication',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarninstallapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarninstallapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarninstallapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebuginstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10350)
def test_tc_0005_filtersbydebuginstallapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebuginstallapp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallApplication',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebuginstallapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebuginstallapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebuginstallapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinforemapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10351)
def test_tc_0005_filtersbyinforemapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinforemapp = url_formatter('All', 'FFNQ5S75G5MN', 'RemoveApplication',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinforemapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinforemapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinforemapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorinstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10352)
def test_tc_0005_filtersbyerrorremapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorremapp = url_formatter('All', 'FFNQ5S75G5MN', 'RemoveApplication',1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorremapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorremapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorremapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnremapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10353)
def test_tc_0005_filtersbywarnremapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarnremapp = url_formatter('All', 'FFNQ5S75G5MN', 'RemoveApplication',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarnremapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnremapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnremapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugremapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10354)
def test_tc_0005_filtersbydebugremapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugremapp = url_formatter('All', 'FFNQ5S75G5MN', 'RemoveApplication',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugremapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugremapp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugremapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoinstallprof == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10355)
def test_tc_0005_filtersbyinstallprof(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoinstallprof = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProfile',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoinstallprof
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoinstallprof--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoinstallprof is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarninstallprof == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10356)
def test_tc_0005_filtersbywarninstallprof(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarninstallprof = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProfile',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarninstallprof
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarninstallprof---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarninstallprof is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebuginstallprof == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10357)
def test_tc_0005_filtersbydebuginstallprof(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebuginstallprof = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProfile',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebuginstallprof
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebuginstallprof---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebuginstallprof is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoinstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10358)
def test_tc_0005_filtersbyinstallpp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyinfoinstallpp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProvisioningProfile',1, 100, '', 'INFO', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyinfoinstallpp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoinstallpp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoinstallpp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorinstallprof == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10359)
def test_tc_0005_filtersbyerrorinstallpp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyerrorinstallprof = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProvisioningProfile',1, 100, '', 'ERROR', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyerrorinstallprof
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorinstallpp--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorinstallpp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarninstallpp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10360)
def test_tc_0005_filtersbywarninstallpp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbywarninstallpp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProvisioningProfile',1, 100, '', 'WARN', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbywarninstallpp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarninstallpp---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarninstallpp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebuginstallpp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.regressiontest
@pytest.mark.run(order=10361)
def test_tc_0005_filtersbydebuginstallpp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebuginstallpp = url_formatter('All', 'FFNQ5S75G5MN', 'InstallProvisioningProfile',1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebuginstallpp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebuginstallpp---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebuginstallpp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
#iOS Device Logs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyalldevinfo == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10362)
def test_tc_0005_filtersbyalldevinfo(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyalldevinfo = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'DeviceInformation', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyalldevinfo
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyalldevinfo--------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyalldevinfo is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyalldevlock == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10363)
def test_tc_0005_filtersbyalldevlock(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyalldevlock = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'DeviceLock', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyalldevlock
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyalldevlock---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyalldevlock is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallclrpass == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10364)
def test_tc_0005_filtersbyallclrpass(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallclrpass = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'ClearPasscode', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallclrpass
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallclrpass---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallclrpass is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallinstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10365)
def test_tc_0005_filtersbyallinstallapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallinstallpp = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'InstallProvisioningProfile', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallinstallpp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallinstallapp---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallinstallapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallinstallprof == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10366)
def test_tc_0005_filtersbyallinstallprof(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallinstallprof = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'InstallProfile', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallinstallprof
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallinstallprof---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallinstallprof is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallremapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10367)
def test_tc_0005_filtersbyallrempapp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallremapp = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'RemoveApplication', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallremapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallrempapp---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallrempapp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallinstallapp == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10368)
def test_tc_0005_filtersbyallinstallpp(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallinstallapp = url_formatter('All', 'FFNQ5S75G5MN', '', 1, 100, 'InstallApplication', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallinstallapp
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyallinstallpp ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyallinstallpp is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugALL == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10369)
def test_tc_0005_filtersbydebugALL(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbydebugALL = url_formatter('All', values.userName, '', 1, 100, '', 'DEBUG', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbydebugALL
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugALL ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugALL is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyallpolicy == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10370)
def test_tc_0005_filtersbyallpolicy(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, '', 1, 100, '', 'All', variable.start_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugALL ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugALL is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyinfoALLdaterange == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10371)
def test_tc_0005_filtersbyinfoALLdaterange(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, '', 1, 100, '', 'INFO', variable.custom_1week_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyinfoALLdaterange ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyinfoALLdaterange is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbydebugALLdaterange == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10372)
def test_tc_0005_filtersbydebugALLdaterange(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, '', 1, 100, '', 'DEBUG', variable.custom_1week_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbydebugALLdaterange ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbydebugALLdaterange is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyerrorALLdaterange == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10373)
def test_tc_0005_filtersbyerrorALLdaterange(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, '', 1, 100, '', 'ERROR', variable.custom_1week_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyerrorALLdaterange ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyerrorALLdaterange is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbywarnALLdaterange == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10374)
def test_tc_0005_filtersbywarnALLdaterange(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, '', 1, 100, '', 'WARN', variable.custom_1week_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbywarnALLdaterange ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbywarnALLdaterange is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyALLdaterange == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10375)
def test_tc_0005_filtersbyALLdaterange(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, 'Login', 1, 100, '', 'All', variable.custom_1week_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyALLdaterange ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyALLdaterange is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_AuditLogs_filtersbyalllogindaterange == 0 , reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.auditlogs
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10376)
def test_tc_0005_filtersbyalllogindaterange(url):
 now1 =datetime.now()
 if values.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
        filtersbyallpolicy=url_formatter('All', values.userName, 'Login', 1, 100, '', 'All', variable.custom_1week_timestamp, variable.end_timestamp)
        apiUrl = values.BaseURL + filtersbyallpolicy
        Headers = {'Authorization': 'Bearer {}'.format(values.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers,timeout=values.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------filtersbyalllogindaterange ---------")
        assert res.status_code == 200
 except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------filtersbyalllogindaterange is failed --------")
        WeGuard.logger.error("Exception : " + str(e))
        assert False