import pytest
import requests
from test_vars import payloads as globals, layouts as validations
import WeGuardlogger as WeGuard
from _datetime import datetime
import test_GETutils as utils
import random
import globalvariables as globalvar


@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_resetpswdEmailOTP == 0, reason="Sending reset password OTP to Email is skipped")
@pytest.mark.positivetest
@pytest.mark.resetpswdtest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10402)
def test_tc_00001_resetpswdEmailOTP(url):
    WeGuard.logger.error("\n\n--------------------------- resetpswdEmailOTP ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswdOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        resetpswdemailotp = {"emailId":globalvar.userName}
        res = requests.post(url=api_URL,json= resetpswdemailotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.debug("\n\n---------------------------  resetpswdEmailOTP PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- resetpswdEmailOTP FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00001_resetpswd_verifyOTP_valid == 0, reason="Verifying reset password with Valid OTP is skipped")
@pytest.mark.positivetest
@pytest.mark.resetpswdtest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10403)
# Verify Valid OTP for reset password
def test_tc_00001_resetpswd_verifyOTP_valid(url):
    WeGuard.logger.error("\n\n--------------------------- verifyOTP with validOTP ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswd_verifyOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        verifyotp = {'username': globalvar.userName, 'otp': globals.otp, 'newpassword': globals.newPassword}
        res = requests.post(url=api_URL, json=verifyotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        if res.content == b'{"successful":true,"result":"Invalid/Missing Credentials","statusCode":2000,"entity":"","entities":[],"count":0}':
            WeGuard.logger.error("\n\n---------------------please provide Correct OTP in encrypted format--------------------------\n\n")
        else:
            WeGuard.logger.error("\n\n---------------------------  verifyOTP with validOTP PASS ---------------------------\n\n")
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- verifyOTP with validOTP FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00002_resetpswd_verifyOTP_invalid == 0, reason="Verifying reset password with invalid OTP is skipped")
@pytest.mark.negativetest
@pytest.mark.resetpswdtest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10404)
def test_tc_00002_resetpswd_verifyOTP_invalid(url):
    WeGuard.logger.error("\n\n--------------------------- verifyOTP with invalidOTP ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswd_verifyOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        verifyotp = {'username': globalvar.userName, 'otp': random.random(), 'newpassword': globals.newPassword}
        res = requests.post(url=api_URL, json=verifyotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.error("\n\n---------------------------  verifyOTP with invalidOTP PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- verifyOTP with invalidOTP FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00003_resetpswd_verifyOTP_emptyOTP== 0, reason="Verifying reset password without OTP is skipped")
@pytest.mark.negativetest
@pytest.mark.resetpswdtest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10405)
def test_tc_00003_resetpswd_verifyOTP_emptyOTP(url):
    WeGuard.logger.error("\n\n---------------------------verifyOTP with emptyOTP ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswd_verifyOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        verifyotp = {'username': globalvar.userName, 'otp': None, 'newpassword': globals.newPassword}
        res = requests.post(url=api_URL, json=verifyotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.error("\n\n---------------------------  verifyOTP with emptyOTP PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- verifyOTP with emptyOTP FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00004_resetpswd_verifyOTP_sameoldpassword== 0, reason="Verifying reset password with same old password is skipped")
@pytest.mark.positivetest
@pytest.mark.resetpswdtest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10406)
def test_tc_00004_resetpswd_verifyOTP_sameoldpassword(url):
    WeGuard.logger.error("\n\n--------------------------- verifyOTP with sameoldpassword ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswd_verifyOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        verifyotp = {'username': globalvar.userName, 'otp': globals.otp, 'newpassword': globals.samePassword}
        res = requests.post(url=api_URL, json=verifyotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        if res.content == b'{"successful":true,"result":"Invalid/Missing Credentials","statusCode":2000,"entity":"","entities":[],"count":0}':
            WeGuard.logger.error("\n\n---------------------please provide Correct OTP in encrypted format--------------------------\n\n")
        else:
            WeGuard.logger.error("\n\n--------------------------- verifyOTP with sameoldpassword PASS ---------------------------\n\n")
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- verifyOTP with sameoldpassword FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00005_resetpswd_verifyOTP_newpassword== 0, reason="Verifying reset password with new password is skipped")
@pytest.mark.positivetest
@pytest.mark.resetpswdtest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10407)
def test_tc_00005_resetpswd_verifyOTP_newpassword(url):
    WeGuard.logger.error("\n\n--------------------------- verifyOTP with newpassword ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswd_verifyOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        verifyotp = {'username': globalvar.userName, 'otp': globals.otp, 'newpassword': globals.newPassword}
        res = requests.post(url=api_URL, json=verifyotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        if res.content == b'{"successful":true,"result":"Invalid/Missing Credentials","statusCode":2000,"entity":"","entities":[],"count":0}':
            WeGuard.logger.error("\n\n---------------------please provide Correct OTP in encrypted format--------------------------\n\n")
        else:
            WeGuard.logger.error("\n\n--------------------------- verifyOTP with newpassword PASS ---------------------------\n\n")
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- verifyOTP with newpassword FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(validations.run_test_tc_00006_resetpswd_verifyOTP_emptypassword== 0, reason="Verifying reset password with empty password is skipped")
@pytest.mark.negativetest
@pytest.mark.resetpswdtest
@pytest.mark.regressiontest
@pytest.mark.sanitytest
@pytest.mark.run(order=10408)
def test_tc_00006_resetpswd_verifyOTP_emptypassword(url):
    WeGuard.logger.error("\n\n--------------------------- verifyOTP with empty password ---------------------------")
    now1 = datetime.now()
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        api_URL = globalvar.BaseURL + globals.resetpswd_verifyOTP_URL
        headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        verifyotp = {'username': globalvar.userName, 'otp': globals.otp, 'newpassword': None}
        res = requests.post(url=api_URL, json=verifyotp, headers=headers, timeout=10)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + api_URL + " Response headers: " + str(res.headers) + "\n" + " Request Payload: " + str(res.content))
        assert res.status_code == 200
        WeGuard.logger.error("\n\n--------------------------- verifyOTP with empty password PASS ---------------------------\n\n")
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.error('Error at %s', 'BaseException', 'e')
        WeGuard.logger.error("Time taken: " + str(now2 - now1))
        pytest.fail("\n\n--------------------------- verifyOTP with empty password FAIL ---------------------------\n\n")
        WeGuard.logger.error("Exception : " + str(e))
        assert False
