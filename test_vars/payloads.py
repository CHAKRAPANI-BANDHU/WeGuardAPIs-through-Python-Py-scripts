import globalvariables as globalvar
import WeBoxpayloadinfo as variable
import groupglobalvar as globals
import WeBoxpayloadinfo as vars

historylist =[]

global policyid
policyid = ""
global pId
pId = ""
type = "FCM_MESSAGE"
imei = ""
global BC_deviceid
BC_deviceid = ""

broadcast_All_topic = globalvar.actcode + "_" + globalvar.pactcode
broadcast_group_topic = policyid+"_"+ globalvar.actcode
broadcast_device_topic = BC_deviceid+ "_"+ globalvar.actcode+"_" + globalvar.pactcode
wetalk_device_topic = "WT_"+globalvar.actcode+"_"+globalvar.pactcode+"_"+ BC_deviceid
wetalk_All_topic = "WT_"+globalvar.actcode+"_"+globalvar.pactcode
wetalk_group_topic = "WT_"+globalvar.actcode+"_"+globalvar.pactcode+"_"+ policyid

login_URL = "enterprise/rest/users/login"
getdevices_URL = "enterprise/rest/weguard-v2/getDevices"
videocallsettings_URL = "enterprise/rest/wenablesso/config/save"
global page
page = '1'
global pageSize
pageSize = '1000'
# Reset Password
#-----------------------------------------------------------------------------------------
resetpswdOTP_URL = "enterprise/rest/users/resetPwdEmailOTP"
resetpswd_verifyOTP_URL = "enterprise/rest/users/verifyOTP"
otp = "4d9bcd24df3a26246322b0e286828ad55378c4b6c277a125f7e233d66c949737 "
newPassword = "2b217fd26f0506d7cfe87e08483838fe8bf130ce6b3a987d94adfd3d043454a5"
samePassword = "2b217fd26f0506d7cfe87e08483838fe8bf130ce6b3a987d94adfd3d043454a5"
#----------------------------------------------------------------------------------------------
# Broadcast
searchimei_URL = "enterprise/rest/weguard-v2/search?"
searchdeviceid_URL = "enterprise/rest/weguard-v2/searchimei"
msghis_devices_URL = "enterprise/rest/weguard-v2/messageHistory/devices/"
messagehistory_URL = "enterprise/rest/weguard-v2/messageHistory"
imei = "869"
deviceType = "android"
#-----------------------------------------------------------------------------------------------------------------------------------
# WeTalk
wetalkparams = "searchString=&page=1&pageSize=100000000"
Wetalk_search_URL = "enterprise/rest/weguard-v2/search?"
Wetalk_fcm_URL = "enterprise/rest/weguard-v2/fcmUpdate"
Wetalk_events_URL = "enterprise/rest/weguard/logs/events"
Wetalkcallauthtoken_URL = "enterprise/rest/wetalk/video/authtoken"
wetalkcallhistory_URL = "enterprise/rest/wetalk/history/user/"
calldeviceid = "869881036785080"
startdate = vars.isostart
enddate = vars.isoend

# today1 = datetime.date.today()
# globalvar.today = today1
# yesterday1 = today1 - datetime.timedelta(days=1)
# globalvar.yesterday = yesterday1
todaydate = "&from=2020-07-03T00:00:00.000Z&to=2020-07-03T23:59:59.999Z"
print(todaydate)
yesterdaydate = "&from=2020-07-03T00:00:00.000Z&to=2020-07-03T23:59:59.999Z"
print(yesterdaydate)

