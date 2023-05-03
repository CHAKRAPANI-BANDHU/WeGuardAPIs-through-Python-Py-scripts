run_resetpswdcases = 1
run_broadcastcases = 1
run_wetalkcases = 1
run_devicedetailscases = 1
run_positivetest = 1
run_negativetest = 1

run_test_tc_00001_actpact = 0
run_test_tc_00001_wetalkcallhistory =0
test_tc_00001_broadcast_messagehistory_withreqID = 0
run_test_tc_00001_wetalk_videocallconfig = 0
run_test_tc_00001_wetalk_events = 0
run_test_tc_00001_bc_uploadimage =0
run_test_tc_00002_wetalk_events = 0
run_test_tc_00003_wetalk_events = 0
run_test_tc_00001_wetalk_fcm_update = 0
run_test_tc_00001_searchdevices_inwetalkpage =0
run_test_tc_00002_wetalk_fcm_update = 0
run_test_tc_00003_wetalk_fcm_update = 0
run_test_tc_00001_searchdeviceid = 0
run_test_tc_00001_bc_fcm_update = 0
run_test_tc_00002_bc_fcm_update = 0
run_test_tc_00003_bc_fcm_update = 0
run_test_tc_00001_broadcast_messagehistory_fordevice = 0
run_test_tc_00001_broadcast_messagehistory = 0
run_test_tc_00001_bc_events = 0
run_test_tc_00002_bc_events = 0
run_test_tc_00003_bc_events = 0
run_test_tc_00001_bc_img_upload = 0
run_test_tc_00001_apps = 0
run_test_tc_00002_apps = 0
run_test_tc_00001_firebase_auth = 0
run_test_tc_00001_authtoken = 0
run_test_tc_00001_updatedevice = 0
run_test_tc_00001_webrtc_stream = 0
run_test_tc_00001_notes = 0
run_test_tc_00001_bc_searchdeviceid = 0
run_test_tc_00001_auth = 0
run_test_tc_00001_screensharehistory = 0
run_test_tc_00001_fcm_remote_view = 0
run_test_tc_00001_fcm_force_stop_app = 0
run_test_tc_00001_fcm_device_wakeup = 0
run_test_tc_00001_fcm_update = 0
run_test_tc_00001_Kiosk_unlock_events = 0
run_test_tc_00001_fcm_Kiosk_unlock = 0
run_test_tc_00001_fcm_Kiosk_lock = 0
run_test_tc_00001_Kiosk_lock_events = 0
run_test_tc_00001_fcm_admin_lock = 0
run_test_tc_00001_admin_lock_events = 0
run_test_tc_00001_fcm_admin_unlock = 0
run_test_tc_00001_admin_unlock_events = 0
run_test_tc_00001_fcm_device_wipe = 0
run_test_tc_00001_fcm_device_reboot = 0
run_test_tc_00001_fcm_device_poweroff = 0
run_test_tc_00001_fcm_device_lock = 0
run_test_tc_00002_screensharehistory = 0
run_test_tc_00003_screensharehistory = 0
run_test_tc_00002_notes = 0
run_resetpswdEmailOTP = 0
run_test_tc_00001_resetpswd_verifyOTP_valid = 0
run_test_tc_00002_resetpswd_verifyOTP_invalid = 0
run_test_tc_00003_resetpswd_verifyOTP_emptyOTP = 0
run_test_tc_00004_resetpswd_verifyOTP_sameoldpassword = 0
run_test_tc_00005_resetpswd_verifyOTP_newpassword = 0
run_test_tc_00006_resetpswd_verifyOTP_emptypassword = 0
run_test_tc_00004_wetalk_complete_events = 0
run_test_tc_00001_login = 0
run_test_tc_00001_getdevice = 0
run_test_tc_00001_wetalkcall_authtoken = 0
run_test_tc_00001_wetalkcall_fcm = 0
run_test_tc_00002_wetalkcall_authtoken = 0
run_test_tc_00001_wetalkcall_event = 0
run_test_tc_00002_wetalkcall_event = 0
run_test_tc_00002_wetalkcallhistory = 0

