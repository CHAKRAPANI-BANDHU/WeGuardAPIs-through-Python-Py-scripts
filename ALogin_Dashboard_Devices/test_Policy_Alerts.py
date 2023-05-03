# QR For Android
import json
import jsonnames
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import groupglobalvar as globalcheck
import WeGuardlogger as WeGuard
import test_GETutils as utils

notification_postUrl = "notification/rest/notification"


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_003_policy_get_alert_configs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.sprint20
@pytest.mark.run(order=10143)
def test_tc_01_get_policy_alert(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        # for policyid in globalcheck.android_policy_id:
        policylevel_alert_getURL = "notification/rest/notification/all/policy/" + globalcheck.android_policy_id[0]
        WeGuard.logger.debug("\n-----------Getting Policy level alert configs----------------\n")
        apiUrl = globalvar.BaseURL + policylevel_alert_getURL
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        res.json()
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC  Getting Policy level alert configs Failed ---------------------------\n\n")
        assert False

#posting the policy alerts configs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_003_policy_post_alert_configs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.regressiontest
@pytest.mark.run(order=10144)
def test_tc_02_post_policy_alert(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        WeGuard.logger.debug("\n-----------Posting Policy level alert configs----------------\n")
        apiUrl = globalvar.BaseURL + notification_postUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        globalvar.post_alert_configs[jsonnames.POLICYID] = globalcheck.android_policy_id[0]
        globalvar.post_acc_alert_configs[jsonnames.ACCOUNTID] = globalvar.accountId
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json=globalvar.post_alert_configs, timeout=globalvar.timeout)
        resp_body = res.json()
        content = res.content.decode()
        WeGuard.logger.debug("\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response headers: " + str(res.headers) + "\n  Response: " + str(res.content))
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        globalcheck.Notification_Object_id = json.loads(content)[jsonnames.ENTITY]["id"]
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC  Posting Policy level alert configs Failed ---------------------------\n\n")
        assert False



#updating the policy alerts configs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_003_policy_put_alert_configs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.regressiontest
@pytest.mark.run(order=10145)
def test_tc_put_policy_alert(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        WeGuard.logger.debug("\n-----------Updating the Policy level alert configs----------------\n")
        policylevel_alert_putURL = "notification/rest/notification/" + globalcheck.Notification_Object_id
        apiUrl = globalvar.BaseURL + policylevel_alert_putURL
        header = 'Bearer' + ' ' + globalvar.bearerToken
        globalvar.put_alert_configs["accountId"] = globalvar.accountId
        res = requests.put(url=apiUrl, headers={'Authorization': header}, json = globalvar.put_alert_configs, timeout=globalvar.timeout)
        resp_body = res.json()
        WeGuard.logger.debug(
            "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response headers: " + str(
                res.headers) + "\n  Response: " + str(res.content))
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC Updating Policy level alert configs Failed ---------------------------\n\n")
        assert False