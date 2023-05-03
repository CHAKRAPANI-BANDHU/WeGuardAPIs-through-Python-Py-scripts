import pytest
import requests
from datetime import datetime
import globalvariables as globalvar
import WeGuardlogger as WeGuard
from WeBoxFiles_DeviceUploads_AuditLogs_Alerts import Validator as Executor
import test_GETutils as utils


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_000001_GET_Certificates == 0, reason="Logged out Successfully")
@pytest.mark.raretest
@pytest.mark.logout
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.run(order=10446)
def test_tc_000001_CertificatePolicyLevel(url):
    print("\n\n--------------------------- GET Certificates ---------------------------")
    now1 =datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        CertificateURL = "enterprise/rest/certificate"
        apiUrl = globalvar.BaseURL + CertificateURL
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        res = requests.get(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("apiUrl: " + apiUrl + "\n Response Headers: " + str(res.headers)+ "\n Response code: " + str(res.status_code) + "\n +  Response: " + str(res.content))

        WeGuard.logger.debug("\n\n--------------------------- Displaying all the certificates ---------------------------\n\n")
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------------------------- Certificates are not being displayed ---------------------------\n\n")
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        assert False
