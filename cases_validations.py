
mycases_positive = 0
mycases_negative = 0
mycases_devices = 0
mycases_policygroups = 0
mycases_login_after = 0
mycases_sprint20 = 1



# Declaration for accoount level
run_test_003_account_get_alert_configs = 1
run_test_003_account_post_alert_configs = 1
run_test_003_account_put_alert_configs = 1

# Declarations for positive cases after login

run_tc_001_admin_login = 0
run_tc_001_admin_login_event_logs = 1
run_tc_001_admin_config = 0
run_tc_001_UI_version = 0
run_tc_001_help_Text_after_login = 1
run_tc_001__get_users = 1
run_test_001_license_5000 = 1
run_test_001_bannerNotification_read = 1

# Decalarations for negative cases of login
run_tc_001_admin_login_invalid_Email = 1
run_tc_001_admin_login_invalid_Pwd = 1
run_tc_001_admin_login_with_spaces = 1
run_tc_001_admin_login_userName_spaces = 1
run_tc_001_admin_login_pwd_spaces = 1

# license api negative case after login
run_test_001_license_100 = 1
run_test_001_license_1000 = 1

# Declarations for postive cases on the Devices page
run_test_002_get_devices_size_50 = 1
run_test_002_get_devices_size_100 = 1
run_test_002_policy_device = 1
run_test_002_move_device_android = 0
run_test_002_events_move_device_android = 0
run_test_002_fcm_update_move_device_android = 0
run_test_002_transfer_device_iOS = 0
run_test_002_update_device_android = 0
run_test_002_update_device_iOS = 0
run_test_002_notes_devices_page_android_iOS = 0
run_test_002_delete_device_iOS = 0
run_test_002_fcm_update_move_device_webox = 0
run_test_002_fcm_move_device_files_webox = 0
run_test_002_fcm_change_group_move_device_webox = 0
run_test_002_delete_device_android = 0
run_test_002_get_devices_size_200 = 1
run_test_002_get_devices = 1

# devices page negative cases
run_test_002_get_devices_size_100_size_0 = 1
run_test_002_policy_device_invalid_policy_id = 0

# Declarations for positive cases on the policy_groups page
run_test_tc_003_devices_count_pageSize_10000 = 1
run_test_tc_003_devices_count_pageSize_1000 = 1
run_test_tc_003_devices_forgroup_pageSize_50 = 1
run_test_tc_003_devices_forgroup_pageSize_100 = 1
run_test_tc_003_act_pact_code = 0
run_test_tc_003_group_list = 1
run_test_tc_003_group_disable_apps = 1
run_test_tc_003_group_msg_history = 1
run_test_tc_003_group_location_track = 1
run_test_tc_003_group_cloning_android = 0
run_test_tc_003_group_cloning_iOS = 0
run_test_tc_003_devices_group_iOS = 0
run_test_tc_003_profiles_group_iOS = 0
run_test_tc_003_system_apps_group_iOS = 0
run_test_tc_003_managed_apps_group_iOS = 0
run_test_tc_003_transfer_device_group_iOS = 0
run_test_tc_003_rolesandaccess = 0
run_test_tc_003_delete_group_iOS = 0
run_test_tc_003_events_delete_group_iOS = 0
run_test_tc_003_delete_group_save_configs = 0
run_test_tc_003_delete_group_android = 0
run_test_tc_003_event_delete_group_android = 0
run_test_tc_003_update_group_iOS = 0
run_test_tc_003_events_update_group_iOS = 0
run_test_tc_003_search_devices_group_Android_3digits = 0
run_test_tc_003_search_devices_group_iOS_3strs = 0
run_test_tc_003_files_while_cloning = 0
run_test_tc_003_event_after_cloning_group_Android = 0
run_test_tc_003_event_after_cloning_group_iOS = 0
run_test_tc_003_webox_configs_cloning_Android = 0
run_test_tc_003_webox_configs_cloning_iOS = 0
run_test_tc_003_group_msg_history_page_1000 = 0
run_test_tc_003_group_msg_history_page_100 = 0
run_test_tc_003_app_burndown_iOS = 0
run_test_tc_003_app_burndown_retry_iOS = 0
run_test_tc_003_app_customupload = 0
run_test_tc_003_track_configs_update = 0
run_test_tc_003_update_group_android = 0
run_test_tc_003_event_update_group_android = 0
run_test_tc_003_fcm_update_group_android = 0
run_test_tc_003_approve_after_update = 0
run_test_tc_003_installs = 0
run_test_tc_003_uninstalls = 0
run_test_tc_003_generate_QR_android = 0
run_test_tc_003_search_apps_iOS = 0
run_test_tc_003_generate_QR_NON_DEP = 0
run_test_tc_003_devices_forgroup_pageSize_200 = 1
run_test_tc_003_put_disable_apps = 0
run_test_tc_003_delete_disable_apps = 0
run_test_tc_003_post_disable_apps = 0
run_test_tc_003_approve_product = 0
run_test_tc_003_unapprove_product = 0
run_test_tc_003_appresSchema = 0
run_test_tc_003_system_apps_limit_10 = 1
run_test_tc_003_system_apps_limit_50 = 1
run_test_tc_003_system_apps_limit_100 =  1
run_test_tc_003_get_systemapp_10 = 1
run_test_tc_003_get_systemapp_50 = 1
run_test_tc_003_get_systemapp_100 = 1
run_test_tc_003_get_datausage_configs_android = 1
run_test_tc_003_post_datausage_configs_android = 0
run_test_003_policy_post_alert_configs = 1
run_test_003_policy_put_alert_configs = 1
run_test_003_policy_get_alert_configs = 1



