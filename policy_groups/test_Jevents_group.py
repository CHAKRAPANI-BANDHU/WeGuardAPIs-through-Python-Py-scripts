# events after creating a group (iOS or Android)
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils
event_delete_group = "enterprise/rest/weguard/logs/events"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_event_after_cloning_group_Android == 0, reason= "skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10095)
def test_tc_010_event_cloning_group_Android(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + event_delete_group
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.event_cloning_Android, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        print(e)
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_event_after_cloning_group_iOS == 0, reason= "skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10096)
def test_tc_0010_event_cloning_group_iOS(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + event_delete_group
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.event_cloning_iOS, timeout=globalvar.timeout)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 010 events for cloning a group failed ---------------------------\n\n")
        assert False

