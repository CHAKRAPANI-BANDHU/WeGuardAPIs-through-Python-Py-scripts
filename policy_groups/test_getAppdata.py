#Get app data
import json
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

def url_formatter(actCo, pactCo):
    url= "enterprise/rest/weguard-v2/appdata/getApp/actCode/{actCod}/pactCode/{pactCod}".format(actCod=actCo, pactCod=pactCo)
    return url
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_act_pact_code == 0, reason="Policy is not opened ")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10080)
def test_tc_003_act_pact(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        act_pactUrl = url_formatter(globalvar.actcode, globalvar.pactcode)
        apiUrl = globalvar.BaseURL + act_pactUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
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
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 003 get app data failed ---------------------------\n\n")
        assert False