def test_positivetest():
    global run_test_tc_00001_login
    run_test_tc_00001_login = 1
    global run_test_tc_00001_actpact
    run_test_tc_00001_actpact = 1
    global run_test_tc_00001_wetalkcall_authtoken
    run_test_tc_00001_wetalkcall_authtoken = 1
    global run_test_tc_00002_wetalkcall_authtoken
    run_test_tc_00002_wetalkcall_authtoken = 1
    global run_test_tc_00001_wetalkcall_event
    run_test_tc_00001_wetalkcall_event = 1
    global run_test_tc_00002_wetalkcall_event
    run_test_tc_00002_wetalkcall_event = 1
    global run_test_tc_00001_getdevice
    run_test_tc_00001_getdevice = 1
    global run_test_tc_00001_wetalkcall_fcm
    run_test_tc_00001_wetalkcall_fcm = 1
    global run_resetpswdEmailOTP
    run_resetpswdEmailOTP = 1
    global run_test_tc_00001_resetpswd_verifyOTP_valid
    run_test_tc_00001_resetpswd_verifyOTP_valid = 1
    global run_test_tc_00004_resetpswd_verifyOTP_sameoldpassword
    run_test_tc_00004_resetpswd_verifyOTP_sameoldpassword = 1
    global run_test_tc_00005_resetpswd_verifyOTP_newpassword
    run_test_tc_00005_resetpswd_verifyOTP_newpassword = 1
    # broadcast fcm update
    global run_test_tc_00001_bc_fcm_update
    run_test_tc_00001_bc_fcm_update = 1
    global run_test_tc_00002_bc_fcm_update
    run_test_tc_00002_bc_fcm_update = 1
    global run_test_tc_00003_bc_fcm_update
    run_test_tc_00003_bc_fcm_update = 1
    # broadcast Search imei
    global run_test_tc_00001_bc_searchdeviceid
    run_test_tc_00001_bc_searchdeviceid = 1
    # broadcast events
    global run_test_tc_00001_bc_events
    run_test_tc_00001_bc_events = 1
    global run_test_tc_00002_bc_events
    run_test_tc_00002_bc_events = 1
    global run_test_tc_00003_bc_events
    run_test_tc_00003_bc_events = 1
    global run_test_tc_00001_bc_uploadimage
    run_test_tc_00001_bc_uploadimage = 1

    # wetalk searchimei
    global run_test_tc_00001_searchdeviceid
    run_test_tc_00001_searchdeviceid = 1
    global run_test_tc_00001_broadcast_messagehistory
    run_test_tc_00001_broadcast_messagehistory = 1
    global run_test_tc_00001_broadcast_messagehistory_fordevice
    run_test_tc_00001_broadcast_messagehistory_fordevice = 1
    global run_test_tc_00003_screensharehistory
    run_test_tc_00003_screensharehistory = 1
    global test_tc_00001_broadcast_messagehistory_withreqID
    test_tc_00001_broadcast_messagehistory_withreqID = 1
    # wetalk events
    global run_test_tc_00001_wetalk_events
    run_test_tc_00001_wetalk_events = 1
    global run_test_tc_00002_wetalk_events
    run_test_tc_00002_wetalk_events = 1
    global run_test_tc_00003_wetalk_events
    run_test_tc_00003_wetalk_events = 1
    global run_test_tc_00004_wetalk_complete_events
    run_test_tc_00004_wetalk_complete_events = 1
    # wetalk fcm update
    global run_test_tc_00001_wetalk_fcm_update
    run_test_tc_00001_wetalk_fcm_update = 1
    global run_test_tc_00002_wetalk_fcm_update
    run_test_tc_00002_wetalk_fcm_update = 1
    global run_test_tc_00003_wetalk_fcm_update
    run_test_tc_00003_wetalk_fcm_update = 1
    global run_test_tc_00001_searchdevices_inwetalkpage
    run_test_tc_00001_searchdevices_inwetalkpage = 1
    global run_test_tc_00001_wetalk_videocallconfig
    run_test_tc_00001_wetalk_videocallconfig = 1
    # Wetalk call history
    global run_test_tc_00001_wetalkcallhistory
    run_test_tc_00001_wetalkcallhistory = 1
    # Device commands
    global run_test_tc_00001_fcm_device_wakeup
    run_test_tc_00001_fcm_device_wakeup = 1
    global run_test_tc_00001_admin_unlock_events
    run_test_tc_00001_admin_unlock_events = 1
    global run_test_tc_00001_fcm_admin_unlock
    run_test_tc_00001_fcm_admin_unlock = 1
    global run_test_tc_00001_fcm_Kiosk_unlock
    run_test_tc_00001_fcm_Kiosk_unlock = 1
    global run_test_tc_00001_Kiosk_lock_events
    run_test_tc_00001_Kiosk_lock_events = 1
    global run_test_tc_00001_admin_lock_events
    run_test_tc_00001_admin_lock_events = 1
    global run_test_tc_00001_fcm_admin_lock
    run_test_tc_00001_fcm_admin_lock = 1
    global run_test_tc_00001_fcm_Kiosk_lock
    run_test_tc_00001_fcm_Kiosk_lock = 1
    global run_test_tc_00001_fcm_device_wipe
    run_test_tc_00001_fcm_device_wipe = 0
    global run_test_tc_00001_fcm_device_poweroff
    run_test_tc_00001_fcm_device_poweroff = 0
    global run_test_tc_00001_fcm_device_reboot
    run_test_tc_00001_fcm_device_reboot = 0
    global run_test_tc_00001_Kiosk_unlock_events
    run_test_tc_00001_Kiosk_unlock_events = 1
    global run_test_tc_00001_fcm_update
    run_test_tc_00001_fcm_update = 1
    global run_test_tc_00001_fcm_force_stop_app
    run_test_tc_00001_fcm_force_stop_app = 1
    global run_test_tc_00001_fcm_remote_view
    run_test_tc_00001_fcm_remote_view = 1
    global run_test_tc_00001_fcm_device_lock
    run_test_tc_00001_fcm_device_lock = 1
    global run_test_tc_00001_apps
    run_test_tc_00001_apps = 1
    global run_test_tc_00001_auth
    run_test_tc_00001_auth = 1
    global run_test_tc_00001_notes
    run_test_tc_00001_notes = 1
    global run_test_tc_00002_notes
    run_test_tc_00002_notes = 1
    global run_test_tc_00001_screensharehistory
    run_test_tc_00001_screensharehistory = 1
    global run_test_tc_00001_webrtc_stream
    run_test_tc_00001_webrtc_stream = 1
    global run_test_tc_00001_updatedevice
    run_test_tc_00001_updatedevice = 1
    global run_test_tc_00002_screensharehistory
    run_test_tc_00002_screensharehistory = 1


