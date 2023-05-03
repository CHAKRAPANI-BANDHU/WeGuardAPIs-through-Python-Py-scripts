# If you turn this off, login will not be executed and subsequent test cases should be skipped.
must_run = 1


# Run only selected tests that I need to execute. Usually this should be normally set to 0
my_cases = 0

# Turn it to 1 for sanity tests only, 0 to execute other tests.
sanitytest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
regressiontest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
usualtest = 0

# Turn it to 1 for regression tests only, 0 to execute other tests.
regression_tests = 0

# Turn it to 1 for avoid tests only, 0 to execute other tests.
avoid_test_cases = 0

negative_tests = 1
positive_tests = 1



# Run all positive and negative cases
test_tc_000001_AccountAdmin_login = 1
test_tc_000001_AccountAdmin_Logout = 1
test_tc_000001_AccountAdmin_Invalid_Credentials = 1
test_tc_000001_AccountAdmin_Invalid_Email = 1
test_tc_000001_AccountAdmin_Invalid_Password = 1
test_tc_000001_AccountAdmin_Credentials_With_Spaces = 1
test_tc_000001_AccountAdmin_WithOut_Password = 1
test_tc_000001_AccountAdmin_WithOut_UserName = 1
test_tc_000001_AccountAdmin_WithOut_UserName_Password = 1

#Certificate
test_tc_000001_GET_Certificates=1

#WeBox
test_tc_001_WeBox_AllowDownload=1
test_tc_001_WeBox_licensepagesize=1
test_tc_001_WeBox_FilesinAndroidPolicies=1
test_tc_001_WeBox_FilesiniOSPolicies=1
test_tc_001_WeBox_iOSConfigs=1
test_tc_001_WeBox_iOSPolicy=1
test_tc_001_WeBox_AndroidPolicy=1
test_tc_001_WeBox_undosave=1
test_tc_001_Webox_filespost=1
test_tc_001_WeBox_Uploader=1
test_tc_001_WeBox_AllowFileView=1
test_tc_001_WeBox_OpenWith=1
test_tc_001_WeBox_ShowLinks=1
test_tc_001_noWeBoxConfigs=1
test_tc_001_WeBoxEnabledAllowDownload=1
test_tc_001_WeBoxEnabledAllowFileView =1
test_tc_001_EnabledServiceTypes =1
test_tc_001_WeBoxDisabledServiceTypes=1
test_tc_001_WeBoxEnabledShowLinks=1
test_tc_001_WeBoxEnabledOpenWith=1
test_tc_001_DisabledWeBoxPasscode =1
test_tc_001_EnabledWeBoxPasscode =1
test_tc_001_EnabledGoogleDriveDropbox =1
test_tc_001_AddingfoldersforSDcard =1
test_tc_001_AddingfoldersforGoogleDrive =1
test_tc_001_AddingfoldersforAmazonS3 =1
test_tc_001_AddingfoldersforDropbox =1
test_tc_001_EnabledSDcardAmazonS3=1
test_tc_001_DisabledSDcardAmazonS3=1
test_tc_001_DisabledGoogleDriveDropbox =1
test_tc_001_DeletingfoldersforAmazonS3= 1
test_tc_001_DeletingfoldersforGoogleDrive = 1
test_tc_001_DeletingfoldersforSDCard = 1
test_tc_001_DeletingfoldersforDropbox = 1
test_tc_001_DeviceUploads_GlobalSharedFolders = 1
test_tc_001_DeviceUploads_PolicyGroupsFolders = 1
test_tc_001_WeBox_DeviceUploads_pdf=1
test_tc_001_WeBox_DeviceUploads_zip=1
test_tc_001_DeviceUploads_CreateGlobalSharedFolders = 1
test_tc_001_DeviceUploads_CreatePolicyGroupsFolders = 1
test_tc_001_DeviceUploads_WeBoxuploadconfigingroupsfolder=1
test_tc_001_DeviceUploads_PolicyGorupFolders_WeBoxuploadconfigwithsign=1
test_tc_001_DeviceUploads_PolicyGorupFolders_WeBoxuploadconfigwithoutsign=1
test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithsign=1
test_tc_001_DeviceUploads_SharedFolders_WeBoxuploadconfigwithoutsign=1
test_tc_001_DeviceUploads_WeBoxuploadconfiginglobalsharedfolder=1
test_tc_001_DeviceUploads_GlobalSharedFolders_viewfilesinsharedfolder=1
test_tc_001_DeviceUploads_PolicyGroupsFolders_viewfilesinpolicyfolder=1
test_tc_001_DeviceUploads_GlobalSharedFolders_filesbyclickingonclearinsharedfolders=1
test_tc_001_DeviceUploads_PolicyGroupsFolders_filesbyclickingonclearinpolicyfolders=1
test_tc_001_DeviceUploads_SharedFolders_config=1
test_tc_001_WeBox_SVGUpload=1
test_tc_001_WeBox_MP3Upload=1
test_tc_001_WeBox_MP4Upload=1
test_tc_001_WeBox_OGGUpload=1
test_tc_001_WeBox_TXTUpload=1
test_tc_001_WeBox_DOCUpload=1
test_tc_001_WeBox_DOCXUpload=1
test_tc_001_WeBox_CSVUpload=1
test_tc_001_WeBox_XLSXUpload=1
test_tc_001_WeBox_WAVUpload=1
test_tc_001_WeBox_APKUpload=1
test_tc_001_WeBox_ZIPUpload=1
test_tc_001_WeBox_GIFUpload=1
test_tc_001_WeBox_JPGUpload=1
test_tc_001_WeBox_MOVUpload=1
test_tc_001_WeBox_PNGUpload=1
test_tc_001_WeBox_PDFUpload=1
test_tc_001_WeBox_PPTXUpload=1
test_tc_001_WeBox_MPEGUpload=1
test_tc_001_WeBox_WEBMUpload=1
test_tc_001_GLobalLevel_UploadCertificate =1
filtersbyalldiffeventspolicy=1
test_tc_001_AuditLogs_filtersbydebugALLdaterange=1
test_tc_001_AuditLogs_filtersbywarnALLdaterange=1
test_tc_001_AuditLogs_filtersbyinfoALLdaterange=1
test_tc_001_AuditLogs_filtersbyerrorALLdaterange=1
test_tc_001_AuditLogs_filtersbyalllogindaterange=1
test_tc_001_AuditLogs_filtersbyALLdaterange=1


