#after deleting a group saving the configs
import json
import pytest
import requests
from datetime import datetime
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import  test_GETutils as utils

save_configs_deleted_group = "enterprise/rest/wenablesso/config/save"

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_delete_group_save_configs == 0, reason= "skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10108)
def test_tc_019_save_configs_event_delete_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + save_configs_deleted_group
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.save_config_deletedgroup, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        WeGuard.logger.debug("-----Configs saved Pass-----")
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 019 save configs failed ---------------------------\n\n")
        assert False

