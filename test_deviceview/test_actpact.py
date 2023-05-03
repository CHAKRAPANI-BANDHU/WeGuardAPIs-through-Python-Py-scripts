import json
import pytest
import requests
from test_vars import payloads as globals, layouts as validations
import globalvariables as globalvar
from _datetime import datetime
import WeGuardlogger as WeGuard
import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_actpact == 0, reason="act and pact code is skipped")
@pytest.mark.positivetest
@pytest.mark.regressiontest
@pytest.mark.broadcast
@pytest.mark.sanitytest
@pytest.mark.run(order=10040)
def test_tc_00001_actpact(url):
    WeGuard.logger.error("\n\n--------------------------- test_tc_00001_actpact---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        license= "enterprise/rest/weguard-v2/license?pageSize=10000&page=1"
        api_URL = globalvar.BaseURL + license
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL,headers=headers, timeout=10)
        actcode = json.loads(res.content)['entity']['response'][0]['productInfo']['activationCode']
        globals.actCode = actcode
        pactcode = json.loads(res.content)['entity']['response'][0]['productInfo']['productActivationCode']
        globals.pactCode = pactcode
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n--------------------------- test_tc_00001_actpact PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.debug("Time taken: " + str(now2 - now1))
        WeGuard.logger.debug("Exception : " + str(e))
        pytest.fail("\n\n--------------------------- test_tc_00001_actpact FAIL ---------------------------\n\n")
        assert False
