# location track is the api which calls when policy dialog is opened
import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

locationtrack_configUrl = "enterprise/rest/locationtrackconfig/5e12da3bccc31c1b850a4593"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_location_track== 0, reason="test is skipped")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10091)
def test_tc_007_Locations_track(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + locationtrack_configUrl
        print("\n\n-------------------------- Disable Apps ---------------------------")
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
            "-------------------------- TC 007 locatuon config group failed ---------------------------\n\n")
        assert False

locationtrack_configUrl_invalid_policyID = "enterprise/rest/locationtrackconfig/5e12da3bb850a4593"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_group_location_track_invalid_policyid == 0, reason="test skipped")
@pytest.mark.negativetest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.run(order=10092)
def test_tc_007_Locations_track(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        apiUrl = globalvar.BaseURL + locationtrack_configUrl_invalid_policyID
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                              res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 400
    except BaseException as e:
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        WeGuard.logger.error(
            "-------------------------- TC 007 location config group failed ---------------------------\n\n")
        assert False
