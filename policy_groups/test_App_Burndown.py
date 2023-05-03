#Selecting an app in App burndown chart(when device exists in the policy)

import pytest
import requests
import globalvariables as globalvar
import WeGuardlogger as WeGuard
import cases_validations as config
import test_GETutils as utils
import groupglobalvar as globalcheck

#DeviceAppUrl = "enterprise/rest/ios/profile/burndown/apps?page=1&size=10&sendPushNotification=true"
def url_formatter(page, psize):
    url = "enterprise/rest/ios/profile/burndown/apps?page={page}&size={pagize}&sendPushNotification=true".format(page=page, pagize=psize)
    return url
@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(config.run_test_tc_003_app_burndown_iOS == 0, reason="Skip test")
@pytest.mark.positivetest
@pytest.mark.policygroups
@pytest.mark.sanitytest
@pytest.mark.regressiontest
@pytest.mark.run(order=10111)
def test_tc_022_AppBurndown(url):
    if globalvar.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        DeviceAppUrl = url_formatter(globalcheck.page_1, globalcheck.pagesize_10)
        apiUrl = globalvar.BaseURL + DeviceAppUrl
        header = 'Bearer' + ' ' + globalvar.bearerToken
        res = requests.post(url=apiUrl, headers={'Authorization': header}, json=globalvar.appBurndown_app_selection)
        curl_str1 = utils.getCurlEquivalent(res)
        print(curl_str1)
        WeGuard.logger.debug(
            "\n"  " Response Headers: " + str(
                res.headers)  + " apiUrl: " + apiUrl + " Response code: " + str(res.status_code)  + "\n" + " Response: " + str(res.content))

        assert res.status_code == 200
    except BaseException as e:
        WeGuard.logger.error("Exception : " + str(e))
        WeGuard.logger.error(
            "-------------------------- TC 022 selecting an app in burndown chart failed ---------------------------\n\n")
        assert False