# Declarations for policy_groups negative cases
run_test_tc_003_search_devices_group_2digits_Android = 0
run_test_tc_003_search_devices_group_1digit_Android = 0
run_test_tc_003_search_devices_group_2strs_iOS = 0
run_test_tc_003_search_devices_group_1str_iOS = 0
run_test_tc_003_devices_count_pageSize_1000_page_0 = 0
run_test_tc_003_devices_forgroup_pageSize_50_page_0 = 0
run_test_tc_003_group_msg_history_page_100_page_0 = 0
run_test_tc_003_group_location_track_invalid_policyid = 0
run_test_tc_003_devices_group_iOS_1000_size_1 = 1
run_test_tc_003_generate_Invalid_QR_android = 0
run_test_tc_003_generate_invalid_QR_NON_DEP  = 0
run_test_tc_003_invalid_disable_apps = 0
run_test_tc_003_get_datausage_invalid_policyid_android = 0


def run_positive_cases():
# after login
    global run_tc_001_admin_login
    run_tc_001_admin_login = 1
    global run_tc_001_admin_login_event_logs
    run_tc_001_admin_login_event_logs = 1
    global run_tc_001_admin_config
    run_tc_001_admin_config = 1
    global run_tc_001_prod_version
    run_tc_001_prod_version = 1
    global run_tc_001_help_Text_after_login
    run_tc_001_help_Text_after_login = 1
    global run_tc_001__get_users
    run_tc_001__get_users = 1
    global run_test_001_license
    run_test_001_license = 1
    global run_test_001_bannerNotification_read
    run_test_001_bannerNotification_read = 1
    global run_test_tc_003_app_customupload
    run_test_tc_003_app_customupload = 1

# devices page

    global run_test_002_get_devices_size_50
    run_test_002_get_devices_size_50 = 1
    global run_test_002_get_devices_size_100
    run_test_002_get_devices_size_100 = 1
    global  run_test_002_policy_device
    run_test_002_policy_device = 1
    global  run_test_002_move_device_android
    run_test_002_move_device_android = 1
    global run_test_002_events_move_device_android
    run_test_002_events_move_device_android = 1
    global run_test_002_fcm_update_move_device_android
    run_test_002_fcm_update_move_device_android = 1
    global run_test_002_transfer_device_iOS
    run_test_002_transfer_device_iOS = 0
    global run_test_002_fcm_update_move_device_webox
    run_test_002_fcm_update_move_device_webox = 1
    global run_test_002_fcm_move_device_files_webox
    run_test_002_fcm_move_device_files_webox = 1
    global run_test_002_fcm_change_group_move_device_webox
    run_test_002_fcm_change_group_move_device_webox =1
    global run_test_002_delete_device_android
    run_test_002_delete_device_android = 1
    global run_test_001_license_5000
    run_test_001_license_5000 = 1
    global run_test_002_update_device_android
    run_test_002_update_device_android = 1
    global run_test_002_update_device_iOS
    run_test_002_update_device_iOS = 1
    global run_test_002_delete_device_iOS
    run_test_002_delete_device_iOS = 1
    global run_test_002_notes_devices_page_android_iOS
    run_test_002_notes_devices_page_android_iOS = 1
    global run_test_002_get_devices_size_200
    run_test_002_get_devices_size_200 = 1

