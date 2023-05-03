import pytest
import requests
from datetime import datetime
import payloads as globals, layouts as validations
import test_GETutils as utils
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import test_jsonnames as jsonnames

videocall_subaccount_URL = "enterprise/rest/wetalk/accounts/subaccount"
videocallsettings_URL = "enterprise/rest/wenablesso/config/save"
WeGuard.logger.debug("video call config APIs")


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_wetalk_videocallconfig == 0, reason="wetalk video call configs on portal is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10064)
def test_tc_00001_wetalk_videocallconfig(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk video call configs on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + videocallsettings_URL
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        videocall_config ={jsonnames.COMPANYCONFIGS: [globals.callconfigs]}
        res = requests.post(url=api_URL,json = videocall_config, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
            WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                res.request) + "\nBody: " + (str(res.request.body) if (
                    res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
            WeGuard.logger.debug(
                "\n\n--------------------------- wetalk video call configs on portal PASS ---------------------------")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk video call configs on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_wetalk_videocallconfig == 0, reason="wetalk video call subaccount configs on portal is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetalkpage
@pytest.mark.sprint19
@pytest.mark.run(order=10064)
def test_tc_00002_wetalk_videocallconfig(url):
    WeGuard.logger.error("\n\n--------------------------- wetalk video call configs subaccount on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + videocall_subaccount_URL
        WeGuard.logger.error(api_URL)
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        videocall_config_subaccount = {
            jsonnames.FRIENDLYNAME: globalvar.userName,
            jsonnames.COMPANYID: globalvar.companyName
        }
        res = requests.post(url=api_URL,json = videocall_config_subaccount, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
            WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                res.request) + "\nBody: " + (str(res.request.body) if (
                    res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
            WeGuard.logger.debug(
                "\n\n--------------------------- wetalk video call subaccount on portal PASS ---------------------------")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- wetalk video call subaccount on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

