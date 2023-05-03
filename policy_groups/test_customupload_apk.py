#Selecting an app in App burndown chart(when device exists in the policy)

import pytest
import requests
from datetime import datetime
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils

def url_formatter(fname,lname,userName, ac, pac):
    url = "uploader/upload/file/v2?name={fname}%20%20{lname}&userName={userName}&ac={ac}&pac={pac}".format(fname=fname, lname=lname, userName=userName, ac=ac, pac=pac)
    return url
uploadurl = url_formatter(globalvar.fname, globalvar.lname, globalvar.userName, globalvar.actcode, globalvar.pactcode)

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_app_customupload == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10146)
def test_tc_023_app_customupload(url):
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + uploadurl
        Headers = {'x-token': 'lqa7nt69izjgcg0uv4rl'}
        files = {'file': open("zAuditLogsWeBoxLogout/FilesUpload/Chakrapani Testing Info.apk", 'rb')}
        res = requests.post(url=apiUrl, files=files, headers=Headers)
        print("--------------------File is uploaded successfully-----------------")
        print("--------------------Apk is not supported-----------------")
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("--------------------Failed to upload a file-----------------")
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        assert False