#policy_groups
    global run_test_tc_003_devices_count_pageSize_10000
    run_test_tc_003_devices_count_pageSize_10000 = 1
    global run_test_tc_003_devices_count_pageSize_1000
    run_test_tc_003_devices_count_pageSize_1000 = 1
    global run_test_tc_003_devices_forgroup_pageSize_50
    run_test_tc_003_devices_forgroup_pageSize_50 = 1
    global run_test_tc_003_devices_forgroup_pageSize_100
    run_test_tc_003_devices_forgroup_pageSize_100 = 1
    global run_test_tc_003_act_pact_code
    run_test_tc_003_act_pact_code = 1
    global run_test_tc_003_groups_list
    run_test_tc_003_groups_list = 1
    global run_test_tc_003_group_disable_apps
    run_test_tc_003_group_disable_apps = 1
    global run_test_tc_003_group_msg_history
    run_test_tc_003_group_msg_history = 1
    global run_test_tc_003_group_location_track
    run_test_tc_003_group_location_track =1
    global run_test_tc_003_group_cloning_android
    run_test_tc_003_group_cloning_android = 1
    global run_test_tc_003_group_cloning_iOS
    run_test_tc_003_group_cloning_iOS =1
    global run_test_tc_003_devices_group_iOS
    run_test_tc_003_devices_group_iOS = 1
    global run_test_tc_003_profiles_group_iOS
    global run_test_tc_003_system_apps_group_iOS
    run_test_tc_003_profiles_group_iOS = 1
    run_test_tc_003_system_apps_group_iOS = 1
    global run_test_tc_003_managed_apps_group_iOS
    run_test_tc_003_managed_apps_group_iOS = 1
    global run_test_tc_003_transfer_device_group_iOS
    run_test_tc_003_transfer_device_group_iOS = 1
    global run_test_tc_003_rolesandaccess
    run_test_tc_003_rolesandaccess = 1
    global run_test_tc_003_delete_group_iOS
    run_test_tc_003_delete_group_iOS = 1
    global run_test_tc_003_events_delete_group_iOS
    run_test_tc_003_events_delete_group_iOS = 1
    global run_test_tc_003_delete_group_save_configs
    run_test_tc_003_delete_group_save_configs = 1
    global run_test_tc_003_delete_group_android
    run_test_tc_003_delete_group_android =1
    global run_test_tc_003_event_delete_group_android
    run_test_tc_003_event_delete_group_android = 1
    global run_test_tc_003_update_group_iOS
    run_test_tc_003_update_group_iOS = 1
    global run_test_tc_003_events_update_group_iOS
    run_test_tc_003_events_update_group_iOS = 1
    global run_test_tc_003_search_devices_group_Android_3digits
    run_test_tc_003_search_devices_group_Android_3digits = 1
    global run_test_tc_003_search_devices_group_iOS_3strs
    run_test_tc_003_search_devices_group_iOS_3strs = 1
    global run_test_tc_003_files_while_cloning
    run_test_tc_003_files_while_cloning =1
    global run_test_tc_003_event_after_cloning_group_Android
    run_test_tc_003_event_after_cloning_group_Android = 1
    global run_test_tc_003_event_after_cloning_group_iOS
    run_test_tc_003_event_after_cloning_group_iOS = 1
    global run_test_tc_003_webox_configs_cloning_Android
    run_test_tc_003_webox_configs_cloning_Android = 1
    global run_test_tc_003_webox_configs_cloning_iOS
    run_test_tc_003_webox_configs_cloning_iOS = 1
    global run_test_tc_003_group_msg_history_page_1000
    run_test_tc_003_group_msg_history_page_1000 = 1
    global run_test_tc_003_group_msg_history_page_100
    run_test_tc_003_group_msg_history_page_100 = 1
    global run_test_tc_003_app_burndown_iOS
    run_test_tc_003_app_burndown_iOS = 1
    global run_test_tc_003_app_burndown_retry_iOS
    run_test_tc_003_app_burndown_retry_iOS = 1
    global run_test_tc_003_track_configs_update
    run_test_tc_003_track_configs_update  = 1
    global run_test_tc_003_update_group_android
    run_test_tc_003_update_group_android = 1
    global run_test_tc_003_event_update_group_android
    run_test_tc_003_event_update_group_android = 1
    global run_test_tc_003_fcm_update_group_android
    run_test_tc_003_fcm_update_group_android = 1
    global run_test_tc_003_approve_after_update
    run_test_tc_003_approve_after_update = 1
    global run_test_tc_003_installs
    run_test_tc_003_installs = 1
    global run_test_tc_003_uninstalls
    run_test_tc_003_uninstalls = 1
    global run_test_tc_003_group_list
    run_test_tc_003_group_list = 1
    global run_test_tc_003_generate_QR_android
    run_test_tc_003_generate_QR_android = 1
    global run_test_tc_003_search_apps_iOS
    run_test_tc_003_search_apps_iOS = 1
    global run_test_tc_003_generate_QR_NON_DEP
    run_test_tc_003_generate_QR_NON_DEP = 1
    global run_test_tc_003_devices_forgroup_pageSize_200
    run_test_tc_003_devices_forgroup_pageSize_200 = 1
    global run_test_tc_003_put_disable_apps
    run_test_tc_003_put_disable_apps = 1
    global run_test_tc_003_delete_disable_apps
    run_test_tc_003_delete_disable_apps = 1
    global run_test_tc_003_post_disable_apps
    run_test_tc_003_post_disable_apps = 1
    global run_test_tc_003_approve_product
    run_test_tc_003_approve_product = 1
    global run_test_tc_003_unapprove_product
    run_test_tc_003_unapprove_product = 1
    global run_test_tc_003_appresSchema
    run_test_tc_003_appresSchema = 1
    global run_test_tc_003_system_apps_limit_10
    run_test_tc_003_system_apps_limit_10 = 1
    global run_test_tc_003_system_apps_limit_50
    run_test_tc_003_system_apps_limit_50 = 1
    global run_test_tc_003_system_apps_limit_100
    run_test_tc_003_system_apps_limit_100 = 1
    global run_test_tc_003_get_systemapp_10
    run_test_tc_003_get_systemapp_10 = 1
    global run_test_tc_003_get_systemapp_50
    run_test_tc_003_get_systemapp_50 = 1
    global run_test_tc_003_get_systemapp_100
    run_test_tc_003_get_systemapp_100 = 1
    global run_test_002_get_devices
    run_test_002_get_devices = 1
    global run_test_tc_003_get_datausage_configs_android
    run_test_tc_003_get_datausage_configs_android =1
    global run_test_tc_003_post_datausage_configs_android
    run_test_tc_003_post_datausage_configs_android =1
    global run_test_003_policy_post_alert_configs
    run_test_003_policy_post_alert_configs = 1
    global run_test_003_policy_put_alert_configs
    run_test_003_policy_put_alert_configs = 1
    global run_test_003_policy_get_alert_configs
    run_test_003_policy_get_alert_configs = 1




