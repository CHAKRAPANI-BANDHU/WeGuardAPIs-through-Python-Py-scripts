# QR For Android
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import groupglobalvar as globalcheck
import WeGuardlogger as WeGuard
import test_GETutils as utils


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_generate_QR_android == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10131)
def test_tc_036_genertae_QR(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    print(globalcheck.android_policy_id)
    try:
        print("\n-------------------Generate QR-----------------------------\n")
        for policyid in globalcheck.android_policy_id:
            generte_QRUrl = "enterprise/rest/weguard-v2/qr/generic/generation/" + policyid
            apiUrl = globalvar.BaseURL + generte_QRUrl
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
        WeGuard.logger.error("-------------------------- TC 036 Android QR failed ---------------------------\n\n")
        assert False


generte__invalid_QRUrl = "enterprise/rest/weguard-v2/qr/generation/5e69cc0e7c96b0d9d2"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_generate_Invalid_QR_android == 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.raretest
@pytest.mark.run(order=10132)
def test_tc_036_invalid_QR(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        print ("\n-----------Invalid QR-----------------\n")
        apiUrl = globalvar.BaseURL + generte__invalid_QRUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                              res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 036 Android QR failed ---------------------------\n\n")
        assert False