wetalk_grouplevel_event = {
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "{\"title\":\"New thread conversation started for group 5e9958fb77f85d51483d01fa\",\"body\":{\"displayName\":\"Boston Users\",\"createdBy\":\"OPS\",\"timestamp\":\"2020-07-01T18:18:38.432Z\",\"subject\":\"Group Notice\",\"message\":\"Stay safe at home\",\"importance\":\"High\",\"threadId\":\"Group Noti_1593627518432\",\"threadType\":\"Group\",\"threadStatus\":\"Active\",\"to\":\"5e9958fb77f85d51483d01fa\",\"lastUpdatedTime\":\"2020-07-01T18:18:38.432Z\",\"newMessageRecevied\":true,\"msgCount\":0,\"latestMessage\":\"Stay safe at home\"}}",
  "action": "-",
  "event": "WeTalk",
  "sentTime": variable.start_timestamp,
  "sourceIP": ""
}
wetalk_alllevel_event = {
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "{\"title\":\"New thread conversation started for all\",\"body\":{\"createdBy\":\"OPS\",\"timestamp\":\"2020-07-01T18:13:38.488Z\",\"subject\":\"Notice All\",\"message\":\"Stay healthy and focused\",\"importance\":\"Medium\",\"threadId\":\"Notice  Al_1593627218486\",\"threadType\":\"Group\",\"threadStatus\":\"Active\",\"to\":\"All\",\"lastUpdatedTime\":\"2020-07-01T18:13:38.489Z\",\"newMessageRecevied\":true,\"msgCount\":0,\"latestMessage\":\"Stay healthy and focused \"}}",
  "action": "-",
  "event": "WeTalk",
  "sentTime": variable.start_timestamp,
  "sourceIP": ""
}
wetalk_devicelevel_event ={
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "{\"title\":\"New thread conversation started for device 351558071712584\",\"body\":{\"displayName\":\"Boston Users\",\"createdBy\":\"OPS\",\"timestamp\":\"2020-07-01T18:21:19.126Z\",\"subject\":\"Device Notice\",\"message\":\"Stay healthy\",\"importance\":\"High\",\"threadId\":\"Device Not_1593627679126\",\"threadType\":\"Individual\",\"threadStatus\":\"Active\",\"to\":\"351558071712584\",\"lastUpdatedTime\":\"2020-07-01T18:21:19.127Z\",\"newMessageRecevied\":true,\"msgCount\":0,\"latestMessage\":\"Stay healthy\"}}",
  "action": "-",
  "event": "WeTalk",
  "sentTime": variable.start_timestamp,
  "sourceIP": ""
}
wetalk_complete_event = {
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "{\"title\":\"Thread with subject Notice All is marked as complete\",\"body\":{\"createdBy\":\"OPS\",\"importance\":\"Medium\",\"lastUpdatedTime\":{\"seconds\":1593627218,\"nanoseconds\":489000000},\"latestMessage\":\"Stay healthy and focused \",\"message\":\"Stay healthy and focused\",\"msgCount\":0,\"newMessageRecevied\":true,\"subject\":\"Notice All\",\"threadId\":\"Notice  Al_1593627218486\",\"threadStatus\":\"active\",\"threadType\":\"Group\",\"timestamp\":{\"seconds\":1593627218,\"nanoseconds\":488000000},\"to\":\"All\",\"convtTime\":1593627218000,\"lastUpdateTime\":1593627218000,\"modSub\":\"Notice All\",\"isSubExceeds20Chars\":false,\"modifiedTo\":\"All\",\"modLatestMsg\":\"Stay healthy and foc\",\"isLatestMsgExceeds20Chars\":true,\"modMessage\":\"Stay healthy and focused\"}}",
  "action": "-",
  "event": "WeTalk",
  "sentTime": variable.start_timestamp,
  "sourceIP": ""
}
#------------------------------------------------------------------------------------------
#device details view
get_apps_URL = "enterprise/rest/deviceapps/apps/"
auth_URL = "enterprise/rest/webrtc/auth"
screesharehistory_device_URL = "enterprise/rest/webrtc/screensharehistory/869881036785080?page=1&pageSize=10&email=qateam.129@gmail.com"
webrct_stream_URL = "enterprise/rest/webrtc/stream/"
fcm_URL = "enterprise/rest/weguard-v2/fcmUpdate"
events_URL = "enterprise/rest/weguard/logs/events"
screesharehistory_URL ="enterprise/rest/webrtc/screensharehistory"
deviceupdate_URL = "enterprise/rest/weguard-v2/updateDevice"
notes_URL = "enterprise/rest/notes"
device_broadcast_URL = "enterprise/rest/weguard-v2/messageHistory/"
id = "5ec0c039c586810af06d3c54"
topic = "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode

