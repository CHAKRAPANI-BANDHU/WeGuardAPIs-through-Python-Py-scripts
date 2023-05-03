from datetime import datetime
import requests
import pytest
from . import global_varswetrack as globals
import test_GETutils as utils
from. import config as config
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import groupglobalvar as globalvars
import WeBoxpayloadinfo as variable
import globalvariables2 as globalcheck

def url_formatter3(policyId):
    url3 = 'enterprise/rest/locationtrackconfig/{policyId}'.format(policyId=policyId)
    return url3

#licensesUrl = 'enterprise/rest/weguard-v2/license?pageSize=10000&page=1'
#GetTrackUrl = 'enterprise/rest/locationtrackconfig/' + globalcheck.android_policy_id[0]
PolicyUrl = 'enterprise/rest/weguard-v2/groups/all'
TrackUrl = 'enterprise/rest/locationtrackconfig/5e857a5277f85d47345c1c24'

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_00002_getWeTrack == 0, reason="test_tc_00002_getWeTrack skip test")
@pytest.mark.negativetest
@pytest.mark.usualtest
@pytest.mark.webox
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10161)
def test_tc_000001_GetTrack(url):
 now1 = datetime.now()
 if globalvar.bearerToken == '':
     pytest.skip("Empty Bearer token Skipping test")
 try:
     for policyId in globalvars.android_policy_id:
        url3= url_formatter3(policyId)
     apiUrl = globalvar.BaseURL + url3
     Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
          #variable.createpolicyfolders["policyId"] = globalcheck.android_policy_id[0]
     # globalvar.Track["policyId"] = globalcheck.android_policy_id[0]
     # globalvar.Track["policyName"] = globalcheck.android_policyname
     # globalvar.Track["policyType"] = globalcheck.android_policytype
     res = requests.post(url=apiUrl, headers=Headers, timeout=globalvar.timeout)
     curl_str1 = utils.getCurlEquivalent(res)
     WeGuard.logger.debug(curl_str1)
     WeGuard.logger.debug("\n Response Headers: " + str(res.headers) + "\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response: " + str(res.content))
     WeGuard.logger.debug("\n\n--------------------------- Track is available ---------------------------")
     if (res.status_code == 200):
          print("The request was a success!")
        # Code here will only run if the request is successful
     elif (res.status_code != 400):
          print("Result not found!")
 except BaseException as e:
     now2 = datetime.now()
     WeGuard.logger.warning("Time taken: " + str(now2 - now1))
     WeGuard.logger.error("\n\n--------------------------- Track is not available ---------------------------\n\n")
     WeGuard.logger.error("Exception : " + str(e))
     assert False


