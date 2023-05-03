import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

help_textUrl = "enterprise/rest/weguard-v2/helptext/language/eng"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_tc_001_help_Text_after_login == 0, reason= "test is skipped")
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.usualtest
@pytest.mark.run(order=10010)
def test_tc_005_getHelpText(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + help_textUrl
        header =  globalvar.bearerToken
        res = requests.get(url=apiUrl, headers= {'access_token': header}, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n"  " Response Headers: " + str(
                res.headers)  + " apiUrl: " + apiUrl + " Response code: " + str(res.status_code)  + "\n" + " Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 005 Help Text Failed ---------------------------\n\n")
        assert False
