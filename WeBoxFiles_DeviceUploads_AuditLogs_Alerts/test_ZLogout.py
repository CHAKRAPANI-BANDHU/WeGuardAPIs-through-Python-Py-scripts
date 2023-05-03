import pytest
import requests
from datetime import datetime
import globalvariables as X
import WeGuardlogger as WeGuard
import Validator as Executor
import test_GETutils as utils
import WeBoxpayloadinfo as variable

LogoutURL= 'enterprise/rest/weguard/logs/events'

@pytest.mark.parametrize('url', [""])
@pytest.mark.skipif(Executor.test_tc_000001_AccountAdmin_Logout == 0, reason="Logged out Successfully")
@pytest.mark.raretest
@pytest.mark.logout
@pytest.mark.usualtest
@pytest.mark.sanitytest
@pytest.mark.run(order=10448)
def test_tc_000001_Logout(url):
    print("\n\n--------------------------- TC 000001 Logout Start ---------------------------")
    now1 =datetime.now()
    if X.bearerToken == '':
        pytest.skip("Empty Bearer token Skipping test")
    try:
        apiUrl = X.BaseURL + LogoutURL
        Headers = {'Authorization': 'Bearer {}'.format(X.bearerToken)}
        res = requests.post(url=apiUrl, headers=Headers, json=variable.logout, timeout=X.timeout)
        curl_str1 = utils.getCurlEquivalent(res)
        WeGuard.logger.debug(curl_str1)
        WeGuard.logger.debug("\n Response code: " + str(res.status_code) + "\n apiUrl: " + apiUrl + "\n Response Headers: " + str(res.headers) + "\n Response: " + str(res.content))
        WeGuard.logger.debug("\n\n--------------------------- Logout PASS ---------------------------\n\n")
        assert res.status_code == 200
    except BaseException as e:
        now2 = datetime.now()
        WeGuard.logger.warning("Time taken: " + str(now2 - now1))
        WeGuard.logger.error("\n\n--------------------------- Logout FAIL ---------------------------\n\n")
        WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
        assert False