def run_negative_cases():
# login
    global run_tc_001_admin_login
    run_tc_001_admin_login = 1
    global run_tc_001_admin_login_invalid_Email
    run_tc_001_admin_login_invalid_Email= 1
    global run_tc_001_admin_login_invalid_Pwd
    run_tc_001_admin_login_invalid_Pwd =  1
    global run_tc_001_admin_login_with_spaces
    run_tc_001_admin_login_with_spaces = 1
    global run_tc_001_admin_login_userName_spaces
    run_tc_001_admin_login_userName_spaces = 1
    global run_tc_001_admin_login_pwd_spaces
    run_tc_001_admin_login_pwd_spaces = 1

#after login license api negative cases
    global run_test_001_license_100
    run_test_001_license_100 = 1
    global run_test_001_license_1000
    run_test_001_license_1000 = 1

#devices page
    global run_test_002_get_devices_size_100_size_0
    run_test_002_get_devices_size_100_size_0 = 1
    global run_test_002_policy_device_invalid_policy_id
    run_test_002_policy_device_invalid_policy_id = 1




#policy_groups
# -search device
    global run_test_tc_003_search_devices_group_2digits_Android
    run_test_tc_003_search_devices_group_2digits_Android = 1
    global run_test_tc_003_search_devices_group_1digit_Android
    run_test_tc_003_search_devices_group_1digit_Android = 1
    global run_test_tc_003_search_devices_group_2strs_iOS
    run_test_tc_003_search_devices_group_2strs_iOS = 1
    global run_test_tc_003_search_devices_group_1str_iOS
    run_test_tc_003_search_devices_group_1str_iOS = 1

