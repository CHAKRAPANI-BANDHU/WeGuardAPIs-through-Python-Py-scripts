from datetime import date, timedelta
import datetime
import globalvariables as globalvar
import groupglobalvar as variables

import globalvariables as var
global policyid
policyid = ""

global pId
pId = ""

type = "FCM_MESSAGE"
updtype = "FCM_UPDATE"
imei = ""

global BC_deviceid
BC_deviceid = ""

login_URL = "enterprise/rest/users/login"
global page
page = '1'
global pageSize
pageSize = '1000'
# Reset Password
#-----------------------------------------------------------------------------------------
otp = "4d9bcd24df3a26246322b0e286828ad55378c4b6c277a125f7e233d66c949737 "
newPassword = "2b217fd26f0506d7cfe87e08483838fe8bf130ce6b3a987d94adfd3d043454a5"
samePassword = "2b217fd26f0506d7cfe87e08483838fe8bf130ce6b3a987d94adfd3d043454a5"
#----------------------------------------------------------------------------------------------
# Broadcast
Imei = "866"
deviceType = "android"
#broadcast history details
historylist =[]
message= "{\"bgColor\":\"#000400\",\"textColor\":\"#4fffff\",\"title\":\"Announcement\",\"body\":\"Submit all the documents on time\"}"
message_group =  "{\"bgColor\":\"#000000\",\"textColor\":\"#ffffff\",\"title\":\"Announcement to Group Users\",\"body\":\"Submit all the documents on time\"}"
message_device ="{\"bgColor\":\"#000000\",\"textColor\":\"#ffffff\",\"title\":\"Announcment to Device holder"+BC_deviceid +"\",\"body\":\"Submit all the documents on time\"}"
Message_All_event ='{\"title\":\"Message broadcasted to All\",\"body\":{\"topic\":\"'+var.actcode+'_'+var.pactcode+'\",\"type\":\"FCM_MESSAGE\",\"isLicenseLevel\":true,\"actcode\":\"'+var.actcode+'\",\"pactcode\":\"'+var.pactcode+'\",\"message\":\"{\\\"bgColor\\\":\\\"#000000\\\",\\\"textColor\\\":\\\"#ffffff\\\",\\\"title\\\":\\\"Notice all\\\",\\\"body\\\":\\\"Stay safe at home\\\"}\",\"pId\":null,\"priority\":\"high\"}}'
Message_group_event ="{\"title\":\"Message broadcasted to group Boston Users\",\"body\":{\"topic\":\"5e9958fb77f85d51483d01fa_HXHXL\",\"type\":\"FCM_MESSAGE\",\"isLicenseLevel\":true,\"actcode\":\"HXHXL\",\"pactcode\":\"WELL-L0CO6\",\"message\":\"{\\\"bgColor\\\":\\\"#000000\\\",\\\"textColor\\\":\\\"#ffffff\\\",\\\"title\\\":\\\"Group Notice\\\",\\\"body\\\":\\\"Stay safe at home\\\"}\",\"pId\":\"5e9958fb77f85d51483d01fa\",\"priority\":\"high\"}}"
Message_device_event="{\"title\":\"Message broadcasted to device 5979869587579\",\"body\":{\"topic\":\"6467575768686_HXHXL_WELL-L0CO6\",\"type\":\"FCM_MESSAGE\",\"isLicenseLevel\":false,\"actcode\":\"HXHXL\",\"pactcode\":\"WELL-L0CO6\",\"message\":\"{\\\"bgColor\\\":\\\"#000000\\\",\\\"textColor\\\":\\\"#ffffff\\\",\\\"title\\\":\\\"Device Notice\\\",\\\"body\\\":\\\"Stay safe at Home\\\"}\",\"pId\":\"5e9958fb77f85d51483d01fa\",\"priority\":\"high\"}}"
image = "{\"title\":\"logo[1].png is uploaded in undefined policy\"}"

#-----------------------------------------------------------------------------------------------------------------------------------
page1 = "?page="
limit = "&limit="
limitvalue = '500'
#-----------------------------------------------------------------------------------------------------------------------------------
# WeTalk


message_fcm_all ="eyJtc2dQYXRoIjoiVFlMVFUvTkFOQy1SSVdINC9UaHJlYWRzIiwidGhyZWFkSWQiOiJBbm5vdW5jZW1lXzE1OTk0ODMwODk3MzMiLCJzdWJqZWN0IjoiQW5ub3VuY2VtZW50IHRvIEFMTCBsZXZlbCIsInByaW9yaXR5IjoiSGlnaCIsImlzVGhyZWFkIjp0cnVlLCJtZXNzYWdlIjoiU3VibWl0IHlvdXIgZG9jdW1lbnRzIG9uIHRpbWUifQ=="

