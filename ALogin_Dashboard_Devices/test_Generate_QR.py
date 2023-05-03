# QR For Android
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import groupglobalvar as globalcheck
import WeGuardlogger as WeGuard
import test_GETutils as utils


genert_invalid_QRUrl = "enterprise/rest/weguard-v2/qr/generation/5e69cc0e7c96b0d9d2"


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_generate_QR_android == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.sprint20
@pytest.mark.run(order=10124)
def test_tc_031_genertae_QR(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        generte_QRUrl = "enterprise/rest/weguard-v2/qr/generic/generation/" + globalcheck.android_policy_id[0]
        WeGuard.logger.debug("\n-------------------Generate QR-----------------------------\n")
        # for policyid in globalcheck.android_policy_id:
        # generte_QRUrl = "enterprise/rest/weguard-v2/qr/generic/generation/" + policyid
        apiUrl = globalvar.BaseURL + generte_QRUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 036 Android QR failed ---------------------------\n\n")
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_generate_Invalid_QR_android == 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.raretest
@pytest.mark.policygroups
@pytest.mark.regressiontest
@pytest.mark.sprint20
@pytest.mark.run(order=10125)
def test_tc_031_invalid_QR(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        WeGuard.logger.debug("\n-----------Invalid QR-----------------\n")
        apiUrl = globalvar.BaseURL + genert_invalid_QRUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 036 Android QR failed ---------------------------\n\n")
        assert False
