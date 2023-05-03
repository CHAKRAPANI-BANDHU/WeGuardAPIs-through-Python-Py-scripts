#CLONING ANDROID POLICIES
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import groupglobalvar as globalcheck
import test_GETutils as utils

group_URL = "enterprise/rest/weguard-v2/group"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_cloning_android == 0, reason=" test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10093)
def test_tc_008_group(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + group_URL
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json=globalvar.group)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                                  res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        globalvar.android_groupId = json.loads(res.content)['entity']['groupId']
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 008 cloning a group failed ---------------------------\n\n")
        assert False