#data usage
    global run_test_tc_003_get_datausage_invalid_policyid_android
    run_test_tc_003_get_datausage_invalid_policyid_android = 1
#poicy groups - devices count
    global run_test_tc_003_devices_count_pageSize_1000_page_0
    run_test_tc_003_devices_count_pageSize_1000_page_0 = 1
#policy-grouos-for group
    global run_test_tc_003_devices_forgroup_pageSize_50_page_0
    run_test_tc_003_devices_forgroup_pageSize_50_page_0 = 1

#msg history in a group
    global run_test_tc_003_group_msg_history_page_100_page_0
    run_test_tc_003_group_msg_history_page_100_page_0 =1

#invalid policy id for a grp track config
    global run_test_tc_003_group_location_track_invalid_policyid
    run_test_tc_003_group_location_track_invalid_policyid = 1

#iOS devices in a policy(display 1000 in 2 pages)
    global run_test_tc_003_devices_group_iOS_1000_size_1
    run_test_tc_003_devices_group_iOS_1000_size_1 = 1
#Invlaid Android QR
    global run_test_tc_003_generate_Invalid_QR_android
    run_test_tc_003_generate_Invalid_QR_android = 1
#invalid NON-DEP QR
    global run_test_tc_003_generate_invalid_QR_NON_DEP
    run_test_tc_003_generate_invalid_QR_NON_DEP = 1

    global run_test_tc_003_invalid_disable_apps
    run_test_tc_003_invalid_disable_apps = 1

def devices():
    global run_test_002_get_devices_size_50
    run_test_002_get_devices_size_50 = 1
    global run_test_002_get_devices_size_100
    run_test_002_get_devices_size_100 = 1
    global run_test_002_policy_device
    run_test_002_policy_device = 1
    global run_test_002_move_device_android
    run_test_002_move_device_android = 1
    global run_test_002_events_move_device_android
    run_test_002_events_move_device_android = 1
    global run_test_002_fcm_update_move_device_android
    run_test_002_fcm_update_move_device_android = 1
    global run_test_002_transfer_device_iOS
    run_test_002_transfer_device_iOS = 0
    global run_test_002_fcm_update_move_device_webox
    run_test_002_fcm_update_move_device_webox = 1
    global run_test_002_fcm_move_device_files_webox
    run_test_002_fcm_move_device_files_webox = 1
    global run_test_002_fcm_change_group_move_device_webox
    run_test_002_fcm_change_group_move_device_webox = 1
    global run_test_002_delete_device_android
    run_test_002_delete_device_android = 1
    global run_test_001_license_10000
    run_test_001_license_10000 = 1
    global run_test_002_update_device_android
    run_test_002_update_device_android = 1
    global run_test_002_update_device_iOS
    run_test_002_update_device_iOS = 1
    global run_test_002_delete_device_iOS
    run_test_002_delete_device_iOS = 1
    global run_test_002_notes_devices_page_android_iOS
    run_test_002_notes_devices_page_android_iOS = 1
    global run_test_002_get_devices_size_200
    run_test_002_get_devices_size_200 = 1
    global run_test_002_get_devices_size_100_size_0
    run_test_002_get_devices_size_100_size_0 = 1
    global run_test_002_policy_device_invalid_policy_id
    run_test_002_policy_device_invalid_policy_id = 1
    global run_test_002_get_devices
    run_test_002_get_devices = 1