message_fcm_group = "eyJtc2dQYXRoIjoiVFlMVFUvTkFOQy1SSVdINC9UaHJlYWRzIiwidGhyZWFkSWQiOiJBbm5vdW5jZW1lXzE1OTk0ODMyMTIwOTYiLCJzdWJqZWN0IjoiQW5ub3VuY2VtZW50IHRvIEdyb3VwIiwicHJpb3JpdHkiOiJIaWdoIiwiaXNUaHJlYWQiOnRydWUsIm1lc3NhZ2UiOiJQbGVhc2Ugc3VibWl0IGFsbCB5b3VyIGRvY3VtZW50IG9uIHRpbWUifQ=="

message_fcm_device ="eyJtc2dQYXRoIjoiVFlMVFUvTkFOQy1SSVdINC9UaHJlYWRzIiwidGhyZWFkSWQiOiJBbm5vdW5jZW1lXzE1OTk0ODMzMDkyMTUiLCJzdWJqZWN0IjoiQW5ub3VuY2VtZW50IHRvIERldmljZSIsInByaW9yaXR5IjoiSGlnaCIsImlzVGhyZWFkIjp0cnVlLCJtZXNzYWdlIjoiUGxlYXNlIHN1Ym1pdCB5b3UgZG9jdW1lbnRzIGZvciB2ZXJpZmljYXRpb24gb24gdGltZS4ifQ=="

calldeviceid = "869881036785080"

now = datetime.datetime.now()
element = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
nowtd = element
timestamp = int(datetime.datetime.timestamp(now)*1000)
WTtimestamp = str(timestamp)

datestart = date.today()
days_before = (now-timedelta(days=30))
days_before_element = days_before.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
startdate = str(days_before_element)
enddate = str(element)

date1 = date.today()
todaydate = "&from="+ str(date1) +"T00:00:00.000Z"+"&to="+str(date1)+"T23:59:59.999Z"

date2 = date1 - datetime.timedelta(days = 1)
yesterdaydate = "&from="+ str(date2) +"T00:00:00.000Z"+"&to="+str(date2)+"T23:59:59.999Z"

wetalk_grouplevel_event = {
  "agent": "PORTAL",
  "actorId": globalvar.userName,
  "policyId": variables.android_policy_id,
  "type": "Info",
  "msg": "{\"title\":\"New thread conversation started for group 5e9958fb77f85d51483d01fa\",\"body\":{\"displayName\":\"Boston Users\",\"createdBy\":\"OPS\",\"timestamp\":\"2020-07-01T18:18:38.432Z\",\"subject\":\"Group Notice\",\"message\":\"Stay safe at home\",\"importance\":\"High\",\"threadId\":\"Group Noti_1593627518432\",\"threadType\":\"Group\",\"threadStatus\":\"Active\",\"to\":\"5e9958fb77f85d51483d01fa\",\"lastUpdatedTime\":\"2020-07-01T18:18:38.432Z\",\"newMessageRecevied\":true,\"msgCount\":0,\"latestMessage\":\"Stay safe at home\"}}",
  "action": "-",
  "event": "WeTalk",
  "sentTime": timestamp,
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
  "sentTime": timestamp,
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
  "sentTime": timestamp,
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
  "sentTime": timestamp,
  "sourceIP": ""
}
#------------------------------------------------------------------------------------------
#device details view
id = "5f27f286fce966474413b5ce"
topic = "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode
apkDU_type ="APK_DU_USAGE"
endmsg ="Video calling is ended for the device "
callconfigs ={"enterprise": globalvar.companyName,"configName": "UserSettings","key": "settings","value": "{\"isVideoCallingEnabled\":true}"}
#fcm data
fcm={"actCode": globalvar.actcode, "isLicenseLevel": False, "pActCode": globalvar.pactcode, "pId": "5ede1149273d1b2ede5abb31","topic": globalvar.actcode+"_"+globalvar.pactcode,"type": "FCM_UPDATE"}
fcm_remoteview = {
  "topic":  "869881036785080"+"_"+globalvar.actcode+"_"+globalvar.pactcode,
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
  "actorId": "paddu121996.p@gmail.com",
  "policyId": None,
  "type": "Info",
  "msg": "Executed UNLOCK command for device with ID 351558071712584",
  "action": "-",
  "event": "Command",
  "sentTime": 1593631575544,
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
  "sentTime": timestamp,
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
  "sentTime": timestamp,
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
  "sentTime": timestamp,
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
  "deviceId": "869881036785080",
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
  "policyId": variables.android_policy_id,
  "activation": globalvar.actcode,
  "type": "General"
}
update_device_tags_ids = {
  "activationCode": globalvar.actcode,
  "productActivationCode": globalvar.pactcode,
  "updateDeviceRequest": [
    {
      "deviceID": "869881036785080",
      "id1": "QA",
      "id2": "ID card number",
      "id3": None,
      "adminTaggedName": "Wenable QA"
    }
  ]
}