def test_reset_password():
    global run_resetpswdEmailOTP
    run_resetpswdEmailOTP = 1
    global run_test_tc_00001_resetpswd_verifyOTP_valid
    run_test_tc_00001_resetpswd_verifyOTP_valid = 1
    global run_test_tc_00002_resetpswd_verifyOTP_invalid
    run_test_tc_00002_resetpswd_verifyOTP_invalid = 1
    global run_test_tc_00003_resetpswd_verifyOTP_emptyOTP
    run_test_tc_00003_resetpswd_verifyOTP_emptyOTP = 1
    global run_test_tc_00004_resetpswd_verifyOTP_sameoldpassword
    run_test_tc_00004_resetpswd_verifyOTP_sameoldpassword = 1
    global run_test_tc_00005_resetpswd_verifyOTP_newpassword
    run_test_tc_00005_resetpswd_verifyOTP_newpassword = 1
    global run_test_tc_00006_resetpswd_verifyOTP_emptypassword
    run_test_tc_00006_resetpswd_verifyOTP_emptypassword = 1

if run_resetpswdcases == 1:
    test_reset_password()

def test_broadcast():
    # broadcast fcm update
    global run_test_tc_00001_bc_fcm_update
    run_test_tc_00001_bc_fcm_update = 1
    global run_test_tc_00002_bc_fcm_update
    run_test_tc_00002_bc_fcm_update = 1
    global run_test_tc_00003_bc_fcm_update
    run_test_tc_00003_bc_fcm_update = 1
    # broadcast Search imei
    global run_test_tc_00001_bc_searchdeviceid
    run_test_tc_00001_bc_searchdeviceid = 1
    # broadcast events
    global run_test_tc_00001_bc_events
    run_test_tc_00001_bc_events = 1
    global run_test_tc_00002_bc_events
    run_test_tc_00002_bc_events = 1
    global run_test_tc_00003_bc_events
    run_test_tc_00003_bc_events = 1
    global run_test_tc_00001_bc_img_upload
    run_test_tc_00001_bc_img_upload = 1
if run_broadcastcases == 1:
    test_broadcast()