def policygroups():
    global run_test_tc_003_devices_count_pageSize_10000
    run_test_tc_003_devices_count_pageSize_10000 = 1
    global run_test_tc_003_devices_count_pageSize_1000
    run_test_tc_003_devices_count_pageSize_1000 = 1
    global run_test_tc_003_devices_forgroup_pageSize_50
    run_test_tc_003_devices_forgroup_pageSize_50 = 1
    global run_test_tc_003_devices_forgroup_pageSize_100
    run_test_tc_003_devices_forgroup_pageSize_100 = 1
    global run_test_tc_003_act_pact_code
    run_test_tc_003_act_pact_code = 1
    global run_test_tc_003_groups_list
    run_test_tc_003_groups_list = 1
    global run_test_tc_003_group_disable_apps
    run_test_tc_003_group_disable_apps = 1
    global run_test_tc_003_group_msg_history
    run_test_tc_003_group_msg_history = 1
    global run_test_tc_003_group_location_track
    run_test_tc_003_group_location_track =1
    global run_test_tc_003_group_cloning_android
    run_test_tc_003_group_cloning_android = 1
    global run_test_tc_003_group_cloning_iOS
    run_test_tc_003_group_cloning_iOS =1
    global run_test_tc_003_devices_group_iOS
    run_test_tc_003_devices_group_iOS = 1
    global run_test_tc_003_profiles_group_iOS
    global run_test_tc_003_system_apps_group_iOS
    run_test_tc_003_profiles_group_iOS = 1
    run_test_tc_003_system_apps_group_iOS = 1
    global run_test_tc_003_managed_apps_group_iOS
    run_test_tc_003_managed_apps_group_iOS = 1
    global run_test_tc_003_transfer_device_group_iOS
    run_test_tc_003_transfer_device_group_iOS = 1
    global run_test_tc_003_rolesandaccess
    run_test_tc_003_rolesandaccess = 1
    global run_test_tc_003_delete_group_iOS
    run_test_tc_003_delete_group_iOS = 1
    global run_test_tc_003_events_delete_group_iOS
    run_test_tc_003_events_delete_group_iOS = 1
    global run_test_tc_003_delete_group_save_configs
    run_test_tc_003_delete_group_save_configs = 1
    global run_test_tc_003_delete_group_android
    run_test_tc_003_delete_group_android =1
    global run_test_tc_003_event_delete_group_android
    run_test_tc_003_event_delete_group_android = 1
    global run_test_tc_003_update_group_iOS
    run_test_tc_003_update_group_iOS = 1
    global run_test_tc_003_events_update_group_iOS
    run_test_tc_003_events_update_group_iOS = 1
    global run_test_tc_003_search_devices_group_Android_3digits
    run_test_tc_003_search_devices_group_Android_3digits = 1
    global run_test_tc_003_search_devices_group_iOS_3strs
    run_test_tc_003_search_devices_group_iOS_3strs = 1
    global run_test_tc_003_files_while_cloning
    run_test_tc_003_files_while_cloning =1
    global run_test_tc_003_event_after_cloning_group_Android
    run_test_tc_003_event_after_cloning_group_Android = 1
    global run_test_tc_003_event_after_cloning_group_iOS
    run_test_tc_003_event_after_cloning_group_iOS = 1
    global run_test_tc_003_webox_configs_cloning_Android
    run_test_tc_003_webox_configs_cloning_Android = 1
    global run_test_tc_003_webox_configs_cloning_iOS
    run_test_tc_003_webox_configs_cloning_iOS = 1
    global run_test_tc_003_group_msg_history_page_1000
    run_test_tc_003_group_msg_history_page_1000 = 1
    global run_test_tc_003_group_msg_history_page_100
    run_test_tc_003_group_msg_history_page_100 = 1
    global run_test_tc_003_app_burndown_iOS
    run_test_tc_003_app_burndown_iOS = 1
    global run_test_tc_003_app_burndown_retry_iOS
    run_test_tc_003_app_burndown_retry_iOS = 1
    global run_test_tc_003_track_configs_update
    run_test_tc_003_track_configs_update  = 1
    global run_test_tc_003_update_group_android
    run_test_tc_003_update_group_android = 1
    global run_test_tc_003_event_update_group_android
    run_test_tc_003_event_update_group_android = 1
    global run_test_tc_003_fcm_update_group_android
    run_test_tc_003_fcm_update_group_android = 1
    global run_test_tc_003_approve_after_update
    run_test_tc_003_approve_after_update = 1
    global run_test_tc_003_installs
    run_test_tc_003_installs = 1
    global run_test_tc_003_uninstalls
    run_test_tc_003_uninstalls = 1
    global run_test_tc_003_group_list
    run_test_tc_003_group_list = 1
    global run_test_tc_003_generate_QR_android
    run_test_tc_003_generate_QR_android = 1
    global run_test_tc_003_search_apps_iOS
    run_test_tc_003_search_apps_iOS = 1
    global run_test_tc_003_generate_QR_NON_DEP
    run_test_tc_003_generate_QR_NON_DEP = 1
    global run_test_tc_003_devices_forgroup_pageSize_200
    run_test_tc_003_devices_forgroup_pageSize_200 = 1
    global run_test_tc_003_put_disable_apps
    run_test_tc_003_put_disable_apps = 1
    global run_test_tc_003_delete_disable_apps
    run_test_tc_003_delete_disable_apps = 1
    global run_test_tc_003_post_disable_apps
    run_test_tc_003_post_disable_apps = 1
    global run_test_tc_003_search_devices_group_2digits_Android
    run_test_tc_003_search_devices_group_2digits_Android = 1
    global run_test_tc_003_search_devices_group_1digit_Android
    run_test_tc_003_search_devices_group_1digit_Android = 1
    global run_test_tc_003_search_devices_group_2strs_iOS
    run_test_tc_003_search_devices_group_2strs_iOS = 1
    global run_test_tc_003_search_devices_group_1str_iOS
    run_test_tc_003_search_devices_group_1str_iOS = 1
    global run_test_tc_003_approve_product
    run_test_tc_003_approve_product = 1
    global run_test_tc_003_unapprove_product
    run_test_tc_003_unapprove_product = 1
    global run_test_tc_003_appresSchema
    run_test_tc_003_appresSchema = 1
    global run_test_tc_003_get_datausage_configs_android
    run_test_tc_003_get_datausage_configs_android = 1
    global run_test_tc_003_post_datausage_configs_android
    run_test_tc_003_post_datausage_configs_android = 1
    global run_test_003_policy_post_alert_configs
    run_test_003_policy_post_alert_configs = 1
    global run_test_003_policy_put_alert_configs
    run_test_003_policy_put_alert_configs = 1
    global run_test_003_policy_get_alert_configs
    run_test_003_policy_get_alert_configs = 1

    # poicy groups - devices count
    global run_test_tc_003_devices_count_pageSize_1000_page_0
    run_test_tc_003_devices_count_pageSize_1000_page_0 = 1
    # policy-grouos-for group
    global run_test_tc_003_devices_forgroup_pageSize_50_page_0
    run_test_tc_003_devices_forgroup_pageSize_50_page_0 = 1

    # msg history in a group
    global run_test_tc_003_group_msg_history_page_100_page_0
    run_test_tc_003_group_msg_history_page_100_page_0 = 1

    # invalid policy id for a grp track config
    global run_test_tc_003_group_location_track_invalid_policyid
    run_test_tc_003_group_location_track_invalid_policyid = 1

    # iOS devices in a policy(display 1000 in 2 pages)
    global run_test_tc_003_devices_group_iOS_1000_size_1
    run_test_tc_003_devices_group_iOS_1000_size_1 = 1
    # Invlaid Android QR
    global run_test_tc_003_generate_Invalid_QR_android
    run_test_tc_003_generate_Invalid_QR_android = 1
    # invalid NON-DEP QR
    global run_test_tc_003_generate_invalid_QR_NON_DEP
    run_test_tc_003_generate_invalid_QR_NON_DEP = 1

    global run_test_tc_003_invalid_disable_apps
    run_test_tc_003_invalid_disable_apps = 1

    #search system apps
    global run_test_tc_003_system_apps_limit_10
    run_test_tc_003_system_apps_limit_10 = 1
    global run_test_tc_003_system_apps_limit_50
    run_test_tc_003_system_apps_limit_50 = 1
    global  run_test_tc_003_system_apps_limit_100
    run_test_tc_003_system_apps_limit_100 =1

    #get system apps
    global run_test_tc_003_get_systemapp_10
    run_test_tc_003_get_systemapp_10 = 1
    global run_test_tc_003_get_systemapp_50
    run_test_tc_003_get_systemapp_50 = 1
    global run_test_tc_003_get_systemapp_100
    run_test_tc_003_get_systemapp_100 = 1

   #invalid policy id
    global run_test_tc_003_get_datausage_invalid_policyid_android
    run_test_tc_003_get_datausage_invalid_policyid_android = 1


