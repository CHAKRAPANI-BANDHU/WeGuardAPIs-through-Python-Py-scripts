#prod version

import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_tc_001_UI_version == 0, reason= "test is skipped")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10009)
def test_tc_004_UI_version(url):
    try :
        version="version/version.json?v=0.6488869520508422"
        apiUrl = globalvar.BaseURL + version
        res = requests.get(url=apiUrl, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n"  " Response Headers: " + str(
                res.headers)  + " apiUrl: " + apiUrl + " Response code: " + str(res.status_code)  + "\n" + " Response: " + str(res.content))
        print(res.content)
        if (res.status_code == 200):
          print("The request was a success!")
        # Code here will only run if the request is successful
        elif (res.status_code != 400):
          print("Result not found!")
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        assert False