def test_wetalk():
    # wetalk searchimei
    global run_test_tc_00001_searchdeviceid
    run_test_tc_00001_searchdeviceid = 1
    global run_test_tc_00001_broadcast_messagehistory
    run_test_tc_00001_broadcast_messagehistory = 1
    global run_test_tc_00001_broadcast_messagehistory_fordevice
    run_test_tc_00001_broadcast_messagehistory_fordevice = 1
    global run_test_tc_00003_screensharehistory
    run_test_tc_00003_screensharehistory = 1
    # wetalk events
    global run_test_tc_00001_wetalk_events
    run_test_tc_00001_wetalk_events = 1
    global run_test_tc_00002_wetalk_events
    run_test_tc_00002_wetalk_events = 1
    global run_test_tc_00003_wetalk_events
    run_test_tc_00003_wetalk_events = 1
    global run_test_tc_00004_wetalk_complete_events
    run_test_tc_00004_wetalk_complete_events = 1
    # wetalk fcm update
    global run_test_tc_00001_wetalk_fcm_update
    run_test_tc_00001_wetalk_fcm_update = 1
    global run_test_tc_00002_wetalk_fcm_update
    run_test_tc_00002_wetalk_fcm_update = 1
    global run_test_tc_00003_wetalk_fcm_update
    run_test_tc_00003_wetalk_fcm_update = 1
    global run_test_tc_00002_wetalkcallhistory
    run_test_tc_00002_wetalkcallhistory = 1
    global run_test_tc_00003_wetalkcallhistory
    run_test_tc_00003_wetalkcallhistory = 1
    global run_test_tc_00004_wetalkcallhistory
    run_test_tc_00004_wetalkcallhistory = 1
if run_wetalkcases == 1:
    test_wetalk()

def test_device_details_page():
    # Device commands
    global run_test_tc_00001_fcm_device_wakeup
    run_test_tc_00001_fcm_device_wakeup = 1
    global run_test_tc_00001_admin_unlock_events
    run_test_tc_00001_admin_unlock_events = 1
    global run_test_tc_00001_fcm_admin_unlock
    run_test_tc_00001_fcm_admin_unlock = 1
    global run_test_tc_00001_fcm_Kiosk_unlock
    run_test_tc_00001_fcm_Kiosk_unlock = 1
    global run_test_tc_00001_Kiosk_lock_events
    run_test_tc_00001_Kiosk_lock_events = 1
    global run_test_tc_00001_admin_lock_events
    run_test_tc_00001_admin_lock_events = 1
    global run_test_tc_00001_fcm_admin_lock
    run_test_tc_00001_fcm_admin_lock = 1
    global run_test_tc_00001_fcm_Kiosk_lock
    run_test_tc_00001_fcm_Kiosk_lock = 1
    global run_test_tc_00001_fcm_device_wipe
    run_test_tc_00001_fcm_device_wipe = 1
    global run_test_tc_00001_fcm_device_poweroff
    run_test_tc_00001_fcm_device_poweroff = 1
    global run_test_tc_00001_fcm_device_reboot
    run_test_tc_00001_fcm_device_reboot = 1
    global run_test_tc_00001_Kiosk_unlock_events
    run_test_tc_00001_Kiosk_unlock_events = 1
    global run_test_tc_00001_fcm_update
    run_test_tc_00001_fcm_update = 1
    global run_test_tc_00001_fcm_force_stop_app
    run_test_tc_00001_fcm_force_stop_app = 1
    global run_test_tc_00001_fcm_remote_view
    run_test_tc_00001_fcm_remote_view = 1
    global run_test_tc_00001_fcm_device_lock
    run_test_tc_00001_fcm_device_lock = 1
    global run_test_tc_00001_apps
    run_test_tc_00001_apps = 1
    global run_test_tc_00002_apps
    run_test_tc_00002_apps = 1
    global run_test_tc_00001_auth
    run_test_tc_00001_auth = 1
    global run_test_tc_00001_notes
    run_test_tc_00001_notes = 1
    global run_test_tc_00002_notes
    run_test_tc_00002_notes = 1
    global run_test_tc_00001_screensharehistory
    run_test_tc_00001_screensharehistory = 1
    global run_test_tc_00001_webrtc_stream
    run_test_tc_00001_webrtc_stream = 1
    global run_test_tc_00001_updatedevice
    run_test_tc_00001_updatedevice = 1
    global run_test_tc_00002_screensharehistory
    run_test_tc_00002_screensharehistory = 1
if run_devicedetailscases == 1:
    test_device_details_page()
if run_positivetest == 1:
    test_positivetest()
def test_negativetest():
    global run_test_tc_00002_apps
    run_test_tc_00002_apps = 1
    global run_test_tc_00002_resetpswd_verifyOTP_invalid
    run_test_tc_00002_resetpswd_verifyOTP_invalid = 1
    global run_test_tc_00003_resetpswd_verifyOTP_emptyOTP
    run_test_tc_00003_resetpswd_verifyOTP_emptyOTP = 1
    global run_test_tc_00006_resetpswd_verifyOTP_emptypassword
    run_test_tc_00006_resetpswd_verifyOTP_emptypassword = 1
if run_negativetest == 1:
    test_negativetest()