from datetime import datetime
import requests
import pytest
import globalvariables as globalvar
import WeGuardlogger as WeGuard
from WeBoxFiles_DeviceUploads_AuditLogs_Alerts import Validator as Executor
import test_GETutils as utils
from pprint import pprint

CertificateURL = "enterprise/rest/certificate"

# Upload Certificate from Certificate Management at Global Level
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_001_GLobalLevel_UploadCertificate == 0, reason="This test must run, it is mandatory. Without this test rest of test case execution should stop")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10443)
def test_CertificateGlobalLevel(url):
 now1 = datetime.now()
 if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
 try:
      apiUrl = globalvar.BaseURL + CertificateURL
      Headers = {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryelf8UZPtNUv5iBcq','Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
      Files = {'file': ("ALogin_Dashboard_Devices/WeGuard Certificate.cer", 'rb')}
      res = requests.post(apiUrl, headers=Headers, timeout=globalvar.timeout, data={ 'name': globalvar.certificatename,'filename': 'Certificate SSL.cer', 'description': 'testing'}, files = Files)
      curl_str1 = utils.getCurlEquivalent(res)
      WeGuard.logger.debug(curl_str1)
      WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(res.status_code) + "\n Response: " + str(res.content))
      print("--------------------Certificate is uploaded successfully-----------------")
      pprint(res.json())
      assert res.status_code != 200
 except BaseException as e:
      now2 = datetime.now()
      WeGuard.logger.warning("Time taken: " + str(now2 - now1))
      WeGuard.logger.error("--------------------Failed to upload Certificate-----------------")
      WeGuard.logger.error("Exception : " + str(e))
      assert False