# Audit Logs
# Filters by level
test_tc_001_AuditLogs_filtersbyALL=1
test_tc_001_AuditLogs_filtersbydebugALL=1
test_tc_001_AuditLogs_filtersbywarnALL=1
test_tc_001_AuditLogs_filtersbyerrorALL=1
test_tc_001_AuditLogs_filtersbyinfoALL=1
# UI Logs based on Filter by level as ALL
test_tc_001_AuditLogs_filtersbyallLogin=1
test_tc_001_AuditLogs_filtersbyalllogout=1
test_tc_001_AuditLogs_filtersbyallSimper=1
test_tc_001_AuditLogs_filtersbyallEimper=1
test_tc_001_AuditLogs_filtersbyallpolicy=1
test_tc_001_AuditLogs_filtersbyalldevice=1
test_tc_001_AuditLogs_filtersbyallgroups=1
test_tc_001_AuditLogs_filtersbyallupload=1
test_tc_001_AuditLogs_filtersbyallcommands=1
test_tc_001_AuditLogs_filtersbyallbroadcast=1
test_tc_001_AuditLogs_filtersbyallwetalk=1
test_tc_001_AuditLogs_filtersbyallweboxpass=1
test_tc_001_AuditLogs_filtersbyallrolespermission=1
test_tc_001_AuditLogs_filtersbyallkioskpass=1
# Search for Android and iOS device logs
test_tc_001_AuditLogs_searchAndroidimei=1
test_tc_001_AuditLogs_searchiOSimei=1
# Yesterday Logs
test_tc_001_AuditLogs_filtersbyAllyesterday=1
# Custom Date range Logs
test_tc_001_AuditLogs_filtersbyAllCustomDateRange=1
# Android Device Logs
test_tc_001_AuditLogs_filterbyAll=1
test_tc_001_AuditLogs_filtersbykiosklockunlock=1
test_tc_001_AuditLogs_filtersbylicenseactivation=1
test_tc_001_AuditLogs_filtersbyprovisioningprofile=1
test_tc_001_AuditLogs_filtersbygetlicense=1
test_tc_001_AuditLogs_filtersbypollevents=1
test_tc_001_AuditLogs_filtersbycrashevent=1
test_tc_001_AuditLogs_filtersbydatausage=1
test_tc_001_AuditLogs_filtersbywipeevent=1
test_tc_001_AuditLogs_filtersbypusheevents=1
test_tc_001_AuditLogs_filtersbyWeGuardappevent=1
test_tc_001_AuditLogs_filtersbyotherevent=1
# iOS Device Logs
test_tc_001_AuditLogs_filtersbyalldevinfo=1
test_tc_001_AuditLogs_filtersbyallclrpass=1
test_tc_001_AuditLogs_filtersbyalldevlock=1
test_tc_001_AuditLogs_filtersbyallinstallapp=1
test_tc_001_AuditLogs_filtersbyallremapp=1
test_tc_001_AuditLogs_filtersbyallinstallprof=1
test_tc_001_AuditLogs_filtersbyallinstallpp=1
# UI Audit Logs based on Filter by Level and Events
test_tc_001_AuditLogs_filtersbyinfologin=0
test_tc_001_AuditLogs_filtersbywarnlogin=0
test_tc_001_AuditLogs_filtersbydebuglogin=0
test_tc_001_AuditLogs_filtersbyerrorlogin=0
test_tc_001_AuditLogs_filtersbyinfologout=0
test_tc_001_AuditLogs_filtersbydebuglogout=0
test_tc_001_AuditLogs_filtersbywarnlogout=0
test_tc_001_AuditLogs_filtersbyerrorlogout=0
test_tc_001_AuditLogs_filtersbyinfoSimper=0
test_tc_001_AuditLogs_filtersbydebugSimper=0
test_tc_001_AuditLogs_filtersbyerrorSimper=0
test_tc_001_AuditLogs_filtersbywarnSimper=0
test_tc_001_AuditLogs_filtersbyinfoEimper=0
test_tc_001_AuditLogs_filtersbywarnEimper=0
test_tc_001_AuditLogs_filtersbyerrorEimper=0
test_tc_001_AuditLogs_filtersbydebugEimper=0
test_tc_001_AuditLogs_filtersbyinfopolicy=0
test_tc_001_AuditLogs_filtersbywarnpolicy=0
test_tc_001_AuditLogs_filtersbydebugpolicy=0
test_tc_001_AuditLogs_filtersbyerrorpolicy=0
test_tc_001_AuditLogs_filtersbyinfodevice=0
test_tc_001_AuditLogs_filtersbydebugdevice=0
test_tc_001_AuditLogs_filtersbywarndevice=0
test_tc_001_AuditLogs_filtersbyerrordevice=0
test_tc_001_AuditLogs_filtersbyinfogroup=0
test_tc_001_AuditLogs_filtersbywarngroup=0
test_tc_001_AuditLogs_filtersbydebuggroup=0
test_tc_001_AuditLogs_filtersbyerrorgroup=0
test_tc_001_AuditLogs_filtersbyinfoupload=0
test_tc_001_AuditLogs_filtersbywarnupload=0
test_tc_001_AuditLogs_filtersbydebugupload=0
test_tc_001_AuditLogs_filtersbyerrorupload=0
test_tc_001_AuditLogs_filtersbyinfocommand=0
test_tc_001_AuditLogs_filtersbywarncommand=0
test_tc_001_AuditLogs_filtersbydebugcommand=0
test_tc_001_AuditLogs_filtersbyerrorcommand=0
test_tc_001_AuditLogs_filtersbyinfobroadcast=0
test_tc_001_AuditLogs_filtersbywarnbroadcast=0
test_tc_001_AuditLogs_filtersbydebugbroadcast=0
test_tc_001_AuditLogs_filtersbyerrorbroadcast=0
test_tc_001_AuditLogs_filtersbyinfowetalk=0
test_tc_001_AuditLogs_filtersbywarnwetalk=0
test_tc_001_AuditLogs_filtersbydebugwetalk=0
test_tc_001_AuditLogs_filtersbyerrorwetalk=0
test_tc_001_AuditLogs_filtersbyinfoweboxpass=0
test_tc_001_AuditLogs_filtersbywarnweboxpass=0
test_tc_001_AuditLogs_filtersbydebugweboxpass=0
test_tc_001_AuditLogs_filtersbyerrorweboxpass=0
test_tc_001_AuditLogs_filtersbyinfokioskpass=0
test_tc_001_AuditLogs_filtersbywarnkioskpass=0
test_tc_001_AuditLogs_filtersbydebugkioskpass=0
test_tc_001_AuditLogs_filtersbyerrorkioskpass=0

