from _datetime import datetime

# Getting android policy names  from license api
android_policyname = []

#get android devices with respect to policy type from get devices api
android_devices = []
kiosk_devices = []
wm_devices = []
wp_devices = []

#get devices from get devices api with respect to policy type from get devices api
iosdevices = []
non_dep_devices = []
dep_devices = []
iosdeviceid = []

# Getting ios profile names and ids(individual profile ids)  from license api
iOS_Profile_name = []
nondepProfileIds = []
depProfileIds = []

#Android policy ids from license api
android_policy_id = []
kioskIds = []
wmIds = []
wpIds = []

#Page sizes
pagesize_50 = 50
pagesize_100 = 100
pagesize_200 = 200
page_0 = 0
page_1 = 1
pagesize_30 = 30
pagesize_10000 =10000
pageSize_1000=1000
pagesize_10 =10

#disable apps ids from get api
disableapps_list= []

#Alert Notification id which gets post api
Notification_Object_id =""

#Account level Alert Notification id which gets post api
acc_notification_Object_id = ""

policytype = []

now_datetime = datetime.now()
start_of_day_datetime = now_datetime.replace(hour=00, minute=00, second=00)
end_of_day_datetime = now_datetime.replace(hour=23, minute=59, second=59)
start_timestamp = int(round(start_of_day_datetime.timestamp() * 1000))
end_timestamp = int(round(end_of_day_datetime.timestamp()* 1000))
isostart=datetime.utcfromtimestamp(start_timestamp/1000).strftime('%Y-%m-%dT%H:%M:%S.000Z')
isoend=datetime.utcfromtimestamp(end_timestamp/1000).strftime('%Y-%m-%dT%H:%M:%S.999Z')

