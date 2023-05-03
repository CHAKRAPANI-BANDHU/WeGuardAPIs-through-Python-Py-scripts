import os

import jsonnames
from WeGuardlogger import rotate_log_file
import time
import random
import string
import groupglobalvar as globalcheck
from datetime import datetime

now_datetime = datetime.now()
start_of_day_datetime = now_datetime.replace(hour=00, minute=00, second=00)
end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59)
start_timestamp = int(round(start_of_day_datetime.timestamp() * 1000))
end_timestamp = int(round(end_of_day_datetime.timestamp() * 1000))


global userName
userName = ''
global password
password = ''
global BaseURL
BaseURL= ''
global loglevel
loglevel = 0

android_groupId= ""
ios_groupid = ""

if os.environ.get('WEGUARD_USER') is not None:
    userName = os.getenv('WEGUARD_USER')

if os.environ.get('WEGUARD_PASS') is not None:
    password = os.getenv('WEGUARD_PASS')

if os.environ.get('QA_BASEURL') is not None:
        BaseURL = os.getenv('QA_BASEURL')

if os.environ.get('LOG_LEVEL') is not None:
    loglevel = int(os.environ['LOG_LEVEL'])

log_file = "WeGuard" + format(time.strftime("%Y%m%d_%H%M%S")) + ".log"
rotate_log_file(log_file, loglevel)


timeout= 120
bearerToken= ""
actcode = ""
pactcode = ""
fname = ""
lname = ""
accountId = ""
companyName = ""
login_events=""
name= ""
enterpriseId=""
# Urls
LoginUrl = "enterprise/rest/users/login"
N= 6

Track=''


