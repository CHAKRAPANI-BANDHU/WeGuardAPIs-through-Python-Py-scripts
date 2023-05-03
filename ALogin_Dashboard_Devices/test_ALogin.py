import json
import pytest
import requests
from datetime import datetime
import globalvariables as rest
import cases_validations as config
import jsonnames
import WeGuardlogger as WeGuard
import test_GETutils as utils

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_tc_001_admin_login== 0, reason= "login is compulsory")
@pytest.mark.positivetest
@pytest.mark.usualtest
@pytest.mark.raretest
@pytest.mark.devicespage
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.negativetest
@pytest.mark.run(order=10000)
def test_tc_001_login(url):
  try:
        apiUrl =  rest.BaseURL + rest.LoginUrl
        print("Username"+rest.userName)
        jsonData = {
            jsonnames.USERNAME: rest.userName,
            jsonnames.PASSWORD: rest.password
        }
        res = requests.post(url=apiUrl, json=jsonData, timeout=rest.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        rest.bearerToken = json.loads(res.content)['entity']['jwtToken']
        rest.actcode = json.loads(res.content)['entity']['activationCode']
        rest.pactcode = json.loads(res.content)['entity']['productActivationCode']
        rest.fname = json.loads(res.content)['entity']['fName']
        rest.lname = json.loads(res.content)['entity']['lName']
        rest.accountId = json.loads(res.content)['entity']['userData']['accountInfo']['id']
        rest.name = rest.fname + "%20%20" + rest.lname
        rest.companyName = json.loads(res.content)['entity']['companyName']
        rest.enterpriseId = json.loads(res.content)['entity']['enterpriseId']
        WeGuard.logger.debug("\n" + " Response code: " + str(res.status_code) + " apiUrl: " + apiUrl + " Response headers: " + str(
                res.headers) + "\n" + " Response : " + str(res.content))
        print("JWT token is :"+ rest.bearerToken)
        if (res.status_code == 200):
          print("The request was a success!")
        # Code here will only run if the request is successful
        elif (res.status_code == 400):
          print("Result not found!")
        assert rest.userName == json.loads(res.content)['entity']['userName']
  except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_tc_001_admin_login_invalid_Email == 0, reason= "test is skipped")
@pytest.mark.usualtest
@pytest.mark.negativetest
@pytest.mark.run(order=10002)
def test_tc_001_invalidEmail(url):
  try:
        apiUrl = rest.BaseURL + rest.LoginUrl
        jsonData = {
            jsonnames.USERNAME: "qa@20minutemail.com",
            jsonnames.PASSWORD: rest.password
        }
        now1 = datetime.now()
        res = requests.post(url=apiUrl, json=jsonData, timeout=rest.timeout)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        if (res.status_code == 200):
          print("The request was a success!")
        # Code here will only run if the request is successful
        elif (res.status_code == 400):          \
          print("Result not found!")
        # assert json.loads(res.content)['entity']['result'] == "User does not exists"
  except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_tc_001_admin_login_invalid_Pwd == 0, reason= "test is skipped")
@pytest.mark.usualtest
@pytest.mark.negativetest
@pytest.mark.run(order=10003)
def test_tc_001_invalidPassword(url):
  try:
        apiUrl = rest.BaseURL + rest.LoginUrl
        jsonData = {
            jsonnames.USERNAME: rest.userName,
            jsonnames.PASSWORD: "password"
        }
        res = requests.post(url=apiUrl, json=jsonData, timeout=rest.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        if (res.status_code == 200):
          print("The request was a success!")
        # Code here will only run if the request is successful
        elif (res.status_code == 400):          \
          print("Result not found!")
  except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.positivetest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.usualtest
@pytest.mark.skipif(config.run_tc_001_admin_login_event_logs == 0, reason= "test is skipped")
@pytest.mark.run(order=10007)
def test_tc_002_event_Login(url):
    if rest.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        event_Login = "enterprise/rest/weguard/logs/events"
        apiUrl = rest.BaseURL + event_Login
        header = 'Bearer' + ' ' + rest.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header},json = rest.login_events, timeout=rest.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n"  " Response Headers: " + str(
                res.headers)  + " apiUrl: " + apiUrl + " Response code: " + str(res.status_code)  + "\n" + " Response: " + str(res.content))
        if (res.status_code == 200):
          print("The request was a success!")
        # Code here will only run if the request is successful
        elif (res.status_code == 400):          \
          print("Result not found!")
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 002 EVENTS LOGIN FAIL ---------------------------\n\n")
        assert False


# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(config.run_tc_001_admin_login_with_spaces== 0, reason= "test is skipped")
# @pytest.mark.raretest
# @pytest.mark.negativetest
# @pytest.mark.run(order=10004)
# def test_tc_001_LoginWithSpaces(url):
#   try:
#         apiUrl = rest.BaseURL + rest.LoginUrl
#         jsonData = {
#             jsonnames.USERNAME: "",
#             jsonnames.PASSWORD: ""
#         }
#         now1 = datetime.now()
#         res = requests.post(url=apiUrl, json=jsonData, timeout=rest.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         print(curl_str1)
#         WeGuard.logger.debug("\napiUrl: " + apiUrl + "\nMethod: " + res.request.method
#                                   + "\nRequest: " + str(res.request) + " Body: " + (
#                                       str(res.request.body) if (
#                                                   res.request.method == 'POST' or res.request.method == 'PUT') else "")
#                                   + "\nResponse code: " + str(res.status_code) + " Response headers: " + str(
#             res.headers) + "\nResponse: " + str(res.content))
#         if (res.status_code == 200):
#           print("The request was a success!")
#         # Code here will only run if the request is successful
#         elif (res.status_code == 404):          \
#           print("Result not found!")
#         # assert json.loads(res.content)['entity']['result'] == "User does not exists"
#   except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
#         assert False
#
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(config.run_tc_001_admin_login_userName_spaces== 0, reason= "test is skipped")
# @pytest.mark.raretest
# @pytest.mark.negativetest
# @pytest.mark.run(order=10005)
# def test_tc_001_UsernameWithSpaces(url):
#   try:
#         apiUrl = rest.BaseURL + rest.LoginUrl
#         jsonData = {
#             'userName': "  ",
#             'password': rest.password
#         }
#         now1 = datetime.now()
#         res = requests.post(url=apiUrl, json=jsonData, timeout=rest.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         print(curl_str1)
#    WeGuard.logger.debug(
#    "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
#        res.status_code) + "\n Response: " + str(res.content))
#         assert res.status_code == 200
#         # assert json.loads(res.content)['entity']['result'] == "User does not exists"
#   except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
#         assert False
#
#
# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(config.run_tc_001_admin_login_pwd_spaces== 0, reason= "test is skipped")
# @pytest.mark.raretest
# @pytest.mark.run(order=10006)
# def test_tc_001_PasswordWithSpaces(url):
#   try:
#         apiUrl = rest.BaseURL + rest.LoginUrl
#         jsonData = {
#             jsonnames.USERNAME: rest.userName,
#             jsonnames.PASSWORD: " "
#         }
#         res = requests.post(url=apiUrl, json=jsonData, timeout=rest.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         print(curl_str1)
# WeGuard.logger.debug(
#    "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
 #       res.status_code) + "\n Response: " + str(res.content))
#         if (res.status_code == 200):
#           print("The request was a success!")
#         # Code here will only run if the request is successful
#         elif (res.status_code == 404):          \
#           print("Result not found!")
#   except BaseException as e:
#         WeGuard.logger.error("Exception : " + str(e))
#         WeGuard.logger.error("--------------------------- TC 001 LOGIN FAIL ---------------------------\n\n")
#         assert False

