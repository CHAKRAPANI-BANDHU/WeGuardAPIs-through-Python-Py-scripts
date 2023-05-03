import requests
import pytest
from . import global_varschangepassword as globals
import test_GETutils as utils
from. import config as config
import globalvariables as globalvar
import WeGuardlogger as WeGuard

changepasswordUrl = 'enterprise/rest/users/changePassword'

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_00012_change_password == 0, reason="test_tc_00012_change_password skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.changepassword
@pytest.mark.run(order=10395)
# This must be the first test case for all tests. Without login and hence the Bearer token, all test cases will be skipped.
# This is an alternative conditional marker to check if must_run or test_tc_000001_AccountAdmin_login is set or not.
# Can't do anything without login, hence this test must take pole position.
def test_tc_00012_change_password(url):
    print('\n\n--------changepassword-------')
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + changepasswordUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'confirmPassword': globals.confirmPassword,
            'newPassword': globals.newPassword,
            'oldPassword': globals.oldPassword,
            'requestString': globals.requestString,
            'userName': globals.userName
        }
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------changepassword-------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00013_invalidconfirmpassword == 0, reason="test_tc_00013_invalidconfirmpassword skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.changepassword
@pytest.mark.run(order=10396)
def test_tc_00013_invalidconfirmpassword():
    print("\n\n--------invalid confirm password-------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + changepasswordUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'confirmPassword1': globals.confirmPassword1,
            'newPassword1': globals.newPassword1,
            'oldPassword1': globals.oldPassword1,
            'requestString1': globals.requestString1,
            'userName1': globals.userName1
        }
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------invalid confirm password-------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00014_invalidnewpassword == 0, reason="test_tc_00014_invalidnewpassword skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.changepassword
@pytest.mark.run(order=10397)
def test_tc_00014_invalidnewpassword():
    print("\n\n--------invalid new password-------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + changepasswordUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'confirmPassword2': globals.confirmPassword2,
            'newPassword2': globals.newPassword2,
            'oldPassword2': globals.oldPassword2,
            'requestString2': globals.requestString2,
            'userName2': globals.userName2
        }
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------invalid new password-------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00015_invalidoldpassword == 0, reason="test_tc_00015_invalidoldpassword skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.changepassword
@pytest.mark.run(order=10398)
def test_tc_00015_invalidoldpassword():
    print("\n\n--------invalid old password-------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + changepasswordUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'confirmPassword3': globals.confirmPassword3,
            'newPassword3': globals.newPassword3,
            'oldPassword3': globals.oldPassword3,
            'requestString3': globals.requestString3,
            'userName3': globals.userName3
        }
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------invalid old password-------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00016_invalidrequeststring == 0, reason="test_tc_00016_invalidrequeststring skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.changepassword
@pytest.mark.run(order=10399)
def test_tc_00016_invalidrequeststring():
    print("\n\n--------invalid requeststring-------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + changepasswordUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'confirmPassword4': globals.confirmPassword4,
            'newPassword4': globals.newPassword4,
            'oldPassword4': globals.oldPassword4,
            'requestString4': globals.requestString4,
            'userName4': globals.userName4
        }
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------invalid requeststring-------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00017_invalidusername == 0, reason="test_tc_00017_invalidusername  skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.changepassword
@pytest.mark.run(order=10400)
def test_tc_00017_invalidusername():
    print("\n\n--------invalid username-------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + changepasswordUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'confirmPassword5': globals.confirmPassword4,
            'newPassword5': globals.newPassword4,
            'oldPassword5': globals.oldPassword4,
            'requestString5': globals.requestString4,
            'userName5': globals.userName4
        }
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------invalid username-------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)