def sprint20():
    global run_tc_001_admin_login
    run_tc_001_admin_login = 1
    global run_test_001_license_10000
    run_test_001_license_10000 = 1
    global run_test_003_account_get_alert_configs
    run_test_003_account_get_alert_configs = 1
    global run_test_003_policy_get_alert_configs
    run_test_003_policy_get_alert_configs = 1
    global run_test_003_policy_post_alert_configs
    run_test_003_policy_post_alert_configs =1
    global run_test_003_policy_put_alert_configs
    run_test_003_policy_put_alert_configs = 1
    global run_test_tc_003_get_datausage_configs_android
    run_test_tc_003_get_datausage_configs_android = 1
    global run_test_tc_003_get_datausage_invalid_policyid_android
    run_test_tc_003_get_datausage_invalid_policyid_android = 1
    global run_test_tc_003_post_datausage_configs_android
    run_test_tc_003_post_datausage_configs_android = 1
    global run_test_tc_003_generate_QR_android
    run_test_tc_003_generate_QR_android = 1
    global  run_test_tc_003_generate_Invalid_QR_android
    run_test_tc_003_generate_Invalid_QR_android = 1
    global run_test_003_account_post_alert_configs
    run_test_003_account_post_alert_configs = 1
    global run_test_003_account_put_alert_configs
    run_test_003_account_put_alert_configs = 1


