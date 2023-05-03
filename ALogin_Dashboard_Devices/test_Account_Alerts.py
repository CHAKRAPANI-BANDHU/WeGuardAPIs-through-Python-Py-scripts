import json
import pytest
import requests
import jsonnames
import globalvariables as globalvar
import cases_validations as config
import groupglobalvar as globalcheck
import WeGuardlogger as WeGuard
import test_GETutils as utils


acc_post_notification_Url = "notification/rest/notification"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_003_account_post_alert_configs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.sprint20
@pytest.mark.run(order=10147)
def test_tc_post_acc_alert(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        WeGuard.logger.debug("\n-----------Posting Account level alert configs----------------\n")
        apiUrl = globalvar.BaseURL + acc_post_notification_Url
        header = 'Bearer' + ' ' + globalvar.bearerToken
        globalvar.post_acc_alert_configs[jsonnames.ACCOUNTID] = globalvar.accountId
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json= globalvar.post_acc_alert_configs, timeout=globalvar.timeout)
        resp_body = res.json()
        content = res.content.decode()
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        globalcheck.acc_notification_Object_id = json.loads(content)[jsonnames.ENTITY]['id']
        WeGuard.logger.error("-------------------------- TC  Posting Account level alert configs Pass ---------------------------\n\n")
        WeGuard.logger.debug(globalcheck.acc_notification_Object_id)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC  Posting Account level alert configs Failed --------------------------- \n\n")
        assert False

#updating the account  alerts configs
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_003_account_put_alert_configs == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.regressiontest
@pytest.mark.run(order=10148)
def test_tc_put_acc_alert(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        acc_alert_putURL = "notification/rest/notification/" + globalcheck.acc_notification_Object_id
        WeGuard.logger.debug("\n-----------Updating the Account level alert configs----------------\n")
        apiUrl = globalvar.BaseURL + acc_alert_putURL
        header = 'Bearer' + ' ' + globalvar.bearerToken
        globalvar.acc_put_alerts[jsonnames.ACCOUNTID] = globalvar.accountId
        res = requests.put(url=apiUrl, headers={'Authorization': header}, json= globalvar.acc_put_alerts, timeout=globalvar.timeout)
        resp_body = res.json()
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(
            "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response headers: " + str(
                res.headers) + "\n  Response: " + str(res.content))
        assert resp_body[jsonnames.ENTITY]['accountId'] == globalvar.accountId
        WeGuard.logger.debug("\n-----------  Updated the Account level alert configs PASS  ----------------\n")
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC Updating Account level alert configs Failed ---------------------------\n\n")
        assert False