# iOS Device logs based on Filter by Level and Events
test_tc_001_AuditLogs_filtersbyinfodevinfo=0
test_tc_001_AuditLogs_filtersbywarndevinfo=0
test_tc_001_AuditLogs_filtersbydebugdevinfo=0
test_tc_001_AuditLogs_filtersbyerrordevinfo=0
test_tc_001_AuditLogs_filtersbyinfoclrpass=0
test_tc_001_AuditLogs_filtersbywarnclrpass=0
test_tc_001_AuditLogs_filtersbydebugclrpass=0
test_tc_001_AuditLogs_filtersbyerrorclrpass=0
test_tc_001_AuditLogs_filtersbyinfodevlock=0
test_tc_001_AuditLogs_filtersbywarndevlock=0
test_tc_001_AuditLogs_filtersbydebugdevlock=0
test_tc_001_AuditLogs_filtersbyerrordevlock=0
test_tc_001_AuditLogs_filtersbyinfoinstallapp=0
test_tc_001_AuditLogs_filtersbywarninstallapp=0
test_tc_001_AuditLogs_filtersbydebuginstallapp=0
test_tc_001_AuditLogs_filtersbyerrorinstallapp=0
test_tc_001_AuditLogs_filtersbywarnremapp=0
test_tc_001_AuditLogs_filtersbyinforemapp=0
test_tc_001_AuditLogs_filtersbydebugremapp=0
test_tc_001_AuditLogs_filtersbyerrorremapp=0
test_tc_001_AuditLogs_filtersbyinfoinstallprof=0
test_tc_001_AuditLogs_filtersbywarninstallprof=0
test_tc_001_AuditLogs_filtersbydebuginstallprof=0
test_tc_001_AuditLogs_filtersbyerrorinstallprof=0
test_tc_001_AuditLogs_filtersbyinfoinstallpp=0
test_tc_001_AuditLogs_filtersbywarninstallpp=0
test_tc_001_AuditLogs_filtersbydebuginstallpp=0
test_tc_001_AuditLogs_filtersbyerrorinstallpp=0

# Date Range Alerts
test_tc_001_TodaysAlerts=1
test_tc_001_YesterdaysAlerts=1
test_tc_001_CustomDateRange=1

# Critical Alert that are that are not acknowledged by use after clicking on Alert notification icon
test_tc_001_CriticalAlerts=1

# Types and Level
test_tc_001_AlertsModule_Battery_Low=1
test_tc_001_AlertsModule_Battery_Warning=1
test_tc_001_AlertsModule_Battery_Critical=1
test_tc_001_AlertsModule_DATA_USAGE_Low=1
test_tc_001_AlertsModule_DATA_USAGE_Critical=1
test_tc_001_AlertsModule_DATA_USAGE_Warning=1
test_tc_001_AlertsModule_KIOSK_LOCKED_Regular=1
test_tc_001_AlertsModule_KIOSK_UNLOCKED_Critical=1
test_tc_001_AlertsModule_ADMIN_LOCKED_Critical=1
test_tc_001_AlertsModule_DEVICE_REBOOTED_Critical=1
test_tc_001_AlertsModule_DEVICE_WIPED_Critical=1
test_tc_001_AlertsModule_DEVICE_DELETED_Critical=1
test_tc_001_AlertsModule_ROOTED_ENROLL_Critical=1
test_tc_001_AlertsModule_MEMORY_ALERT_Low=1
test_tc_001_AlertsModule_MEMORY_ALERT_Critical=1
test_tc_001_AlertsModule_MEMORY_ALERT_Warning=1
test_tc_001_AlertsModule_DISC_USAGE_Low=1
test_tc_001_AlertsModule_DISC_USAGE_Critical=1
test_tc_001_AlertsModule_DISC_USAGE_Warning=1
test_tc_001_AlertsModule_DEVICE_FALLEN_Critical=1
test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_Critical=1
test_tc_001_AlertsModule_DEVICE_MARKED_LOST_Critical=1
test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_Critical=1
test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_Critical=1
test_tc_001_AlertsModule_Yesterday=1
test_tc_001_AlertsModule_Today=1
test_tc_001_AlertsModule_CustomDateRange=1

