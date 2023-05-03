#deleting Android group
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils

event_group_iOSUrl = "enterprise/rest/weguard/logs/events"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_events_update_group_iOS == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10110)
def test_tc_event_update_policy(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
        try:
            apiUrl = globalvar.BaseURL + event_group_iOSUrl
            header = 'Bearer' + ' ' + globalvar.bearerToken
            res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.event_update_policy_iOS, timeout=globalvar.timeout)
            resp_body = res.json()
            print(resp_body)
            WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                      + "\nRequest: " + str(res.request) + " Body: " + (
                                          str(res.request.body) if ( res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                      + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
                res.headers) + "\nResponse: " + str(res.content))
            assert res.status_code == 200
        except BaseException as e:
            WeGuard.logger.error("Exception : " + str(e))
            WeGuard.logger.error(
                "-------------------------- TC 021 update policy events failed ---------------------------\n\n")
            assert False