#fcm data
fcm={"actCode": globalvar.actcode, "isLicenseLevel": False, "pActCode": globalvar.pactcode, "pId": "5ede1149273d1b2ede5abb31","topic": globalvar.actcode+"_"+globalvar.pactcode,"type": "FCM_UPDATE"}
fcm_remoteview = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "FCM_REMOTE_VIEW",
  "isLicenseLevel": False,
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
fcm_forcestopapp = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "FORCE_STOP_APP",
  "isLicenseLevel": False,
  "message": "{\"appId\":\"com.opera.mini.android\"}",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
kiosk_unlock = { #fcm
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "UNLOCK_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
kiosk_unlock_events = {
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "Executed UNLOCK command for device with ID 351558071712584",
  "action": "-",
  "event": "Command",
  "sentTime": vars.start_timestamp,
  "sourceIP": ""
}
fcm_kiosk_lock = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "LOCK_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
kiosk_lock_events ={
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "Executed LOCK command for device with ID 351558071712584",
  "action": "-",
  "event": "Command",
  "sentTime": vars.start_timestamp,
  "sourceIP": ""
}
fcm_admin_lock = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "ADMIN_LOCK_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high",
  "message": "Your device is locked, please contact administrator."
}
admin_lock_events = {
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "Executed ADMIN command for device with ID 351558071712584",
  "action": "-",
  "event": "Command",
  "sentTime": vars.start_timestamp,
  "sourceIP": ""
}
fcm_admin_unlock= {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "ADMIN_UNLOCK_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
admin_unlock_events ={
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": None,
  "type": "Info",
  "msg": "Executed ADMIN command for device with ID 351558071712584",
  "action": "-",
  "event": "Command",
  "sentTime": vars.start_timestamp,
  "sourceIP": ""
}
fcm_reboot = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "RESTART_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
fcm_poweroff = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "POWER_OFF_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
fcm_wipe_device ={
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "WIPE_DEVICE",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode,
  "priority": "high"
}
fcm_device_wakeup = {
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "type": "DEVICE_WAKEUP",
  "priority": "high",
  "isLicenseLevel": False,
  "pId": "5e9958fb77f85d51483d01fa",
  "actCode": globalvar.actcode,
  "pActCode": globalvar.pactcode
}
screensharehistory_starteddata = {
  "sessionId": "951633333",
  "deviceId": "351558071712584",
  "actor": globalvar.userName,
  "status": "Started",
  "role": "customer_admin",
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "date": 1593635042118
}
screensharehistory_endeddata = {
  "sessionId": "951633333",
  "deviceId": "869881036785080",
  "actor": globalvar.userName,
  "status": "Ended",
  "role": "customer_admin",
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "date": 1593635332173
}
screensharehistory_aborted = {
  "sessionId": "948682288",
  "deviceId": "869881036785080",
  "actor": globalvar.userName,
  "status": "Aborted",
  "role": "customer_admin",
  "topic": "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
  "date": 1593675320779
}
general_notes = {
  "deviceId": "869881036785080",
  "note": "Device status is not correct",
  "policyId": "5e9958fb77f85d51483d01fa",
  "activation": globalvar.actcode,
  "type": "General"
}
update_device_tags_ids = {
  "activationCode": globalvar.actcode,
  "productActivationCode": globalvar.pactcode,
  "updateDeviceRequest": [
    {
      "deviceID": "869881036785080",
      "id1": "Name",
      "id2": "Id card number",
      "id3": None,
      "adminTaggedName": "Wenable QA"
    }
  ]
}

