import json
import pytest
import requests
import globalvariables as globalvar
import test_GETutils as utils
import cases_validations as config
import groupglobalvar as globalcheck
from collections import defaultdict
import WeGuardlogger as WeGuard

def url_formatter(psize, page):
    url = "enterprise/rest/weguard-v2/license?pageSize={pagize}&page={page}".format(pagize=psize, page=page)
    return url

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_001_license_5000 == 0, reason="test skipped")
@pytest.mark.usualtest
@pytest.mark.devicespage
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.positivetest
@pytest.mark.run(order=10008)
def test_tc_007_license_10000(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        LicenseUrl = url_formatter(globalcheck.pagesize_10000, globalcheck.page_1)
        # LicenseUrl = "enterprise/rest/weguard-v2/license?pageSize=10000&page=1"
        apiUrl = globalvar.BaseURL + LicenseUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        resp_body = res.json()
        print(resp_body)
        json_resp = json.loads(res.content)
        print(json_resp.keys())
        android_policies = json_resp.get('entity').get('response')
        ios_profiles = json_resp.get('entity').get('iosProfile')
        profiletype = []
        profileid = []
        #to get profile ids based on policy type
        for profile in ios_profiles:
            profiletype.append(profile.get('type'))
            profileid.append(profile.get('id'))
        merged_list = [(profiletype[i], profileid[i]) for i in range(0, len(profiletype))]
        for key, value in merged_list:
            if key == 'IOS_NONDEP':
                globalcheck.nondepProfileIds.append(value)
            else:
                globalcheck.depProfileIds.append(value)
        #to get policy ids based on policy type
        policytype = []
        policyid = []
        for policy in android_policies:
            policytype.append(policy.get('type'))
            policyid.append(policy.get('id'))
        merged_list = [(policytype[i], policyid[i]) for i in range(0, len(policytype))]
        for key, value in merged_list:
            if key == 'ANDROID_KIOSK':
                globalcheck.kioskIds.append(value)
            elif key == 'ANDROID_WM':
                globalcheck.wmIds.append(value)
            else:
                globalcheck.wpIds.append(value)
        #to get android policy id
        for policy in android_policies:
            globalcheck.android_policy_id.append(policy.get('id'))
        #to get android policy names
        for policy in android_policies:
            globalcheck.android_policyname.append(policy.get('name'))
        #to get ios profile names
        for policy in ios_profiles:
            globalcheck.iOS_Profile_name.append(policy.get('name'))
        print(globalcheck.kioskIds)
        print(globalcheck.wmIds)
        print(globalcheck.wpIds)
        print(globalcheck.nondepProfileIds)
        print(globalcheck.depProfileIds)
        assert res.status_code == 200
    except BaseException as e:
        print(e)
        assert False

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_001_license_100 == 0, reason="test is skipped")
@pytest.mark.raretest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.negativetest
@pytest.mark.run(order=10012)
def test_tc_007_license_100(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        LicenseUrl_100 = url_formatter(globalcheck.pagesize_100, globalcheck.page_0)
        apiUrl = globalvar.BaseURL + LicenseUrl_100
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 007 Failed to get licenses in the account  ---------------------------\n\n")
        assert False

# LicenseUrl_1000 = "enterprise/rest/weguard-v2/license?pageSize=1000&page=1"
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_001_license_1000 == 0, reason="test is skipped")
@pytest.mark.raretest
@pytest.mark.devicespage
@pytest.mark.regressiontest
@pytest.mark.negativetest
@pytest.mark.run(order=10013)
def test_tc_007_license_1000(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try :
        LicenseUrl_1000 = url_formatter(globalcheck.pageSize_1000, globalcheck.page_1)
        apiUrl = globalvar.BaseURL + LicenseUrl_1000
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.get(url=apiUrl, headers={'Authorization': header})
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n Response Headers: " + str(res.headers) + "\n" + "apiUrl: " + apiUrl + "\n Response code: " + str(
                res.status_code) + "\n Response: " + str(res.content))
        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error("--------------------------- TC 007 Failed to get licenses in the account  ---------------------------\n\n")
        assert False

