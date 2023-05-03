import pytest
import requests
from datetime import datetime
import payloads as globals, layouts as validations
import test_GETutils as utils
import WeGuardlogger as WeGuard
import globalvariables as globalvar
import test_jsonnames as jsonnames

enterpriseappssize_URL = "enterprise/rest/apkdownload"
fcm_URL = "enterprise/rest/weguard-v2/fcmUpdate"

#-----Read apk downloads for a device-------
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_enterpriseapps_size == 0, reason="Enterprise apps size in single device view is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sprint19
@pytest.mark.run(order=10064)
def test_tc_00001_enterpriseapps_size(url):
    WeGuard.logger.error("\n\n---------------------------Enterprise apps size in single device view on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + enterpriseappssize_URL +"/"+ globals.calldeviceid + "/" + globals.id
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=api_URL, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
            WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                res.request) + "\nBody: " + (str(res.request.body) if (
                    res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
            WeGuard.logger.error(
                "\n\n--------------------------- Enterprise apps size in single device view on portal PASS ---------------------------")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Enterprise apps size in single device view on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_apk_du_fcmupdate == 0, reason="Enterprise apps fcm update is skipped")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.devicespage
@pytest.mark.sprint19
@pytest.mark.run(order=10064)
def test_tc_00001_apk_du_fcmupdate(url):
    WeGuard.logger.error("\n\n--------------------------- Enterprise apps fcm update on portal ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token. Skipping test")
    try:
        api_URL = globalvar.BaseURL + fcm_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        apk_du_usage = {
            jsonnames.TOPIC: globals.calldeviceid+"_"+globalvar.actcode+"_"+globalvar.pactcode,
            jsonnames.TYPE: globals.apkDU_type,
            jsonnames.PRIORITY: jsonnames.HIGH,
            jsonnames.LICENSELEVEL: False,
            "pId": "5f27f286fce966474413b5ce",
            jsonnames.ACTCODE: globalvar.actcode,
            jsonnames.PACTCODE: globalvar.pactcode
        }
        res = requests.post(url=api_URL, json = apk_du_usage, headers=headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        if res.status_code == 404:
            print("----------Module not found-----------")
        else:
            assert res.status_code == 200
            WeGuard.logger.debug("\napiUrl: " + api_URL + "\nMethod: " + res.request.method + "\nRequest: " + str(
                res.request) + "\nBody: " + (str(res.request.body) if (
                    res.request.method == 'POST' or res.request.method == 'PUT') else "") + "\nresponse code: " + str(
                res.status_code) + "\nresponse headers: " + str(res.headers) + "\nresponse: " + str(res.content))
            WeGuard.logger.error(
                "\n\n--------------------------- Enterprise apps fcm update on portal PASS ---------------------------")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- Enterprise apps fcm update on portal  FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False