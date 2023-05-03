import pytest
import requests
from _datetime import datetime
import globalvariables as globalvar
import globalvariables2 as vars
import layouts as validations, payloads as globals
import test_GETutils as utils
import WeBoxpayloadinfo as variable

import WeGuardlogger as WeGuard

dashboard_URL = "enterprise/rest/dashboard"

def url_formatter1(actcode, pactcode, page, limit, start, end):
    url3 = "enterprise/rest/auditlogs/{actcode}/{pactcode}?page={page}&limit={limit}&start={start}&end={end}".format(actcode=actcode, pactcode=pactcode,page=page, limit=limit, start=start, end=end)
    return url3
dashboard_calls_URL ="enterprise/rest/dashboard/calls/"

WeGuard.logger.debug("Dashboard page APIs")
#----readDashboardInfo----
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_dashboard == 0, reason="broadcast page on portal is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.dashboard
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00001_dashboard(url):
  now1 = datetime.now()
  if globalvar.bearerToken == '':
     pytest.skip("Empty Bearer token. Skipping test")
  try:
        api_URL = globalvar.BaseURL + dashboard_calls_URL + globalvar.actcode + "/" + globalvar.pactcode
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.error("\n\n---------------------------wetalk call history on portal  PASS ---------------------------\n\n")
  except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_Auditlogs_Recentactivity == 0, reason="Recent activity on portal dashboard is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.dashboard
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00001_Auditlogs_Recentactivity(url):
  now1 = datetime.now()
  if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
  try:
        RecentActivity=url_formatter1(globalvar.actcode, globalvar.pactcode, vars.page_1, vars.limit, variable.iso1weekcustom, variable.isoend)
        api_URL = globalvar.BaseURL + RecentActivity
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.error("\n\n---------------------------wetalk call history on portal  PASS ---------------------------\n\n")
  except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

#---readCallsInfo------
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_dashboard_calls == 0, reason="broadcast page on portal is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.dashboard
@pytest.mark.sprint19
@pytest.mark.run(order=10386)
def test_tc_00001_dashboard_calls(url):
  now1 = datetime.now()
  if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
  try:
        api_URL = globalvar.BaseURL + dashboard_calls_URL + globalvar.actcode + "/" + globalvar.pactcode
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
            res.request) + "\nBody: " + (str(res.request.body) if (
                res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
            res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
        WeGuard.logger.error("\n\n---------------------------wetalk call history on portal  PASS ---------------------------\n\n")
  except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk call history on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False