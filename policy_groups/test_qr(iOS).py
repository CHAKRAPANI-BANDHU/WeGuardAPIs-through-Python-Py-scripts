# QR For iOS NON-DEP
import json
import pytest
import requests
import globalvariables as globalvar
import test_GETutils as utils
import cases_validations as config
import WeGuardlogger as WeGuard
import groupglobalvar as globalcheck


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_generate_QR_NON_DEP== 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10133)
def test_tc_037_non_depqr(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        print ("\n-----------Generate NON-DEP QR-----------------\n")
        for profileid in globalcheck.nondepProfileIds:
            QR_iOSUrl = "enterprise/rest/ios/profile/" + profileid + "/qr"
            apiUrl = globalvar.BaseURL + QR_iOSUrl
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
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 036 iOS QR failed ---------------------------\n\n")
        assert False

InvalidQR_iOSUrl = "enterprise/rest/ios/profile/5e3be512cb610674/qr"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_generate_invalid_QR_NON_DEP== 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.run(order=10134)
def test_tc_037_invalid_non_dep_qr(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        print ("\n-----------Generate Invalid QR-----------------\n")
        apiUrl = globalvar.BaseURL + InvalidQR_iOSUrl
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
        assert res.status_code != 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 036 iOS QR failed ---------------------------\n\n")
        assert False