#Types are different and level is All
test_tc_001_AlertsModule_BATTERY_ALL=1
test_tc_001_AlertsModule_DATA_USAGE=1
test_tc_001_AlertsModule_KIOSK_LOCKED=1
test_tc_001_AlertsModule_KIOSK_UNLOCKED=1
test_tc_001_AlertsModule_ADMIN_LOCKED=1
test_tc_001_AlertsModule_DEVICE_REBOOTED=1
test_tc_001_AlertsModule_DEVICE_WIPED=1
test_tc_001_AlertsModule_DEVICE_DELETED=1
test_tc_001_AlertsModule_ROOTED_ENROLL=1
test_tc_001_AlertsModule_MEMORY_ALERT=1
test_tc_001_AlertsModule_DISC_USAGE=1
test_tc_001_AlertsModule_DEVICE_FALLEN=1
test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED=1
test_tc_001_AlertsModule_DEVICE_MARKED_LOST=1
test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN=1
test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK=1
test_tc_001_AlertsModule_SIM_ADDED_Critical=1
test_tc_001_AlertsModule_UNINSTALL_WEGUARD_Critical=1
test_tc_001_AlertsModule_SIM_CHANGED_Critical=1
test_tc_001_AlertsModule_SIM_REMOVED_Critical=1
test_tc_001_AlertsModule_RESET_PASSWORD_Critical=1
test_tc_001_AlertsModule_SIM_LOCK_CHANGED_Critical =1


