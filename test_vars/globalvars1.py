import os
loglevel = 0
global userName
userName = ''
global password
password = ''
global BaseURL
BaseURL = ''


#broadcast history details

os.environ["WEGUARD_USER"] = "aadan.halston@niickel.us"
# os.environ["WEGUARD_PASS"] = "2b217fd26f0506d7cfe87e08483838fe8bf130ce6b3a987d94adfd3d043454a5"
#os.environ["QA_BASEURL"] = "https://qa-cloud-gw.weguard.io/"
#os.environ["LOG_LEVEL"] = "4"

if os.environ.get('WEGUARD_USER') is not None:
    userName = os.getenv('WEGUARD_USER')
if os.environ.get('WEGUARD_PASS') is not None:
    password = os.getenv('WEGUARD_PASS')
if os.environ.get('QA_BASEURL') is not None:
    BaseURL = os.getenv('QA_BASEURL')
if os.environ.get('LOG_LEVEL') is not None:
    loglevel = int(os.environ['LOG_LEVEL'])