@pytest.mark.skipif(config.run_test_tc_00003_OnlyTrack == 0, reason="test_tc_00003_OnlyTrack skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10163)
def test_tc_00003_OnlyTrack():
    print("\n\n--------Only Track--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id1': globals.id1,
            'trackEnabled1': globals.trackEnabled1,
            'postInterval1': globals.postInterval1,
            'events1': globals.events1,
            'version1': globals.version1,
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Only Track--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00004_TrackwithEventsUrl == 0, reason="test_tc_00004_TrackwithEventsUrl skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10164)
def test_tc_00004_TrackwithEventsUrl():
    print("\n\n--------Track with events--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id2': globals.id2,
            'trackEnabled2': globals.trackEnabled2,
            'postInterval2': globals.postInterval2,
            'events2': globals.events2,
            'version': globals.version2
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Track with events--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)

@pytest.mark.skipif(config.run_test_tc_00005_getalldevicesper_group == 0, reason="test_tc_00005_getalldevicesper_group skip test")
@pytest.mark.positivetest
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10165)
def test_tc_00005_getalldevicesper_group():
    print("\n\n--------get all devices group-------")
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:

        apiUrl = globalvar.BaseURL + PolicyUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = globals.WeTrack_all
        res = requests.post(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------get all devices group--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00006_OnlyTrackinvalidid == 0, reason="test_tc_00006_OnlyTrackinvalidid skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10166)
def test_tc_00006_OnlyTrackinvalidid():
    print("\n\n--------Only Track--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id4': globals.id4,
            'trackEnabled4': globals.trackEnabled4,
            'postInterval4': globals.postInterval4,
            'events4': globals.events4,
            'version4': globals.version4
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Only Track--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00007_OnlyTrackinvalidtrackEnabled == 0, reason="test_tc_00007_OnlyTrackinvalidtrackEnabled skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10167)
def test_tc_00007_OnlyTrackinvalidtrackEnabled():
    print("\n\n--------Only Track--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id5': globals.id5,
            'trackEnabled5': globals.trackEnabled5,
            'postInterval5': globals.postInterval5,
            'events5': globals.events5,
            'version5': globals.version5
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Only Track--------")
        assert res.status_code ==200
    except BaseException as e:
        print(e)


@pytest.mark.skipif(config.run_test_tc_00008_OnlyTrackinvalidpostinterval == 0, reason="test_tc_00008_OnlyTrackinvalidpostinterval skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10168)
def test_tc_00008_OnlyTrackinvalidpostinterval():
    print("\n\n--------Only Track--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id6': globals.id6,
            'trackEnabled6': globals.trackEnabled6,
            'postInterval6': globals.postInterval6,
            'events6': globals.events6,
            'version6': globals.version6
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Only Track--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00009_OnlyTrackinvalidversion == 0, reason="test_tc_00009_OnlyTrackinvalidversion skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10169)
def test_tc_00009_OnlyTrackinvalidversion():
    print("\n\n--------Only Track--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id7': globals.id7,
            'trackEnabled7': globals.trackEnabled7,
            'postInterval7': globals.postInterval7,
            'events7': globals.events7,
            'version7': globals.version7
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Only Track--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)


@pytest.mark.skipif(config.run_test_tc_00010_OnlyTrackinvalidevents == 0, reason="test_tc_00010_OnlyTrackinvalidevents skip test")
@pytest.mark.negativetest
@pytest.mark.regressiontest
@pytest.mark.wetrack
@pytest.mark.run(order=10170)
def test_tc_00010_OnlyTrackinvalidevents():
    print("\n\n--------Only Track--------")
    if  globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = globalvar.BaseURL + TrackUrl
        Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
        jsonData = {
            'id8': globals.id8,
            'trackEnabled8': globals.trackEnabled8,
            'postInterval8': globals.postInterval8,
            'events8': globals.events8,
            'version8': globals.version8
        }
        res = requests.put(url=apiUrl, headers=Headers, json=jsonData, timeout=globals.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug(res.content)
        WeGuard.logger.debug("\n\n--------Only Track--------")
        assert res.status_code ==200
    except BaseException as e:
        WeGuard.logger.error(e)

#@pytest.mark.skipif(config.run_test_tc_00001_licenses == 0, reason=" test_tc_00001_licenseslicenses skip test ")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.wetrack
# @pytest.mark.run(order=10161)
# @pytest.mark.parametrize('url', [""])
# # This must be the first test case for all tests. Without login and hence the Bearer token, all test cases will be skipped.
# # This is an alternative conditional marker to check if must_run or test_tc_000001_AccountAdmin_login is set or not.
# # Can't do anything without login, hence this test must take pole position.
# def test_tc_00001_licenses(url):
#     now1 = datetime.now()
#     if  globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#
#         apiUrl = globalvar.BaseURL + licensesUrl
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globals.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         WeGuard.logger.debug(curl_str1)
#         WeGuard.logger.debug(res.content)
#         WeGuard.logger.debug(" Response code: " + str(res.status_code) + " apiUrl: " + apiUrl + " Response headers: " + str(
#             res.headers) + " Request Payload: " + str(res.content))
#         WeGuard.logger.debug("\n\n--------------------------- TC 000001 All devices ---------------------------")
#         assert res.status_code ==200
#     except BaseException as e:
#         WeGuard.logger.error(e)
#         WeGuard.logger.error('Error at %s', 'BaseException', 'e')
#         now2 = datetime.now()
#         WeGuard.logger.error("Time taken: " + str(now2 - now1))
#         WeGuard.logger.error("\n\n--------------------------- TC 000001 No devices are enrolled ---------------------------\n\n")
#         WeGuard.logger.error("Exception : " + str(e))

# @pytest.mark.parametrize('url', [""])
# @pytest.mark.skipif(config.run_test_tc_00002_getWeTrack == 0, reason="test_tc_00002_getWeTrack skip test")
# @pytest.mark.positivetest
# @pytest.mark.sanitytest
# @pytest.mark.regressiontest
# @pytest.mark.wetrack
# @pytest.mark.run(order=10162)
# def test_tc_00002_getWeTrack(url):
#     print("\n\n--------Track configs--------")
#     if  globalvar.bearerToken == '':
#         pytest.skip("Empty Bearer token Skipping test")
#     try:
#         apiUrl = globalvar.BaseURL + GetTrackUrl
#         Headers = {'Authorization': 'Bearer {}'.format(globalvar.bearerToken)}
#         res = requests.get(url=apiUrl, headers=Headers, timeout=globals.timeout)
#         curl_str1 = utils.getCurlEquivalent(res)
#         WeGuard.logger.debug(curl_str1)
#         WeGuard.logger.debug(res.content)
#         WeGuard.logger.debug("\n\n--------Track configs--------")
#         assert res.status_code ==200
#     except BaseException as e:
#         WeGuard.logger.error(e)