def run_positive_tests():
    print( "Inside run_positive_tests" )
    global test_tc_000001_AccountAdmin_login
    test_tc_000001_AccountAdmin_login = 1

    global test_tc_000001_AccountAdmin_Logout
    test_tc_000001_AccountAdmin_Logout = 1

    global test_tc_000001_GET_Certificates
    test_tc_000001_GET_Certificates=1
    #WeBox Upload
    global test_tc_001_WeBox_SVGUpload
    test_tc_001_WeBox_SVGUpload = 1

    global test_tc_001_WeBox_MP3Upload
    test_tc_001_WeBox_MP3Upload = 1

    global test_tc_001_WeBox_MP4Upload
    test_tc_001_WeBox_MP4Upload = 1

    global test_tc_001_WeBox_OGGUpload
    test_tc_001_WeBox_OGGUpload = 1

    global test_tc_001_WeBox_TXTUpload
    test_tc_001_WeBox_TXTUpload = 1

    global test_tc_001_WeBox_DOCUpload
    test_tc_001_WeBox_DOCUpload = 1

    global test_tc_001_WeBox_DOCXUpload
    test_tc_001_WeBox_DOCXUpload = 1

    global test_tc_001_WeBox_XLSXUpload
    test_tc_001_WeBox_XLSXUpload = 1

    global test_tc_001_WeBox_WAVUpload
    test_tc_001_WeBox_WAVUpload = 1

    global test_tc_001_AlertsModule_CustomDateRange
    test_tc_001_AlertsModule_CustomDateRange = 1

    global test_tc_001_AlertsModule_Today
    test_tc_001_AlertsModule_Today = 1

    global test_tc_001_WeBox_APKUpload
    test_tc_001_WeBox_APKUpload = 1

    global test_tc_001_GLobalLevel_UploadCertificate
    test_tc_001_GLobalLevel_UploadCertificate=1

    global test_tc_001_WeBox_ZIPUpload
    test_tc_001_WeBox_ZIPUpload = 1

    global test_tc_001_WeBox_GIFUpload
    test_tc_001_WeBox_GIFUpload = 1

    global test_tc_001_WeBox_JPGUpload
    test_tc_001_WeBox_JPGUpload = 1

    global test_tc_001_WeBox_MOVUpload
    test_tc_001_WeBox_MOVUpload = 1

    global test_tc_001_WeBox_PNGUpload
    test_tc_001_WeBox_PNGUpload = 1

    global test_tc_001_WeBox_PDFUpload
    test_tc_001_WeBox_PDFUpload = 1

    global test_tc_001_WeBox_PPTXUpload
    test_tc_001_WeBox_PPTXUpload = 1

    global test_tc_001_WeBox_CSVpload
    test_tc_001_WeBox_CSVpload = 1

    global test_tc_001_Addingfoldersforservicetypes
    test_tc_001_Addingfoldersforservicetypes = 1

    global test_tc_001_DeletingfoldersforAmazonS3
    test_tc_001_DeletingfoldersforAmazonS3 = 1

    global test_tc_001_DeletingfoldersforGoogleDrive
    test_tc_001_DeletingfoldersforGoogleDrive = 1

    global test_tc_001_DeletingfoldersforDropbox
    test_tc_001_DeletingfoldersforDropbox = 1

    global test_tc_001_WeBox_DeviceUploads_pdf
    test_tc_001_WeBox_DeviceUploads_pdf=1

    global test_tc_001_WeBox_DeviceUploads_zip
    test_tc_001_WeBox_DeviceUploads_zip=1

    # UI Logs based on Filter by level as ALL
    global test_tc_001_AuditLogs_filtersbyallLogin
    test_tc_001_AuditLogs_filtersbyallLogin = 1

    global test_tc_001_AuditLogs_filtersbyalllogout
    test_tc_001_AuditLogs_filtersbyalllogout = 1

    global test_tc_001_AuditLogs_filtersbyallSimper
    test_tc_001_AuditLogs_filtersbyallSimper = 1

    global test_tc_001_AuditLogs_filtersbyallEimper
    test_tc_001_AuditLogs_filtersbyallEimper = 1

    global test_tc_001_AuditLogs_filtersbyallpolicy
    test_tc_001_AuditLogs_filtersbyallpolicy = 1

    global test_tc_001_AuditLogs_filtersbyalldevice
    test_tc_001_AuditLogs_filtersbyalldevice = 1

    global test_tc_001_AuditLogs_filtersbyallgroups
    test_tc_001_AuditLogs_filtersbyallgroups = 1

    global test_tc_001_AuditLogs_filtersbyallupload
    test_tc_001_AuditLogs_filtersbyallupload = 1

    global test_tc_001_AuditLogs_filtersbyallcommands
    test_tc_001_AuditLogs_filtersbyallcommands = 1

    global test_tc_001_AuditLogs_filtersbyallbroadcast
    test_tc_001_AuditLogs_filtersbyallbroadcast = 1

    global test_tc_001_AuditLogs_filtersbyallwetalk
    test_tc_001_AuditLogs_filtersbyallwetalk = 1

    global test_tc_001_AuditLogs_filtersbyallweboxpass
    test_tc_001_AuditLogs_filtersbyallweboxpass = 1

    global test_tc_001_AuditLogs_filtersbyallkioskpass
    test_tc_001_AuditLogs_filtersbyallkioskpass = 1
    # Search for Android and iOS device logs
    global test_tc_001_AuditLogs_searchAndroidimei
    test_tc_001_AuditLogs_searchAndroidimei = 1

    global test_tc_001_AuditLogs_searchiOSimei
    test_tc_001_AuditLogs_searchiOSimei = 1
    # Date range in Audit Logs
    global test_tc_001_AuditLogs_filtersbyAllyesterday
    test_tc_001_AuditLogs_filtersbyAllyesterday = 1
    # Android Device Logs
    global test_tc_001_AuditLogs_filterbyAll
    test_tc_001_AuditLogs_filterbyAll = 1

    global test_tc_001_AuditLogs_filtersbykiosklockunlock
    test_tc_001_AuditLogs_filtersbykiosklockunlock = 1

    global test_tc_001_AuditLogs_filtersbylicenseactivation
    test_tc_001_AuditLogs_filtersbylicenseactivation = 1

    global globaltest_tc_001_AuditLogs_filtersbyprovisioningprofile
    globaltest_tc_001_AuditLogs_filtersbyprovisioningprofile = 1

    global test_tc_001_AuditLogs_filtersbygetlicense
    test_tc_001_AuditLogs_filtersbygetlicense = 1

    global test_tc_001_AuditLogs_filtersbypollevents
    test_tc_001_AuditLogs_filtersbypollevents = 1

    global test_tc_001_AuditLogs_filtersbycrashevent
    test_tc_001_AuditLogs_filtersbycrashevent = 1

    global test_tc_001_AuditLogs_filtersbydatausage
    test_tc_001_AuditLogs_filtersbydatausage = 1

    global test_tc_001_AuditLogs_filtersbywipeevent
    test_tc_001_AuditLogs_filtersbywipeevent = 1

    global test_tc_001_AuditLogs_filtersbypusheevents
    test_tc_001_AuditLogs_filtersbypusheevents = 1

    global test_tc_001_AuditLogs_filtersbyWeGuardappevent
    test_tc_001_AuditLogs_filtersbyWeGuardappevent = 1

    global test_tc_001_AuditLogs_filtersbyotherevent
    test_tc_001_AuditLogs_filtersbyotherevent = 1
    # iOS Device Logs
    global test_tc_001_AuditLogs_filtersbyalldevinfo
    test_tc_001_AuditLogs_filtersbyalldevinfo = 1

    global test_tc_001_AuditLogs_filtersbyallclrpass
    test_tc_001_AuditLogs_filtersbyallclrpass = 1

    global test_tc_001_AuditLogs_filtersbyalldevlock
    test_tc_001_AuditLogs_filtersbyalldevlock = 1

    global test_tc_001_AuditLogs_filtersbyallinstallapp
    test_tc_001_AuditLogs_filtersbyallinstallapp = 1

    global test_tc_001_AuditLogs_filtersbyallremapp
    test_tc_001_AuditLogs_filtersbyallremapp = 1

    global test_tc_001_AuditLogs_filtersbyallinstallprof
    test_tc_001_AuditLogs_filtersbyallinstallprof = 1

    global test_tc_001_AuditLogs_filtersbyallinstallpp
    test_tc_001_AuditLogs_filtersbyallinstallpp = 1

    global test_tc_001_AlertsModule_Battery_Low
    test_tc_001_AlertsModule_Battery_Low = 1

    global test_tc_001_AlertsModule_Battery_Warning
    test_tc_001_AlertsModule_Battery_Warning = 1

    global test_tc_001_AlertsModule_Battery_Critical
    test_tc_001_AlertsModule_Battery_Critical = 1

    global test_tc_001_AlertsModule_DATA_USAGE_Low
    test_tc_001_AlertsModule_DATA_USAGE_Low = 1

    global test_tc_001_AlertsModule_DATA_USAGE_Critical
    test_tc_001_AlertsModule_DATA_USAGE_Critical = 1

    global test_tc_001_AlertsModule_DATA_USAGE_Warning
    test_tc_001_AlertsModule_DATA_USAGE_Warning = 1

    global test_tc_001_AlertsModule_KIOSK_LOCKED_ALL
    test_tc_001_AlertsModule_KIOSK_LOCKED_ALL = 1

    global test_tc_001_AlertsModule_KIOSK_UNLOCKED_Critical
    test_tc_001_AlertsModule_KIOSK_UNLOCKED_Critical = 1

    global test_tc_001_AlertsModule_ADMIN_LOCKED_Critical
    test_tc_001_AlertsModule_ADMIN_LOCKED_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_REBOOTED_Critical
    test_tc_001_AlertsModule_DEVICE_REBOOTED_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_WIPED_Critical
    test_tc_001_AlertsModule_DEVICE_WIPED_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_DELETED_Critical
    test_tc_001_AlertsModule_DEVICE_DELETED_Critical = 1

    global test_tc_001_AlertsModule_ROOTED_ENROLL_Critical
    test_tc_001_AlertsModule_ROOTED_ENROLL_Critical = 1

    global test_tc_001_AlertsModule_MEMORY_ALERT_Low
    test_tc_001_AlertsModule_MEMORY_ALERT_Low = 1

    global test_tc_001_AlertsModule_MEMORY_ALERT_Critical
    test_tc_001_AlertsModule_MEMORY_ALERT_Critical = 1

    global test_tc_001_AlertsModule_MEMORY_ALERT_Warning
    test_tc_001_AlertsModule_MEMORY_ALERT_Warning = 1

    global test_tc_001_AlertsModule_DISC_USAGE_Low
    test_tc_001_AlertsModule_DISC_USAGE_Low = 1

    global test_tc_001_AlertsModule_DISC_USAGE_Critical
    test_tc_001_AlertsModule_DISC_USAGE_Critical = 1

    global test_tc_001_AlertsModule_DISC_USAGE_Warning
    test_tc_001_AlertsModule_DISC_USAGE_Warning = 1

    global test_tc_001_AlertsModule_DEVICE_FALLEN_Critical
    test_tc_001_AlertsModule_DEVICE_FALLEN_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_Critical
    test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_MARKED_LOST_Critical
    test_tc_001_AlertsModule_DEVICE_MARKED_LOST_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_Critical
    test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN_Critical = 1

    global test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_Critical
    test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK_Critical = 1

    global test_tc_001_AlertsModule_BATTERY_ALL
    test_tc_001_AlertsModule_BATTERY_ALL = 1

    global test_tc_001_AlertsModule_DATA_USAGE
    test_tc_001_AlertsModule_DATA_USAGE = 1

    global test_tc_001_AlertsModule_KIOSK_LOCKED
    test_tc_001_AlertsModule_KIOSK_LOCKED = 1

    global test_tc_001_AlertsModule_KIOSK_UNLOCKED
    test_tc_001_AlertsModule_KIOSK_UNLOCKED = 1

    global test_tc_001_AlertsModule_ADMIN_LOCKED
    test_tc_001_AlertsModule_ADMIN_LOCKED = 1

    global test_tc_001_AlertsModule_DEVICE_REBOOTED
    test_tc_001_AlertsModule_DEVICE_REBOOTED = 1

    global test_tc_001_AlertsModule_DEVICE_WIPED
    test_tc_001_AlertsModule_DEVICE_WIPED = 1

    global test_tc_001_AlertsModule_DEVICE_DELETED
    test_tc_001_AlertsModule_DEVICE_DELETED = 1

    global test_tc_001_AlertsModule_ROOTED_ENROLL
    test_tc_001_AlertsModule_ROOTED_ENROLL = 1

    global test_tc_001_AlertsModule_MEMORY_ALERT
    test_tc_001_AlertsModule_MEMORY_ALERT = 1

    global test_tc_001_AlertsModule_Yesterday
    test_tc_001_AlertsModule_Yesterday = 1

    global test_tc_001_AlertsModule_DISC_USAGE
    test_tc_001_AlertsModule_DISC_USAGE = 1

    global test_tc_001_AlertsModule_DEVICE_FALLEN
    test_tc_001_AlertsModule_DEVICE_FALLEN = 1

    global test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED
    test_tc_001_AlertsModule_DEVICE_MARKED_REPLACED = 1

    global test_tc_001_AlertsModule_DEVICE_MARKED_LOST
    test_tc_001_AlertsModule_DEVICE_MARKED_LOST = 1

    global test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN
    test_tc_001_AlertsModule_DEVICE_MARKED_STOLEN = 1

    global test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK
    test_tc_001_AlertsModule_DEVICE_CONNECTED_BACK = 1

    global test_tc_001_AlertsModule_SIM_ADDED_Critical
    test_tc_001_AlertsModule_SIM_ADDED_Critical = 1

    global test_tc_001_AlertsModule_UNINSTALL_WEGUARD_Critical
    test_tc_001_AlertsModule_UNINSTALL_WEGUARD_Critical = 1

    global test_tc_001_AlertsModule_SIM_CHANGED_Critical
    test_tc_001_AlertsModule_SIM_CHANGED_Critical = 1

    global test_tc_001_AlertsModule_SIM_REMOVED_Critical
    test_tc_001_AlertsModule_SIM_REMOVED_Critical=1

    global test_tc_001_AlertsModule_RESET_PASSWORD_Critical
    test_tc_001_AlertsModule_RESET_PASSWORD_Critical=1

    global test_tc_001_AlertsModule_SIM_LOCK_CHANGED_Critical
    test_tc_001_AlertsModule_SIM_LOCK_CHANGED_Critical=1

    global test_tc_001_DeviceUploads_SharedFolders_config
    test_tc_001_DeviceUploads_SharedFolders_config=1




