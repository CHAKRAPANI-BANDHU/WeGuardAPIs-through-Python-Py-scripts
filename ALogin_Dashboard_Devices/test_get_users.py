import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import test_GETutils as utils
import cases_validations as config

user = "enterprise/rest/users/user"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_tc_001__get_users == 0, reason= "test is skipped")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.usualtest
@pytest.mark.run(order=10011)
def test_tc_006_get_users(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + user
        print("\n\n--------------------------- Device count ---------------------------")
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug("\n" + " Response headers: " + str(res.headers) + " apiUrl: " + apiUrl + " Response code: " + str(res.status_code)  + "\n" + " Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 006 no users ---------------------------\n\n")
        assert False