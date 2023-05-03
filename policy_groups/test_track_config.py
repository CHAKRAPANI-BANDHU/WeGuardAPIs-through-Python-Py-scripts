# updating the track configs
import json
import pytest
import requests
from datetime import datetime
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils

track_configs_updating = "enterprise/rest/locationtrackconfig/5e3bed2077f85d12cb6104fc"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_track_configs_update == 0, reason= "skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10122)
def test_tc_028_event_delete_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + track_configs_updating
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.put(url=apiUrl, headers={'Authorization': header}, json = globalvar.track_configs_updating, timeout=globalvar.timeout)
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
        WeGuard.logger.error("-------------------------- TC 028 track failed ---------------------------\n\n")
        assert False
