import pytest
import requests
import globalvariables as globalvar
import cases_validations as config
import WeGuardlogger as WeGuard
import test_GETutils as utils

unapproveproduct_url = "enterprise/rest/weemm/product/app%3Acom.ludo.king/unapprove"
approveurl = "enterprise/rest/weemm/product/app%3Acom.google.android.gm/approve"
installIds= {"app":"com.google.android.gm"}
uninstallIds={"app": "app:com.ludo.king"}

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_approve_product == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10141)
def test_tc_040_UnapproveProduct(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + unapproveproduct_url
        Headers = {'Authorization':'Bearer {}'.format(globalvar.bearerToken) }
        res = requests.post(url= apiUrl, headers=Headers, data=uninstallIds, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                              res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 040 unapprove product failed ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_unapprove_product == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10142)
def test_tc_040_ApproveProduct(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + approveurl
        Headers = {'Authorization':'Bearer {}'.format(globalvar.bearerToken) }
        # Data2 = {'Approve': 'output {}'.format(installIds)}
        res = requests.post(url=apiUrl, headers=Headers, data=installIds, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
                                  + "\nRequest: " + str(res.request) + " Body: " + (
                                      str(res.request.body) if (
                                              res.request.method == 'POST' or res.request.method == 'PUT') else "")
                                  + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
            res.headers) + "\nResponse: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("-------------------------- TC 040 approve product failed ---------------------------\n\n")
        assert False