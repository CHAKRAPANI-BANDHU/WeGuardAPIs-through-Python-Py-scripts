# Data Usage configs in the policy
import json
import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import groupglobalvar as globalcheck
import WeGuardlogger as WeGuard
import test_GETutils as utils

data_usage_invalidUrl = "enterprise/rest/config/datausage/5e69cc0e7c96b0d9d2"
data_usage_post_configUrl = "enterprise/rest/config/datausage"


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_get_datausage_configs_android == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sprint20
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10140)
def test_tc_get_datausage_configs(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        WeGuard.logger.debug("\n-------------------Data Usage-----------------------------\n")
        data_usage_configUrl = "enterprise/rest/config/datausage/" + globalcheck.android_policy_id[0]
        apiUrl = globalvar.BaseURL + data_usage_configUrl
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
        WeGuard.logger.error("-------------------------- TC Data Usage configs failed ---------------------------\n\n")
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_get_datausage_invalid_policyid_android == 0, reason="Skip test")
@pytest.mark.negativetest
@pytest.mark.sprint20
@pytest.mark.raretest
@pytest.mark.run(order=10141)
def test_tc_invalid_policyid(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        WeGuard.logger.debug("\n-----------Invalid Policy id for Data Usage Configs-----------------\n")
        apiUrl = globalvar.BaseURL + data_usage_invalidUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header}, timeout=globalvar.timeout)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- Invalid Policy id for Data Usage Configs ---------------------------\n\n")
        assert False


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_post_datausage_configs_android == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.sprint20
@pytest.mark.regressiontest
@pytest.mark.run(order=10142)
def test_tc_post_datausage_configs(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    WeGuard.logger.debug(globalcheck.android_policy_id)
    try:
        WeGuard.logger.debug("\n-------------------Data Usage-----------------------------\n")
        apiUrl = globalvar.BaseURL + data_usage_post_configUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        globalvar.datausage_configs["policyId"] = globalcheck.android_policy_id[0]
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json = globalvar.datausage_configs, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC Data Usage configs failed ---------------------------\n\n")
        assert False