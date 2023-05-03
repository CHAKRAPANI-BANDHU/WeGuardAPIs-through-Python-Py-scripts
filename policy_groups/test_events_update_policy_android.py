# events for UPDATING AN Android policy group
import json
import pytest
import requests
from datetime import datetime
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils
events_update_license_url = "enterprise/rest/weguard/logs/events"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_event_update_group_android == 0, reason= "skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10127)
def test_tc_033_update_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + events_update_license_url
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.events_updation_android_policy_, timeout=globalvar.timeout)
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
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 033 events for update policy failed ---------------------------\n\n")
        assert False

#fcm_after updating Android policy

fcm_update_license_url = "enterprise/rest/weguard/logs/events"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_fcm_update_group_android == 0, reason= "skip test")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.run(order=10128)
def test_tc_033_update_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + fcm_update_license_url
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.fcm_updating_policy, timeout=globalvar.timeout)
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
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 033 update policy  event android failed ---------------------------\n\n")
        assert False