def run_negative_tests():
    print( "Inside run_negative_tests" )
    global test_tc_000001_admin_Invalid_Credentials
    test_tc_000001_admin_Invalid_Credentials = 1

    global test_tc_000001_admin_Invalid_Email
    test_tc_000001_admin_Invalid_Email = 1

    global test_tc_000001_admin_Invalid_Password
    test_tc_000001_admin_Invalid_Password = 1

    global test_tc_000001_admin_Credentials_With_Spaces
    test_tc_000001_admin_Credentials_With_Spaces = 1

    global test_tc_000001_admin_WithOut_Password
    test_tc_000001_admin_WithOut_Password = 1

    global test_tc_000001_admin_WithOut_UserName
    test_tc_000001_admin_WithOut_UserName = 1

    global test_tc_000001_admin_WithOut_UserName_Password
    test_tc_000001_admin_WithOut_UserName_Password = 1

    #WeBox Upload
    global test_tc_001_WeBox_OGGUpload
    test_tc_001_WeBox_OGGUpload = 1

    global test_tc_001_WeBox_APKUpload
    test_tc_001_WeBox_APKUpload = 1

    global test_tc_001_WeBox_MOVUpload
    test_tc_001_WeBox_MOVUpload = 1

    global test_tc_001_WeBox_MPEGUpload
    test_tc_001_WeBox_MPEGUpload = 1

    global test_tc_001_WeBox_WEBMUpload
    test_tc_001_WeBox_WEBMUpload = 1

    global test_tc_001_WeBox_undosave
    test_tc_001_WeBox_undosave = 1
    # UI Audit Logs based on Filter by Level and Events
    global test_tc_001_AuditLogs_filtersbyinfologin
    test_tc_001_AuditLogs_filtersbyinfologin = 1

    global test_tc_001_AuditLogs_filtersbywarnlogin
    test_tc_001_AuditLogs_filtersbywarnlogin = 1

    global test_tc_001_AuditLogs_filtersbydebuglogin
    test_tc_001_AuditLogs_filtersbydebuglogin = 1

    global test_tc_001_AuditLogs_filtersbyerrorlogin
    test_tc_001_AuditLogs_filtersbyerrorlogin = 1

    global test_tc_001_AuditLogs_filtersbyinfologout
    test_tc_001_AuditLogs_filtersbyinfologout = 1
    global test_tc_001_AuditLogs_filtersbydebuglogout
    test_tc_001_AuditLogs_filtersbydebuglogout = 1

    global test_tc_001_AuditLogs_filtersbywarnlogout
    test_tc_001_AuditLogs_filtersbywarnlogout = 1

    global test_tc_001_AuditLogs_filtersbyerrorlogout
    test_tc_001_AuditLogs_filtersbyerrorlogout = 1

    global test_tc_001_AuditLogs_filtersbyinfoSimper
    test_tc_001_AuditLogs_filtersbyinfoSimper = 1

    global test_tc_001_AuditLogs_filtersbydebugSimper
    test_tc_001_AuditLogs_filtersbydebugSimper = 1

    global test_tc_001_AuditLogs_filtersbyerrorSimper
    test_tc_001_AuditLogs_filtersbyerrorSimper = 1

    global test_tc_001_AuditLogs_filtersbywarnSimper
    test_tc_001_AuditLogs_filtersbywarnSimper = 1

    global test_tc_001_AuditLogs_filtersbyinfoEimper
    test_tc_001_AuditLogs_filtersbyinfoEimper = 1

    global test_tc_001_AuditLogs_filtersbywarnEimper
    test_tc_001_AuditLogs_filtersbywarnEimper = 1

    global test_tc_001_AuditLogs_filtersbyerrorEimper
    test_tc_001_AuditLogs_filtersbyerrorEimper = 1

    global test_tc_001_AuditLogs_filtersbydebugEimper
    test_tc_001_AuditLogs_filtersbydebugEimper = 1

    global test_tc_001_AuditLogs_filtersbyinfopolicy
    test_tc_001_AuditLogs_filtersbyinfopolicy = 1

    global test_tc_001_AuditLogs_filtersbywarnpolicy
    test_tc_001_AuditLogs_filtersbywarnpolicy = 1

    global test_tc_001_AuditLogs_filtersbydebugpolicy
    test_tc_001_AuditLogs_filtersbydebugpolicy = 1

    global test_tc_001_AuditLogs_filtersbyerrorpolicy
    test_tc_001_AuditLogs_filtersbyerrorpolicy = 1

    global test_tc_001_AuditLogs_filtersbyinfodevice
    test_tc_001_AuditLogs_filtersbyinfodevice = 1

    global test_tc_001_AuditLogs_filtersbydebugdevice
    test_tc_001_AuditLogs_filtersbydebugdevice = 1

    global test_tc_001_AuditLogs_filtersbywarndevice
    test_tc_001_AuditLogs_filtersbywarndevice = 1

    global test_tc_001_AuditLogs_filtersbyerrordevice
    test_tc_001_AuditLogs_filtersbyerrordevice = 1

    global test_tc_001_AuditLogs_filtersbyinfogroup
    test_tc_001_AuditLogs_filtersbyinfogroup = 1

    global test_tc_001_AuditLogs_filtersbywarngroup
    test_tc_001_AuditLogs_filtersbywarngroup = 1

    global test_tc_001_AuditLogs_filtersbydebuggroup
    test_tc_001_AuditLogs_filtersbydebuggroup = 1

    global test_tc_001_AuditLogs_filtersbyerrorgroup
    test_tc_001_AuditLogs_filtersbyerrorgroup = 1

    global test_tc_001_AuditLogs_filtersbyinfoupload
    test_tc_001_AuditLogs_filtersbyinfoupload = 1

    global test_tc_001_AuditLogs_filtersbywarnupload
    test_tc_001_AuditLogs_filtersbywarnupload = 1

    global test_tc_001_AuditLogs_filtersbydebugupload
    test_tc_001_AuditLogs_filtersbydebugupload = 1

    global test_tc_001_AuditLogs_filtersbyerrorupload
    test_tc_001_AuditLogs_filtersbyerrorupload = 1

    global test_tc_001_AuditLogs_filtersbyinfocommand
    test_tc_001_AuditLogs_filtersbyinfocommand = 1

    global test_tc_001_AuditLogs_filtersbywarncommand
    test_tc_001_AuditLogs_filtersbywarncommand = 1

    global test_tc_001_AuditLogs_filtersbydebugcommand
    test_tc_001_AuditLogs_filtersbydebugcommand = 1

    global test_tc_001_AuditLogs_filtersbyerrorcommand
    test_tc_001_AuditLogs_filtersbyerrorcommand = 1

    global test_tc_001_AuditLogs_filtersbyinfobroadcast
    test_tc_001_AuditLogs_filtersbyinfobroadcast = 1

    global test_tc_001_AuditLogs_filtersbywarnbroadcast
    test_tc_001_AuditLogs_filtersbywarnbroadcast = 1

    global test_tc_001_AuditLogs_filtersbydebugbroadcast
    test_tc_001_AuditLogs_filtersbydebugbroadcast = 1

    global test_tc_001_AuditLogs_filtersbyerrorbroadcast
    test_tc_001_AuditLogs_filtersbyerrorbroadcast = 1

    global test_tc_001_AuditLogs_filtersbyinfowetalk
    test_tc_001_AuditLogs_filtersbyinfowetalk = 1

    global test_tc_001_AuditLogs_filtersbywarnwetalk
    test_tc_001_AuditLogs_filtersbywarnwetalk = 1

    global test_tc_001_AuditLogs_filtersbydebugwetalk
    test_tc_001_AuditLogs_filtersbydebugwetalk = 1

    global test_tc_001_AuditLogs_filtersbyerrorwetalk
    test_tc_001_AuditLogs_filtersbyerrorwetalk = 1

    global test_tc_001_AuditLogs_filtersbyinfoweboxpass
    test_tc_001_AuditLogs_filtersbyinfoweboxpass = 1

    global test_tc_001_AuditLogs_filtersbywarnweboxpass
    test_tc_001_AuditLogs_filtersbywarnweboxpass = 1

    global test_tc_001_AuditLogs_filtersbydebugweboxpass
    test_tc_001_AuditLogs_filtersbydebugweboxpass = 1

    global test_tc_001_AuditLogs_filtersbyerrorweboxpass
    test_tc_001_AuditLogs_filtersbyerrorweboxpass = 1

    global test_tc_001_AuditLogs_filtersbyinfokioskpass
    test_tc_001_AuditLogs_filtersbyinfokioskpass = 1

    global test_tc_001_AuditLogs_filtersbywarnkioskpass
    test_tc_001_AuditLogs_filtersbywarnkioskpass = 1

    global test_tc_001_AuditLogs_filtersbydebugkioskpass
    test_tc_001_AuditLogs_filtersbydebugkioskpass = 1

    global test_tc_001_AuditLogs_filtersbyerrorkioskpass
    test_tc_001_AuditLogs_filtersbyerrorkioskpass = 1

    # iOS Device logs based on Filter by Level and Events
    global test_tc_001_AuditLogs_filtersbyinfodevinfo
    test_tc_001_AuditLogs_filtersbyinfodevinfo = 1

    global test_tc_001_AuditLogs_filtersbywarndevinfo
    test_tc_001_AuditLogs_filtersbywarndevinfo = 1

    global test_tc_001_AuditLogs_filtersbydebugdevinfo
    test_tc_001_AuditLogs_filtersbydebugdevinfo = 1

    global test_tc_001_AuditLogs_filtersbyerrordevinfo
    test_tc_001_AuditLogs_filtersbyerrordevinfo = 1

    global test_tc_001_AuditLogs_filtersbyinfoclrpass
    test_tc_001_AuditLogs_filtersbyinfoclrpass = 1

    global test_tc_001_AuditLogs_filtersbywarnclrpass
    test_tc_001_AuditLogs_filtersbywarnclrpass = 1

    global test_tc_001_AuditLogs_filtersbydebugclrpass
    test_tc_001_AuditLogs_filtersbydebugclrpass = 1

    global test_tc_001_AuditLogs_filtersbyerrorclrpass
    test_tc_001_AuditLogs_filtersbyerrorclrpass = 1

    global test_tc_001_AuditLogs_filtersbyinfodevlock
    test_tc_001_AuditLogs_filtersbyinfodevlock = 1

    global test_tc_001_AuditLogs_filtersbywarndevlock
    test_tc_001_AuditLogs_filtersbywarndevlock = 1

    global test_tc_001_AuditLogs_filtersbydebugdevlock
    test_tc_001_AuditLogs_filtersbydebugdevlock = 1

    global test_tc_001_AuditLogs_filtersbyerrordevlock
    test_tc_001_AuditLogs_filtersbyerrordevlock = 1

    global test_tc_001_AuditLogs_filtersbyinfoinstallapp
    test_tc_001_AuditLogs_filtersbyinfoinstallapp = 1

    global test_tc_001_AuditLogs_filtersbywarninstallapp
    test_tc_001_AuditLogs_filtersbywarninstallapp = 1

    global test_tc_001_AuditLogs_filtersbydebuginstallapp
    test_tc_001_AuditLogs_filtersbydebuginstallapp = 1

    global test_tc_001_AuditLogs_filtersbyerrorinstallapp
    test_tc_001_AuditLogs_filtersbyerrorinstallapp = 1

    global test_tc_001_AuditLogs_filtersbywarnremapp
    test_tc_001_AuditLogs_filtersbywarnremapp = 1

    global test_tc_001_AuditLogs_filtersbyinforemapp
    test_tc_001_AuditLogs_filtersbyinforemapp = 1

    global test_tc_001_AuditLogs_filtersbydebugremapp
    test_tc_001_AuditLogs_filtersbydebugremapp = 1

    global test_tc_001_AuditLogs_filtersbyerrorremapp
    test_tc_001_AuditLogs_filtersbyerrorremapp = 1

    global test_tc_001_AuditLogs_filtersbyinfoinstallprof
    test_tc_001_AuditLogs_filtersbyinfoinstallprof = 1

    global test_tc_001_AuditLogs_filtersbywarninstallprof
    test_tc_001_AuditLogs_filtersbywarninstallprof = 1

    global test_tc_001_AuditLogs_filtersbydebuginstallprof
    test_tc_001_AuditLogs_filtersbydebuginstallprof = 1

    global test_tc_001_AuditLogs_filtersbyerrorinstallprof
    test_tc_001_AuditLogs_filtersbyerrorinstallprof = 1

    global test_tc_001_AuditLogs_filtersbyinfoinstallpp
    test_tc_001_AuditLogs_filtersbyinfoinstallpp = 1

    global test_tc_001_AuditLogs_filtersbywarninstallpp
    test_tc_001_AuditLogs_filtersbywarninstallpp = 1

    global test_tc_001_AuditLogs_filtersbydebuginstallpp
    test_tc_001_AuditLogs_filtersbydebuginstallpp = 1

    global test_tc_001_AuditLogs_filtersbyerrorinstallpp
    test_tc_001_AuditLogs_filtersbyerrorinstallpp = 1
    # Filters by level
    global test_tc_001_AuditLogs_filtersbyALL
    test_tc_001_AuditLogs_filtersbyALL = 1

    global test_tc_001_AuditLogs_filtersbydebugALL
    test_tc_001_AuditLogs_filtersbydebugALL = 1

    global test_tc_001_AuditLogs_filtersbywarnALL
    test_tc_001_AuditLogs_filtersbywarnALL = 1

    global test_tc_001_AuditLogs_filtersbyerrorALL
    test_tc_001_AuditLogs_filtersbyerrorALL = 1

    global test_tc_001_AuditLogs_filtersbyinfoALL
    test_tc_001_AuditLogs_filtersbyinfoALL = 1


if positive_tests == 1:
    run_positive_tests()

if negative_tests == 1:
   run_negative_tests()