Z=8
certificatename= {"name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=Z))}

C=6
createglobalfolder= {
  "name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=C)),
  "policies": [],
  "shared": "true",
  "actCode": actcode
}

B=6
createpolicyfolders={
  "name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=B)),
  "policies": [
    {
      "policyId": globalcheck.android_policy_id,
      "policyName": globalcheck.android_policyname,
      "policyType": globalcheck.policytype
    }
  ],
  "shared": "false",
  "actCode": actcode
}

post_alert_configs = {
  "accountId": "5e3beb8e77f85d12cb61041e",
  "policyId": globalcheck.android_policy_id,
  "batteryWarningEmailList": [],
  "batteryLowEmailList": [],
  "batteryCriticalEmailList": [],
  "dataUsageWarningEmailList": None,
  "dataUsageLowEmailList": None,
  "dataUsageCriticalEmailList": None,
  "adminLockedEmailList": None,
  "deviceRebootedEmailList": None,
  "deviceWipedEmailList": None,
  "deviceDeletedEmailList": None,
  "deviceLostEmailList": None,
  "deviceStolenEmailList": None,
  "deviceReplacedEmailList": None,
  "deviceConnectedBackEmailList": None,
  "memoryWarningEmailList": None,
  "memoryLowEmailList": None,
  "memoryCriticalEmailList": None,
  "discUsageWarningEmailList": None,
  "discUsageLowEmailList": None,
  "discUsageCriticalEmailList": None
}

acc_put_alerts= {
  "accountId": jsonnames.ACCOUNTID,
  "policyId": None,
  "batteryWarningEmailList": [
    userName
  ],
  "batteryLowEmailList": [
    userName
  ],
  "batteryCriticalEmailList": None,
  "dataUsageWarningEmailList": None,
  "dataUsageLowEmailList": None,
  "dataUsageCriticalEmailList": None,
  "adminLockedEmailList": None,
  "deviceRebootedEmailList": None,
  "deviceWipedEmailList": None,
  "deviceDeletedEmailList": None,
  "deviceLostEmailList": None,
  "deviceStolenEmailList": None,
  "deviceReplacedEmailList": None,
  "deviceConnectedBackEmailList": None,
  "memoryWarningEmailList": None,
  "memoryLowEmailList": None,
  "memoryCriticalEmailList": None,
  "discUsageWarningEmailList": None,
  "discUsageLowEmailList": None,
  "discUsageCriticalEmailList": None
}
post_acc_alert_configs = {
  "accountId": jsonnames.ACCOUNTID,
  "policyId": None,
  "batteryWarningEmailList": [
    userName
  ],
  "batteryLowEmailList": None,
  "batteryCriticalEmailList": None,
  "dataUsageWarningEmailList": None,
  "dataUsageLowEmailList": None,
  "dataUsageCriticalEmailList": None,
  "adminLockedEmailList": None,
  "deviceRebootedEmailList": None,
  "deviceWipedEmailList": None,
  "deviceDeletedEmailList": None,
  "deviceLostEmailList": None,
  "deviceStolenEmailList": None,
  "deviceReplacedEmailList": None,
  "deviceConnectedBackEmailList": None,
  "memoryWarningEmailList": None,
  "memoryLowEmailList": None,
  "memoryCriticalEmailList": None,
  "discUsageWarningEmailList": None,
  "discUsageLowEmailList": None,
  "discUsageCriticalEmailList": None
}

put_alert_configs = {
  "accountId": jsonnames.ACCOUNTID,
  "policyId": globalcheck.android_policy_id ,
  "batteryWarningEmailList": [
    userName
  ],
  "batteryLowEmailList": [
    userName
  ],
  "batteryCriticalEmailList": [
    userName
  ],
  "dataUsageWarningEmailList": [userName],
  "dataUsageLowEmailList": [userName],
  "dataUsageCriticalEmailList": [userName],
  "kioskLockedEmailList": [
    userName
  ],
  "kioskUnLockedEmailList": [
    userName
  ],
  "adminLockedEmailList": [
    userName
  ],
  "deviceRebootedEmailList": [
    userName
  ],
  "deviceWipedEmailList": [
    userName
  ],
  "deviceDeletedEmailList": [
    userName
  ],
  "deviceLostEmailList": [
    userName
  ],
  "deviceStolenEmailList": [
    userName
  ],
  "deviceReplacedEmailList": [
    userName
  ],
  "deviceConnectedBackEmailList": [
    userName
  ],
  "memoryWarningEmailList": [
    userName
  ],
  "memoryLowEmailList": [
    userName
  ],
  "memoryCriticalEmailList": [
    userName
  ],
  "discUsageWarningEmailList": [userName],
  "discUsageLowEmailList": [userName],
  "discUsageCriticalEmailList": [userName]
}

datausage_configs = {
  "policyId": "5e3ce6c977f85d12cb613271",
  "configs": [
    {
      "notifyAdmin": True,
      "notifyUser": True,
      "value": 525336576,
      "provider": "MOBILE",
      "level": "critical"
    },
    {
      "notifyAdmin": True,
      "notifyUser": True,
      "value": 525336576,
      "provider": "MOBILE",
      "level": "low"
    },
    {
      "notifyAdmin": True,
      "notifyUser": True,
      "value": 525336576,
      "provider": "MOBILE",
      "level": "warning"
    },
    {
      "notifyAdmin": True,
      "notifyUser": True,
      "value": 525336576,
      "provider": "WIFI",
      "level": "critical"
    },
    {
      "notifyAdmin": True,
      "notifyUser": True,
      "value": 525336576,
      "provider": "WIFI",
      "level": "low"
    },
    {
      "notifyAdmin": True,
      "notifyUser": True,
      "value": 525336576,
      "provider": "WIFI",
      "level": "warning"
    }
  ]
}

move_device_android = {
  "policyId": "5e3ce6c977f85d12cb613271",
  "ids": [
    "869881036785080"
  ]
}
update_device_android = {
  "activationCode": actcode,
  "productActivationCode": pactcode,
    "updateDeviceRequest": [
    {
      "deviceID": "869881036785080",
      "replaced": True
    }
  ]
}


android_Name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
group = {
    "groupId":  actcode +"_" + pactcode + "_" + android_Name,
    "groupDisplayName":android_Name ,
    "activation": actcode,
    "productActivation": pactcode,
    "cloneGroupId": None,
    "type": "ANDROID_WM",
    "clonedFrom":"5e3bed2077f85d12cb6104fd" ,
    "clonedFromName": "Default Android Work Managed"
}


appResSchema = {
            "appIds": [
                "app:com.f5.edge.client_ics"
            ]
        }

disable_apps_post = {
  "disabledApps": [
    {
      "name": "Google Chrome: Fast & Secure",
      "pkgId": "com.android.chrome",
      "policyId": "5e3ce6c977f85d12cb613271",
      "disableAppId": " ",
      "appType": " ",
      "nameTemp": "Google Chrome: Fa...",
      "pkgIDTemp": "com.android.chrom...",
      "disable": True,
      "deleted": False,
      "deleteDisable": False,
      "isChecked": True
    }
  ]
}

fcm_updating_policy = {
  "topic": actcode+"_"+pactcode,
  "type": "FCM_UPDATE",
  "isLicenseLevel": True,
  "pId": "5e3bed2077f85d12cb6104fd",
  "actCode": actcode,
  "pActCode": pactcode,
  "priority": "high"
}

approve = {
  "products": [
    "app:com.whatsapp"
  ],
  "approvedPermissions": "allPermissions"
}

disable_apps_put_data = {
  "name": "Slack",
  "pkgId": "com.Slack",
  "policyId": "5e3ce6c977f85d12cb613271",
  "disableAppId": "5f31356ffce9664744905686",
  "appType": "disableApp",
  "pkgIDTemp": "com.Slack",
  "disable": True,
  "deleted": False
}

installs = {
  "installIds": [
    {
      "appId": "app:com.Slack"
    },
    {
      "appId": "app:com.adobe.reader"
    }
  ]
}
uninstalls = {
  "installIds": [
    {
      "appId": "app:com.Slack"
    },
    {
      "appId": "app:com.adobe.reader"
    }
  ]
}

msg_history = {
  "actCode": actcode,
  "pActCode": pactcode,
  "pId": "5e12da3bccc31c1b850a4593",
  "type": "FCM_MESSAGE"
}

track_configs_updating = {
  "id": "5e3bed2077f85d12cb6104fc",
  "trackEnabled": True,
  "postInterval": 1800,
  "events": [],
  "version": 177
}
webox_configs_android = {
  "linkToWeGuard": True,
  "allowDownload": True,
  "allowReDownload": True,
  "allowLiveFileView": True,
  "openWith": True,
  "allowFileView": True,
  "loadFilesFromSDCard": False,
  "loadFromBoth": False,
  "allowDownloadOnlyOnWiFi": False,
  "allowDownloadOnNWWiFI": True,
  "allowDownloadOnNetwork": False
}
webox_configs_iOS = {
  "linkToWeGuard": True,
  "allowDownload": True,
  "allowReDownload": True,
  "allowLiveFileView": True,
  "openWith": True,
  "allowFileView": True,
  "loadFilesFromSDCard": False,
  "loadFromBoth": False,
  "allowDownloadOnlyOnWiFi": False,
  "allowDownloadOnNWWiFI": True,
  "allowDownloadOnNetwork": False
}



# Transfer a device
move_device = {
  "policyId": globalcheck.android_policy_id,
  "ids": [
    "869881036785080"
  ]
}

fcm_update_move_device =   {
  "topic": actcode+"_"+pactcode,
  "type": "FCM_UPDATE",
  "isLicenseLevel": True,
  "pId": "5e71fbacccc31c2c3f905bea",
  "actCode": actcode,
  "pActCode": pactcode,
  "priority": "high"
}

fcm_webox_move_device ={
  "topic": "webox_5e71fbacccc31c2c3f905bea",
  "type": "FCM_CHANGE_GROUP",
  "message": "{\"groupID\":\"5e0ec91fccc31c1b85ea5d1a\",\"deviceList\":[\"869881036785080\"]}",
  "isLicenseLevel": True
}
fcm_files_webox_move_device =  {
  "topic": "webox"+"_"+actcode+"_"+pactcode,
  "type": "FILES_UPDATE",
  "message": "WeBox msg",
  "isLicenseLevel": True
}
fcm_change_group_move_device = {
  "topic": "WT_5e71fbacccc31c2c3f905bea",
  "type": "FCM_CHANGE_GROUP",
  "message": "{\"groupID\":\"5e0ec91fccc31c1b85ea5d1a\",\"deviceList\":[\"869881036785080\"]}",
  "isLicenseLevel": True
}

transfer_device_iOS = {
  "destProfileId": "5eda5312273d1b2ede5ab3ad",
  "deviceIds": [
    "5f324722fce9664744909707"
  ]
}

ios_update_device ={
  "id1": None,
  "id2": None,
  "adminTaggedName": None,
  "lost": True
}


location_config_put = {
  "id": "5f3b8dc4fce9664744e4fd9d",
  "trackEnabled": True,
  "postInterval": 600,
  "events": [],
  "version": 30
}



id = {
  "idToken": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVlOWVlOTdjODQwZjk3ZTAyNTM2ODhhM2I3ZTk0NDczZTUyOGE3YjUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vd2VndWFyZC1lbnQtZGV2IiwiYXVkIjoid2VndWFyZC1lbnQtZGV2IiwiYXV0aF90aW1lIjoxNTg4MDc2MzE1LCJ1c2VyX2lkIjoiZWxpdGVAZ21haWwuY29tIiwic3ViIjoiZWxpdGVAZ21haWwuY29tIiwiaWF0IjoxNTg4MDc2MzE1LCJleHAiOjE1ODgwNzk5MTUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnt9LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.xHBOo7iqBp8LwmWphN4WSWmsQ17jIdTU9mOVq6J4zTw08Rkw2YSMLZ8932XwZpoF_Sr-oKXpVaZa1o5celYu0PXbkQBkA8bdZkXeEHbymHDGweBmxu891P-myO1DtWUqYfVFXzGtzGTT1Dnyo2K-YG9ERMHd55LFoWguQ55_ryaC8xSKx4010JZRrBkQynCELnV__ai6qZd_HJqfmXT9w0ZHHJWLM0vRdD-I6E4NCIs09eTJ2g3mwXWs80q8MmXqxib1-SzQebLoxGfbPRB9zXp1HWlcbf0CsNjjPQa0CdJsua7q6jZJC_5LtvG7fxO5f7DS2QDSm-7Q0MLVWcp7Vw"
 }

fcm_Update = {
  "topic": "WT_"+actcode+"_"+pactcode+"_860362040109798",
  "type": "VIDEO_CALL",
  "isLicenseLevel": False,
  "actCode": actcode,
  "pActCode": pactcode,
  "message": "OPS"+"_"+userName+"_"+"860362040109798_1588047190243",
  "timestamp": start_timestamp
}

Broadcast = {
        "topic": actcode+"_"+pactcode,
        "type": "FCM_MESSAGE",
        "isLicenseLevel": True,
        "actCode": actcode,
        "pActCode": pactcode,
        "message": "{\"bgColor\":\"#000000\",\"textColor\":\"#ffffff\",\"title\":\"Testin\",\"body\":\"on prod\"}",
        "pId": "null",
        "priority": "high"
}


Notes = {
  "deviceId": "860362040109798",
  "note": "REPLACED",
  "policyId": "5e9958fb77f85d51483d01fa",
  "activation": actcode,
  "type": "replaced"
}

save_config_deletedgroup = {
  "companyConfigs": []
}

transfer = {
  "destProfileId": "5e43837177f85d12cb7c30d0",
  "deviceIds": [
    "5ef429f6273d1b2ede86658d"
  ]
}

appBurndown_app_selection = {
      "bundleId": "com.google.chrome.ios",
      "bundleVersion": "80.0.3987.95",
      "profileVersion": 3,
      "profileId": "5e8aa4d677f85d47345ce1df"
}

moveDevice = {

    "actCode": actcode,
    "pActCode": pactcode,
    "policyId": "5e0ec91fccc31c1b85ea5d1a",
    "ids": [
        860362040109798
    ]
}

iospolicy = {
  "deleted": False,
  "createdBy": userName,
  "createdAt": "2020-02-06T10:49:57.738+0000",
  "updatedBy": userName,
  "updatedAt": "2020-07-06T05:07:48.130+0000",
  "activationCode": actcode,
  "companyName": None,
  "productName": None,
  "productCategoryName": None,
  "productActivationCode": pactcode,
  "email": userName,
  "clonedFrom": "5e3bef5577f85d12cb610674",
  "clonedFromName": "Default iOS Non DEP",
  "type": "IOS_NONDEP",
  "token": None,
  "hasParent": False,
  "parentId": None,
  "name": ''.join(random.choices(string.ascii_lowercase + string.digits, k=N)),
  "application": [
    {
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "APP_STORE",
      "ipaId": None,
      "provisioningProfileExpirationDate": None,
      "provisioningProfileName": None,
      "bundleName": "Google Chrome",
      "bundleVersion": None,
      "appImgUrl": "https://is2-ssl.mzstatic.com/image/thumb/Purple113/v4/9b/ad/9e/9bad9eb3-a6b5-92ea-dcf7-25ee873850ac/source/100x100bb.jpg",
      "minimumOsVersion": "12.0",
      "fileSizeInBytes": 72178688,
      "trackId": "535886823",
      "bundleId": "com.google.chrome.ios",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "80.0.3987.95"
    },
    {
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "PRO_APPS",
      "ipaId": "5ee76162273d1b2edea8460f",
      "provisioningProfileExpirationDate": "Sat Sep 26 05:13:01 UTC 2020",
      "provisioningProfileName": "WeTalk Distribution",
      "bundleName": "WeTalk",
      "bundleVersion": "1",
      "appImgUrl": None,
      "minimumOsVersion": "11.0",
      "fileSizeInBytes": 25175219,
      "trackId": None,
      "bundleId": "com.weguard.wetalk",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "1.0.5"
    },
    {
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "APP_STORE",
      "ipaId": None,
      "provisioningProfileExpirationDate": None,
      "provisioningProfileName": None,
      "bundleName": "MyJio: For Everything Jio",
      "bundleVersion": None,
      "appImgUrl": "https://is2-ssl.mzstatic.com/image/thumb/Purple123/v4/6e/81/5a/6e815ad6-73b6-7384-7abb-a6e682e92da9/source/100x100bb.jpg",
      "minimumOsVersion": "10.0",
      "fileSizeInBytes": 238543872,
      "trackId": "1074964262",
      "bundleId": "com.jio.myjio",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "6.0.10"
    },
    {
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "APP_STORE",
      "ipaId": None,
      "provisioningProfileExpirationDate": None,
      "provisioningProfileName": None,
      "bundleName": "Inshorts",
      "bundleVersion": None,
      "appImgUrl": "https://is4-ssl.mzstatic.com/image/thumb/Purple123/v4/c8/67/51/c86751eb-7503-a656-d559-424c60e16a3d/source/100x100bb.jpg",
      "minimumOsVersion": "10.0",
      "fileSizeInBytes": 92367872,
      "trackId": "892146527",
      "bundleId": "com.nis.app",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "5.8.9"
    },
    {
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "PRO_APPS",
      "ipaId": "5ed9e24c273d1b21e44e7a84",
      "provisioningProfileExpirationDate": "Sat Sep 26 05:13:01 UTC 2020",
      "provisioningProfileName": "WeBox Distribution",
      "bundleName": "WeBox",
      "bundleVersion": "1",
      "appImgUrl": None,
      "minimumOsVersion": "11.0",
      "fileSizeInBytes": 13643487,
      "trackId": None,
      "bundleId": "com.weguard.webox",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "1.0.5"
    }
  ],
  "whiteListApps": None,
  "blackListApps": None,
  "restrictions": {
    "allowActivityContinuation": True,
    "allowAddingGameCenterFriends": True,
    "allowAirPlayIncomingRequests": True,
    "allowAirPrint": True,
    "allowAirPrintCredentialsStorage": True,
    "allowAirPrintiBeaconDiscovery": True,
    "allowAppCellularDataModification": True,
    "allowAppInstallation": True,
    "allowAppRemoval": True,
    "allowAssistant": True,
    "allowAssistantWhileLocked": True,
    "allowAutoCorrection": True,
    "allowAutomaticAppDownloads": True,
    "allowBluetoothModification": True,
    "allowBookstore": True,
    "allowBookstoreErotica": True,
    "allowCamera": True,
    "allowCellularPlanModification": True,
    "allowChat": True,
    "allowCloudBackup": True,
    "allowCloudDocumentSync": True,
    "allowCloudPhotoLibrary": True,
    "allowDefinitionLookup": True,
    "allowDeviceNameModification": True,
    "allowDictation": True,
    "allowESIMModification": True,
    "allowEnablingRestrictions": True,
    "allowEnterpriseAppTrust": True,
    "allowEnterpriseBookBackup": True,
    "allowEnterpriseBookMetadataSync": True,
    "allowEraseContentAndSettings": True,
    "allowExplicitContent": True,
    "allowFingerprintForUnlock": True,
    "allowFingerprintModification": True,
    "allowGameCenter": True,
    "allowGlobalBackgroundFetchWhenRoaming": True,
    "allowInAppPurchases": True,
    "allowKeyboardShortcuts": True,
    "allowManagedAppsCloudSync": True,
    "allowMultiplayerGaming": True,
    "allowMusicService": True,
    "allowNews": True,
    "allowNotificationsModification": True,
    "allowOpenFromManagedToUnmanaged": True,
    "allowOpenFromUnmanagedToManaged": True,
    "allowPairedWatch": True,
    "allowPassbookWhileLocked": True,
    "allowPasscodeModification": True,
    "allowPasswordAutoFill": True,
    "allowPasswordProximityRequests": True,
    "allowPasswordSharing": True,
    "allowPersonalHotspotModification": True,
    "allowPhotoStream": True,
    "allowPodcasts": True,
    "allowPredictiveKeyboard": True,
    "allowProximitySetupToNewDevice": True,
    "allowRadioService": True,
    "allowRemoteAppPairing": True,
    "allowRemoteScreenObservation": True,
    "allowSafari": True,
    "allowScreenShot": True,
    "allowSharedStream": True,
    "allowSiriServerLogging": True,
    "allowSpellCheck": True,
    "allowSpotlightInternetResults": True,
    "allowSystemAppRemoval": True,
    "allowUIAppInstallation": True,
    "allowUIConfigurationProfileInstallation": True,
    "allowUSBRestrictedMode": False,
    "allowUntrustedTLSPrompt": True,
    "allowVPNCreation": True,
    "allowVideoConferencing": True,
    "allowVoiceDialing": True,
    "allowWallpaperModification": True,
    "allowiTunes": True,
    "enforcedSoftwareUpdateDelay": 30,
    "forceAirDropUnmanaged": True,
    "forceAirPlayIncomingRequestsPairingPassword": True,
    "forceAirPlayOutgoingRequestsPairingPassword": True,
    "forceAirPrintTrustedTLSRequirement": True,
    "forceAssistantProfanityFilter": True,
    "forceAuthenticationBeforeAutoFill": True,
    "forceAutomaticDateAndTime": True,
    "forceClassroomAutomaticallyJoinClasses": True,
    "forceClassroomRequestPermissionToLeaveClasses": True,
    "forceClassroomUnpromptedAppAndDeviceLock": True,
    "forceClassroomUnpromptedScreenObservation": True,
    "forceDelayedSoftwareUpdates": True,
    "forceEncryptedBackup": True,
    "forceITunesStorePasswordEntry": True,
    "forceLimitAdTracking": True,
    "forceWatchWristDetection": True,
    "forceWiFiWhitelisting": False,
    "ratingApps": 1000,
    "ratingMovies": 1000,
    "ratingRegion": None,
    "ratingTVShows": 1000,
    "safariAcceptCookies": 2,
    "safariAllowAutoFill": True,
    "safariAllowJavaScript": True,
    "safariAllowPopups": False,
    "safariForceFraudWarning": True
  },
  "wifi": [],
  "passcode": None,
  "appLock": None,
  "lockScreenMessage": None,
  "wallpaper": None,
  "qrLink": None,
  "supervised": False,
  "qrExpiry": 1596604068129,
  "devicesCount": 0,
  "categoury": "IOS",
  "licenseType": "iOS Default",
  "disableDelete": True,
  "policyType": "IOS"
}

update_policy_iOS = {
  "deleted": False,
  "createdBy": userName,
  "createdAt": "2020-02-06T10:49:57.738+0000",
  "updatedBy": "wenablesuperadmin@gmail.com",
  "updatedAt": "2020-08-12T04:55:59.514+0000",
  "activationCode": actcode,
  "description": "This is default policy",
  "companyName": None,
  "productName": None,
  "productCategoryName": None,
  "productActivationCode": pactcode,
  "email": userName,
  "clonedFrom": None,
  "clonedFromName": None,
  "type": "IOS_NONDEP",
  "token": None,
  "hasParent": False,
  "parentId": None,
  "name": "Default iOS Non DEP",
  "application": [
    {
      "id": "5e4f79a077f85d12cb7dd64a",
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "APP_STORE",
      "ipaId": None,
      "provisioningProfileExpirationDate": None,
      "provisioningProfileName": None,
      "bundleName": "Google Chrome",
      "bundleVersion": None,
      "appImgUrl": "https://is2-ssl.mzstatic.com/image/thumb/Purple113/v4/9b/ad/9e/9bad9eb3-a6b5-92ea-dcf7-25ee873850ac/source/100x100bb.jpg",
      "minimumOsVersion": "12.0",
      "fileSizeInBytes": 72178688,
      "trackId": "535886823",
      "bundleId": "com.google.chrome.ios",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "80.0.3987.95",
      "isAppInstalled": True,
      "isActive": False
    },
    {
      "id": "5e8ab6cb77f85d2789dd460c",
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "APP_STORE",
      "ipaId": None,
      "provisioningProfileExpirationDate": None,
      "provisioningProfileName": None,
      "bundleName": "MyJio: For Everything Jio",
      "bundleVersion": None,
      "appImgUrl": "https://is2-ssl.mzstatic.com/image/thumb/Purple123/v4/6e/81/5a/6e815ad6-73b6-7384-7abb-a6e682e92da9/source/100x100bb.jpg",
      "minimumOsVersion": "10.0",
      "fileSizeInBytes": 238543872,
      "trackId": "1074964262",
      "bundleId": "com.jio.myjio",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "6.0.10",
      "isAppInstalled": True,
      "isActive": False
    },
    {
      "id": "5e3bfa4477f85d12cb610b8e",
      "email": userName,
      "activationCode": actcode,
      "productActivationCode": pactcode,
      "deleted": False,
      "appType": "APP_STORE",
      "ipaId": None,
      "provisioningProfileExpirationDate": None,
      "provisioningProfileName": None,
      "bundleName": "Inshorts",
      "bundleVersion": None,
      "appImgUrl": "https://is4-ssl.mzstatic.com/image/thumb/Purple123/v4/c8/67/51/c86751eb-7503-a656-d559-424c60e16a3d/source/100x100bb.jpg",
      "minimumOsVersion": "10.0",
      "fileSizeInBytes": 92367872,
      "trackId": "892146527",
      "bundleId": "com.nis.app",
      "profileId": "5e3bef5577f85d12cb610674",
      "appVersion": "5.8.9",
      "isAppInstalled": True,
      "isActive": False
    }
  ],
  "whiteListApps": [],
  "blackListApps": [],
  "restrictions": {
    "allowActivityContinuation": True,
    "allowAddingGameCenterFriends": True,
    "allowAirPlayIncomingRequests": True,
    "allowAirPrint": True,
    "allowAirPrintCredentialsStorage": True,
    "allowAirPrintiBeaconDiscovery": True,
    "allowAppCellularDataModification": True,
    "allowAppInstallation": True,
    "allowAppRemoval": True,
    "allowAssistant": True,
    "allowAssistantWhileLocked": True,
    "allowAutoCorrection": True,
    "allowAutomaticAppDownloads": True,
    "allowBluetoothModification": True,
    "allowBookstore": True,
    "allowBookstoreErotica": True,
    "allowCamera": True,
    "allowCellularPlanModification": True,
    "allowChat": True,
    "allowCloudBackup": True,
    "allowCloudDocumentSync": True,
    "allowCloudPhotoLibrary": True,
    "allowDefinitionLookup": True,
    "allowDeviceNameModification": True,
    "allowDictation": True,
    "allowESIMModification": True,
    "allowEnablingRestrictions": True,
    "allowEnterpriseAppTrust": True,
    "allowEnterpriseBookBackup": True,
    "allowEnterpriseBookMetadataSync": True,
    "allowEraseContentAndSettings": True,
    "allowExplicitContent": True,
    "allowFingerprintForUnlock": True,
    "allowFingerprintModification": True,
    "allowGameCenter": True,
    "allowGlobalBackgroundFetchWhenRoaming": True,
    "allowInAppPurchases": True,
    "allowKeyboardShortcuts": True,
    "allowManagedAppsCloudSync": True,
    "allowMultiplayerGaming": True,
    "allowMusicService": True,
    "allowNews": True,
    "allowNotificationsModification": True,
    "allowOpenFromManagedToUnmanaged": True,
    "allowOpenFromUnmanagedToManaged": True,
    "allowPairedWatch": True,
    "allowPassbookWhileLocked": True,
    "allowPasscodeModification": True,
    "allowPasswordAutoFill": True,
    "allowPasswordProximityRequests": True,
    "allowPasswordSharing": True,
    "allowPersonalHotspotModification": True,
    "allowPhotoStream": True,
    "allowPodcasts": True,
    "allowPredictiveKeyboard": True,
    "allowProximitySetupToNewDevice": True,
    "allowRadioService": True,
    "allowRemoteAppPairing": True,
    "allowRemoteScreenObservation": True,
    "allowSafari": True,
    "allowScreenShot": True,
    "allowSharedStream": True,
    "allowSiriServerLogging": True,
    "allowSpellCheck": True,
    "allowSpotlightInternetResults": True,
    "allowSystemAppRemoval": True,
    "allowUIAppInstallation": True,
    "allowUIConfigurationProfileInstallation": True,
    "allowUSBRestrictedMode": False,
    "allowUntrustedTLSPrompt": True,
    "allowVPNCreation": True,
    "allowVideoConferencing": True,
    "allowVoiceDialing": True,
    "allowWallpaperModification": True,
    "allowiTunes": True,
    "enforcedSoftwareUpdateDelay": 30,
    "forceAirDropUnmanaged": True,
    "forceAirPlayIncomingRequestsPairingPassword": True,
    "forceAirPlayOutgoingRequestsPairingPassword": True,
    "forceAirPrintTrustedTLSRequirement": True,
    "forceAssistantProfanityFilter": True,
    "forceAuthenticationBeforeAutoFill": True,
    "forceAutomaticDateAndTime": True,
    "forceClassroomAutomaticallyJoinClasses": True,
    "forceClassroomRequestPermissionToLeaveClasses": True,
    "forceClassroomUnpromptedAppAndDeviceLock": True,
    "forceClassroomUnpromptedScreenObservation": True,
    "forceDelayedSoftwareUpdates": True,
    "forceEncryptedBackup": True,
    "forceITunesStorePasswordEntry": True,
    "forceLimitAdTracking": True,
    "forceWatchWristDetection": True,
    "forceWiFiWhitelisting": False,
    "ratingApps": 1000,
    "ratingMovies": 1000,
    "ratingRegion": None,
    "ratingTVShows": 1000,
    "safariAcceptCookies": 2,
    "safariAllowAutoFill": True,
    "safariAllowJavaScript": True,
    "safariAllowPopups": False,
    "safariForceFraudWarning": True
  },
  "wifi": [],
  "passcode": None,
  "appLock": None,
  "lockScreenMessage": {},
  "wallpaper": {},
  "qrLink": None,
  "supervised": False,
  "qrExpiry": 1596604068129,
  "productInfo": {
    "activationCode": None,
    "autoInstallMode": "forceAutoInstall",
    "suspendedSettingsApp": None,
    "autoUpdatePolicy": "always",
    "companyName": None,
    "productName": None,
    "productCategoryName": None,
    "productActivationCode": None,
    "field1": "697FA5312DE775BED6F0E61F2663D29D2A2F72E9DC5F4724808CBC9C7942477EA7F28E0503E01ED4A3638C4E063F095601A5937FC70683B71B88AB995D15C5E2",
    "field2": "com.weguard.android",
    "field3": "123456",
    "field4": None,
    "field5": None,
    "personaAppList": [],
    "emmPlayApps": [],
    "appVersion": None,
    "appVersionCode": 0,
    "appCheckSum": None,
    "appSize": 0,
    "urlToDownload": None,
    "unlockPasscode": None,
    "timeIntervalToPoll": 3600,
    "weguardAppVersion": None,
    "wegVersionCode": 0,
    "wegAppSize": 0,
    "wegCheckSum": None,
    "weguardAppUrlToDownload": None,
    "wegHash": None,
    "weGuardPolltime": 3600,
    "forceLaunch": False,
    "isUnlockSet": False,
    "allowFOTAUpdates": True,
    "personaBasedProvision": True,
    "personaName": None,
    "personaImageURL": None,
    "personImageChecksum": None,
    "personImageSize": 0,
    "wallpaperUrl": None,
    "wallpaperChecksum": None,
    "wallpaperImageSize": 0,
    "shouldDeactivateProduct": False,
    "settingsList": [],
    "fileList": None,
    "policy": {
      "shouldBlockBrowser": True,
      "shouldBlockYoutube": True,
      "shouldBlockAndroidMarket": False,
      "shouldBlockVoiceDialer": True,
      "shouldBlockNotifications": "",
      "shouldDeactivateProduct": False,
      "shouldAllowWipe": False,
      "hideSystemBar": False,
      "allowStatubarExpansion": True,
      "allowSettingsChange": True,
      "allowWallpaperChange": False,
      "allowPowerSavingMode": False,
      "allowPowerOff": True,
      "removeAllWidgets": True,
      "roamingData": False,
      "allowScreenCapture": False,
      "removeAllShortcuts": True,
      "maximumTimeToLock": 0,
      "keyguardDisabledFeatures": [],
      "defaultPermissionPolicy": 0,
      "permissionPolicy": [],
      "openNetworkConfiguration": {
        "networkConfigurations": []
      },
      "systemUpdate": None,
      "accountTypesWithManagementDisabled": [],
      "addUserDisabled": True,
      "adjustVolumeDisabled": False,
      "factoryResetDisabled": True,
      "installAppsDisabled": False,
      "safeBootDisabled": True,
      "uninstallAppsDisabled": True,
      "statusBarDisabled": False,
      "keyguardDisabled": True,
      "bluetoothContactSharingDisabled": True,
      "mountPhysicalMediaDisabled": True,
      "shortSupportMessage": {
        "localizedMessages": {},
        "defaultMessage": None
      },
      "longSupportMessage": {
        "localizedMessages": {},
        "defaultMessage": None
      },
      "passwordRequirements": None,
      "bluetoothConfigDisabled": False,
      "cellBroadcastsConfigDisabled": False,
      "credentialsConfigDisabled": False,
      "mobileNetworksConfigDisabled": False,
      "tetheringConfigDisabled": False,
      "vpnConfigDisabled": False,
      "wifiConfigDisabled": False,
      "createWindowsDisabled": False,
      "systemErrorDialogDisallow": False,
      "networkResetDisabled": False,
      "outgoingBeamDisabled": False,
      "outgoingCallsDisabled": False,
      "removeUserDisabled": False,
      "shareLocationDisabled": False,
      "smsDisabled": False,
      "unmuteMicrophoneDisabled": False,
      "usbFileTransferDisabled": False,
      "ensureVerifyAppsEnabled": False,
      "bluetoothSharingEmabled": False,
      "keepDeviceOnWhilePlugiIn": False,
      "cameraDisabled": False,
      "permittedInputMethods": {
        "packageNames": []
      },
      "recommendedGlobalProxy": {
        "host": None,
        "port": 0,
        "excludedHosts": [],
        "pacUri": None
      },
      "clearGlobalProxies": False,
      "organizationName": "",
      "setWallpaperDisabled": False,
      "certificateManagement": {
        "installCACert": {
          "location": None
        },
        "removePublicPrivateCKeyPairs": False,
        "removeAllCACerts": False,
        "installPublicPrivateKeyPair": {
          "location": None
        }
      },
      "alwaysOnVpnPackage": {
        "id": None,
        "deleted": False,
        "createdBy": None,
        "createdAt": None,
        "updatedBy": None,
        "updatedAt": None,
        "version": None,
        "packageName": None,
        "lockdownEnabled": False
      },
      "dataRoamingDisabled": False,
      "bluetoothDisabled": False,
      "blockUnInstallByPcakageName": {
        "pkgID": []
      },
      "installUnknownSourcesAllowed": False,
      "debuggingFeaturesAllowed": False,
      "funDisabled": False,
      "autoFillDisabled": False,
      "autoBrightnessDisabled": False,
      "autoTimeRequired": False,
      "statusBarColor": None,
      "textColor": None,
      "personaHomeBgColor": "#009487",
      "personaBgColor": "#009487",
      "disableCellularData": False,
      "disableMicroPhone": False,
      "alwaysScreenOn": False,
      "disableWPOnFullyManaged": False,
      "disableAirplaneMode": True,
      "disableGoogleCrashReport": True,
      "disableNotifications": True,
      "enableKioskPassword": False
    },
    "enterpriseID": enterpriseId,
    "launchOnBoot": None,
    "weTalkDisabled": False,
    "weBoxDisabled": False,
    "enableLiveView": False,
    "unlockSet": False
  },
  "devicesCount": 0,
  "categoury": "IOS",
  "licenseType": "iOS Default",
  "disableDelete": True,
  "policyType": "IOS"
}




update_policy_android = {
  "id": "5f16de4274e8b77ecc4fecf7",
  "deleted": False,
  "createdBy": userName,
  "createdAt": "2020-07-21T12:23:30.570+0000",
  "updatedBy": userName,
  "updatedAt": "2020-07-27T04:20:00.075+0000",
  "licenseQuantity": 0,
  "usedQuantity": 0,
  "osType": None,
  "product": None,
  "expired": False,
  "productInfo": {
    "activationCode": actcode,
    "autoInstallMode": "forceAutoInstall",
    "companyName": companyName,
    "productName": None,
    "productCategoryName": None,
    "productActivationCode": pactcode,
    "field3": "596418",
    "field4": None,
    "field5": "{\"allowStatubarExpansion\":True,\"allowSettingsChange\":True,\"allowWallpaperChange\":False,\"hideSystemBar\":False,\"removeAllWidgets\":False,\"removeAllShortcuts\":False,\"statusBarColor\":\"#000000\",\"personaBgColor\":\"#000000\",\"allowPowerSavingMode\":False,\"textColor\":\"#FFFFFF\",\"allowScreenCapture\":True,\"personaHomeBgColor\":\"#000000\",\"roamingData\":True,\"favoriteAppList\":[],\"allowPowerOff\":True}",
    "personaAppList": [
      {
        "id": None,
        "deleted": False,
        "createdBy": None,
        "createdAt": None,
        "updatedBy": None,
        "updatedAt": None,
        "appName": "AirDroid Remote access File_v4.2.5.0_apkpure.com",
        "appID": "com.sand.airdroid",
        "urlToDownload": "https://cache.weguard.io/6HHTQ/LINE-XAHTH/com.sand.airdroid/30280/com.sand.airdroid-30280.apk",
        "appVersion": "4.2.5.0",
        "versionCode": 30280,
        "type": "white_list",
        "playstoreApp": False,
        "checksum": "4d837d829aa6c6c8ea5377a48edd414f",
        "apkSize": 42101340,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False
      },
      {
        "id": None,
        "deleted": False,
        "createdBy": None,
        "createdAt": None,
        "updatedBy": None,
        "updatedAt": None,
        "appName": "PlayStore-Hide",
        "appID": "com.android.vending",
        "urlToDownload": None,
        "appVersion": None,
        "versionCode": 0,
        "type": "white_list",
        "playstoreApp": False,
        "checksum": None,
        "apkSize": 0,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": True,
        "status": True
      },
      {
        "id": "5caefac7ccc31c184c35c1d5",
        "deleted": False,
        "createdBy": userName,
        "createdAt": "2019-04-11T08:28:55.671+0000",
        "updatedBy": userName,
        "updatedAt": "2019-04-11T08:28:55.671+0000",
        "appName": "Filter Provider",
        "appID": "com.samsung.android.provider.filterprovider",
        "urlToDownload": None,
        "appVersion": "3.0.08",
        "versionCode": 300800000,
        "type": None,
        "playstoreApp": False,
        "checksum": None,
        "apkSize": 0,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False,
        "status": True
      },
      {
        "id": "5caefac7ccc31c184c35c1d4",
        "deleted": False,
        "createdBy": userName,
        "createdAt": "2019-04-11T08:28:55.657+0000",
        "updatedBy": userName,
        "updatedAt": "2019-04-11T08:28:55.657+0000",
        "appName": "Beaming Service",
        "appID": "com.mobeam.barcodeService",
        "urlToDownload": None,
        "appVersion": "1.3.8  ",
        "versionCode": 25,
        "type": None,
        "playstoreApp": False,
        "checksum": None,
        "apkSize": 0,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False,
        "status": True
      },
      {
        "id": "5caefac7ccc31c184c35c1df",
        "deleted": False,
        "createdBy": userName,
        "createdAt": "2019-04-11T08:28:55.688+0000",
        "updatedBy": userName,
        "updatedAt": "2019-04-11T08:28:55.688+0000",
        "appName": "Dialer Storage",
        "appID": "com.android.providers.telephony",
        "urlToDownload": None,
        "appVersion": "7.0",
        "versionCode": 24,
        "type": None,
        "playstoreApp": False,
        "checksum": None,
        "apkSize": 0,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False,
        "status": True
      },
      {
        "id": "5caefac7ccc31c184c35c1de",
        "deleted": False,
        "createdBy": userName,
        "createdAt": "2019-04-11T08:28:55.687+0000",
        "updatedBy": userName,
        "updatedAt": "2019-04-11T08:28:55.687+0000",
        "appName": "Android Services Library",
        "appID": "com.google.android.ext.services",
        "urlToDownload": None,
        "appVersion": "1",
        "versionCode": 1,
        "type": None,
        "playstoreApp": False,
        "checksum": None,
        "apkSize": 0,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False,
        "status": True
      },
      {
        "id": None,
        "deleted": False,
        "createdBy": None,
        "createdAt": None,
        "updatedBy": None,
        "updatedAt": None,
        "appName": "WeBox",
        "appID": "com.webox.android",
        "urlToDownload": "https://get.weguard.io/weguard/proapps/WeBox_v1.4.58.apk",
        "appVersion": "1.4.58",
        "versionCode": 140058,
        "type": "white_list",
        "playstoreApp": False,
        "checksum": "f1e80a46365c9bd5c7afb57d9e74c611",
        "apkSize": 30485568,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False
      },
      {
        "id": None,
        "deleted": False,
        "createdBy": None,
        "createdAt": None,
        "updatedBy": None,
        "updatedAt": None,
        "appName": "WeTalk",
        "appID": "com.wetalk.android",
        "urlToDownload": " https://cache.weguard.io/proapps/com.wetalk.android/140028/com.wetalk.android-140028.apk",
        "appVersion": "1.4.28",
        "versionCode": 140028,
        "type": "white_list",
        "playstoreApp": False,
        "checksum": "ece3fa55f6adf080424fb4cbcd3b2c88",
        "apkSize": 33335377,
        "launcherIntentPkg": None,
        "launcherIntentActivity": None,
        "launcherIntentFlag": False,
        "hideApp": False
      }
    ],
    "emmPlayApps": [
      {
        "appId": "app:com.google.android.apps.enterprise.dmagent",
        "appName": "Google.android.apps.enterprise.dmagent",
        "managedConfigModel": None,
        "supportsConfig": False,
        "launcherIntent": None
      },
      {
        "appId": "app:com.google.android.apps.meetings",
        "appName": "Google.android.apps.meetings",
        "managedConfigModel": None,
        "supportsConfig": False,
        "launcherIntent": None
      },
      {
        "appId": "app:com.google.android.apps.docs",
        "appName": "Google.android.apps.docs",
        "managedConfigModel": None,
        "supportsConfig": False,
        "launcherIntent": None
      },
      {
        "appId": "app:com.google.android.gm",
        "appName": "Gmail",
        "managedConfigModel": None,
        "supportsConfig": True,
        "launcherIntent": None
      },
      {
        "appId": "app:com.lexa.fakegps",
        "appName": "Lexa.fakegps",
        "managedConfigModel": None,
        "supportsConfig": False,
        "launcherIntent": None
      },
      {
        "appId": "app:com.cisco.anyconnect.vpn.android.avf",
        "appName": "Cisco.anyconnect.vpn.android.avf",
        "managedConfigModel": None,
        "supportsConfig": True,
        "launcherIntent": None
      },
      {
        "appId": "app:org.mozilla.firefox",
        "appName": "Mozilla.firefox",
        "managedConfigModel": None,
        "supportsConfig": False,
        "launcherIntent": None
      }
    ],
    "appVersion": None,
    "appVersionCode": 0,
    "appCheckSum": None,
    "appSize": 0,
    "urlToDownload": None,
    "unlockPasscode": None,
    "timeIntervalToPoll": 3600,
    "weguardAppVersion": "4.10.90",
    "wegVersionCode": 500090,
    "wegAppSize": 18840080,
    "wegCheckSum": "cbfd85697adb97ce5bcf5be63921d657",
    "weguardAppUrlToDownload": None,
    "weGuardPolltime": 3600,
    "forceLaunch": False,
    "allowFOTAUpdates": True,
    "wallpaperUrl": None,
    "wallpaperChecksum": None,
    "wallpaperImageSize": 0,
    "adminLocked": False,
    "personaBasedProvision": True,
    "personaName": "Desert",
    "personaImageURL": "https://cache.weguard.io/6HHTQ/LINE-XAHTH/Desert.jpg",
    "personImageChecksum": "ba45c8f60456a672e003a875e469d0eb",
    "personImageSize": 845941,
    "shouldDeactivateProduct": False,
    "settingsList": [
      "WIFI_NONE",
      "BT_NONE",
      "NFC-Off",
      "ScreenRotation-On",
      "DataUsage-Off",
      "ErrorReporting-Off",
      "Messaging-On",
      "status_bar-Off",
      "allowUnlock-On",
      "Location"
    ],
    "fileList": None,
    "policy": {
      "shouldBlockBrowser": False,
      "shouldBlockYoutube": False,
      "shouldBlockAndroidMarket": False,
      "shouldBlockVoiceDialer": True,
      "shouldBlockNotifications": "",
      "shouldDeactivateProduct": False,
      "shouldAllowWipe": False,
      "hideSystemBar": False,
      "allowStatubarExpansion": False,
      "allowSettingsChange": True,
      "allowWallpaperChange": False,
      "allowPowerSavingMode": False,
      "allowPowerOff": True,
      "removeAllWidgets": False,
      "roamingData": False,
      "allowScreenCapture": False,
      "removeAllShortcuts": False,
      "maximumTimeToLock": 0,
      "keyguardDisabledFeatures": [],
      "defaultPermissionPolicy": 0,
      "permissionPolicy": [],
      "openNetworkConfiguration": {
        "networkConfigurations": []
      },
      "systemUpdate": {
        "type": None,
        "startMinutes": 0,
        "endMinutes": 0
      },
      "accountTypesWithManagementDisabled": [
        "com.google.work"
      ],
      "addUserDisabled": True,
      "adjustVolumeDisabled": False,
      "factoryResetDisabled": False,
      "installAppsDisabled": False,
      "safeBootDisabled": False,
      "uninstallAppsDisabled": False,
      "statusBarDisabled": False,
      "keyguardDisabled": False,
      "bluetoothContactSharingDisabled": True,
      "mountPhysicalMediaDisabled": False,
      "shortSupportMessage": {
        "localizedMessages": {},
        "defaultMessage": "This device is managed by LinenClub___46930"
      },
      "longSupportMessage": {
        "localizedMessages": {},
        "defaultMessage": "This device is managed by LinenClub___46930\n Please contact Admin@LinenClub___46930"
      },
      "passwordRequirements": {
        "passwordExpirationTimeout": 0,
        "passwordHistoryLength": 0,
        "passwordQuality": 0,
        "passwordMinimumLength": 0,
        "passwordMinimumLetters": 0,
        "passwordMinimumLowerCase": 0,
        "passwordMinimumNonLetter": 0,
        "passwordMinimumNumeric": 0,
        "passwordMinimumSymbols": 0,
        "passwordMinimumUpperCase": 0,
        "maximumFailedPasswordsForWipe": 0,
        "passwordScope": "SCOPE_DEVICE"
      },
      "bluetoothConfigDisabled": False,
      "cellBroadcastsConfigDisabled": False,
      "credentialsConfigDisabled": False,
      "mobileNetworksConfigDisabled": False,
      "tetheringConfigDisabled": False,
      "vpnConfigDisabled": False,
      "wifiConfigDisabled": False,
      "createWindowsDisabled": False,
      "systemErrorDialogDisallow": False,
      "networkResetDisabled": False,
      "outgoingBeamDisabled": False,
      "outgoingCallsDisabled": False,
      "removeUserDisabled": False,
      "shareLocationDisabled": False,
      "smsDisabled": False,
      "unmuteMicrophoneDisabled": False,
      "usbFileTransferDisabled": False,
      "ensureVerifyAppsEnabled": False,
      "bluetoothSharingEmabled": False,
      "keepDeviceOnWhilePlugiIn": False,
      "cameraDisabled": False,
      "permittedInputMethods": {
        "packageNames": [
          "com.apedroid.hwkeyboardhelperdemo"
        ]
      },
      "recommendedGlobalProxy": {
        "host": None,
        "port": 0,
        "excludedHosts": [],
        "pacUri": None
      },
      "clearGlobalProxies": False,
      "organizationName": "",
      "setWallpaperDisabled": False,
      "certificateManagement": {
        "installCACert": {
          "location": None
        },
        "removePublicPrivateCKeyPairs": False,
        "removeAllCACerts": False,
        "installPublicPrivateKeyPair": {
          "location": None
        }
      },
      "alwaysOnVpnPackage": {
        "id": None,
        "deleted": False,
        "createdBy": userName,
        "createdAt": "2020-07-21T12:23:30.570+0000",
        "updatedBy": userName,
        "updatedAt": "2020-07-27T04:20:00.075+0000",
        "version": None,
        "packageName": None,
        "lockdownEnabled": False
      },
      "dataRoamingDisabled": False,
      "bluetoothDisabled": False,
      "blockUnInstallByPcakageName": {
        "pkgID": []
      },
      "installUnknownSourcesAllowed": False,
      "debuggingFeaturesAllowed": False,
      "funDisabled": False,
      "autoFillDisabled": False,
      "autoBrightnessDisabled": False,
      "autoTimeRequired": False,
      "statusBarColor": "#0a0a0a",
      "textColor": "#f9f6f6",
      "personaHomeBgColor": "#009487",
      "personaBgColor": "#82124c",
      "disableCellularData": False,
      "disableMicroPhone": False,
      "disableWPOnFullyManaged": False,
      "disableAirplaneMode": True,
      "disableGoogleCrashReport": True,
      "disableNotifications": True,
      "stayOnPluggedModes": [],
      "frpAdminEmails": [],
      "statusReportingSettings": {},
      "passwordPolicies": [],
      "applications": [],
      "screenCaptureDisabled": False,
      "persistentPreferredActivities": [],
      "appAutoUpdatePolicy": "WIFI_ONLY",
      "playStoreMode": False,
      "complianceRules": [],
      "choosePrivateKeyRules": [],
      "prevAppDataUsageList": [],
      "enablePreventAppUsage": True
    },
    "enterpriseID": enterpriseId,
    "launchOnBoot": None,
    "weTalkDisabled": False,
    "weBoxDisabled": False,
    "enableLiveView": False,
    "suspendedSettingsApp": [],
    "autoUpdatePolicy": "always",
    "unlockSet": False,
    "isPlayStoreEnabled": True
  },
  "key_type": None,
  "userID": None,
  "retailerID": None,
  "groupId": actcode+"_"+pactcode+"_AI WM Russia",
  "groupDisplayName": "AI WM Russia",
  "name": "AI WM Russia",
  "type": "ANDROID_WM",
  "description": "This is default policy",
  "clonedFrom": "5e253094ccc31c20f817033f",
  "clonedFromName": "Default Android Work Managed",
  "deviceType": None,
  "categoury": "Android",
  "disableDelete": False,
  "licenseType": "Android Group",
  "policyType": "Android",
  "disableKIOSKTab": True
}