def afterlogin_positive():
    global run_tc_001_admin_login
    run_tc_001_admin_login = 1
    global run_tc_001_admin_login_event_logs
    run_tc_001_admin_login_event_logs = 1
    global run_tc_001_admin_config
    run_tc_001_admin_config = 1
    global run_tc_001_prod_version
    run_tc_001_prod_version = 1
    global run_tc_001_help_Text_after_login
    run_tc_001_help_Text_after_login = 1
    global run_tc_001__get_users
    run_tc_001__get_users = 1
    global run_test_001_license
    run_test_001_license = 1
    global run_test_001_bannerNotification_read
    run_test_001_bannerNotification_read = 1

    global run_tc_001_admin_login_invalid_Email
    run_tc_001_admin_login_invalid_Email = 1
    global run_tc_001_admin_login_invalid_Pwd
    run_tc_001_admin_login_invalid_Pwd = 1
    global run_tc_001_admin_login_with_spaces
    run_tc_001_admin_login_with_spaces = 1
    global run_tc_001_admin_login_userName_spaces
    run_tc_001_admin_login_userName_spaces = 1
    global run_tc_001_admin_login_pwd_spaces
    run_tc_001_admin_login_pwd_spaces = 1

    # after login license api negative cases
    global run_test_001_license_100
    run_test_001_license_100 = 1
    global run_test_001_license_1000
    run_test_001_license_1000 = 1


if mycases_negative == 1:
    run_negative_cases()

if mycases_positive == 1:
    run_positive_cases()

if mycases_devices == 1:
    devices()

if mycases_policygroups == 1:
    policygroups()

if mycases_login_after == 1:
    afterlogin_positive()

if mycases_sprint20 == 1:
    sprint20()
