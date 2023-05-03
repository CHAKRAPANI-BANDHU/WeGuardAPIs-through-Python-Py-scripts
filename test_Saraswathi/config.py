
run_positive =1
run_negative =1
run_wetrack = 1
run_changepassword =1


run_test_tc_00001_licenses = 0
run_test_tc_00002_getWeTrack = 0
run_test_tc_00003_OnlyTrack =0
run_test_tc_00004_TrackwithEventsUrl =0
run_test_tc_00005_getalldevicesper_group = 0
run_test_tc_00006_OnlyTrackinvalidid =0
run_test_tc_00007_OnlyTrackinvalidtrackEnabled =0
run_test_tc_00008_OnlyTrackinvalidpostinterval =0
run_test_tc_00009_OnlyTrackinvalidversion =0
run_test_tc_00010_OnlyTrackinvalidevents =0

run_test_tc_00012_change_password = 0
run_test_tc_00013_invalidconfirmpassword = 0
run_test_tc_00014_invalidnewpassword = 0
run_test_tc_00015_invalidoldpassword = 0
run_test_tc_00016_invalidrequeststring = 0
run_test_tc_00017_invalidusername = 0

def test_run_positive():
    global run_test_tc_00001_licenses
    run_test_tc_00001_licenses = 1

    global run_test_tc_00002_getWeTrack
    run_test_tc_00002_getWeTrack = 1

    global run_test_tc_00003_OnlyTrack
    run_test_tc_00003_OnlyTrack = 1

    global run_test_tc_00004_TrackwithEventsUrl
    run_test_tc_00004_TrackwithEventsUrl = 1

    global run_test_tc_00005_getalldevicesper_group
    run_test_tc_00005_getalldevicesper_group= 1

    # changepassword
    global run_test_tc_00012_change_password
    run_test_tc_00012_change_password =1

def test_run_negative():

    #  Declarations for negative cases for WeTrack

    global run_test_tc_00006_OnlyTrackinvalidid
    run_test_tc_00006_OnlyTrackinvalidid = 1

    global run_test_tc_00007_OnlyTrackinvalidtrackEnabled
    run_test_tc_00007_OnlyTrackinvalidtrackEnabled = 1

    global run_test_tc_00008_OnlyTrackinvalidpostinterval
    run_test_tc_00008_OnlyTrackinvalidpostinterval = 1

    global run_test_tc_00009_OnlyTrackinvalidversion
    run_test_tc_00009_OnlyTrackinvalidversion  = 1

    global run_test_tc_00010_OnlyTrackinvalidevents
    run_test_tc_00010_OnlyTrackinvalidevents = 1



    # Declarations for negative cases for change password

    global run_test_tc_00013_invalidconfirmpassword
    run_test_tc_00013_invalidconfirmpassword = 1


    global run_test_tc_00014_invalidnewpassword
    run_test_tc_00014_invalidnewpassword = 1

    global run_test_tc_00015_invalidoldpassword
    run_test_tc_00015_invalidoldpassword = 1

    global run_test_tc_00016_invalidrequeststring
    run_test_tc_00016_invalidrequeststring = 1

    global  run_test_tc_00017_invalidusername
    run_test_tc_00017_invalidusername = 1


def test_run_wetrack():
    global run_test_tc_00001_licenses
    run_test_tc_00001_licenses = 1

    global run_test_tc_00002_getWeTrack
    run_test_tc_00002_getWeTrack = 1

    global run_test_tc_00003_OnlyTrack
    run_test_tc_00003_OnlyTrack = 1

    global run_test_tc_00004_TrackwithEventsUrl
    run_test_tc_00004_TrackwithEventsUrl = 1

    global run_test_tc_00005_getalldevicesper_group
    run_test_tc_00005_getalldevicesper_group = 1


    global run_test_tc_00006_OnlyTrackinvalidid
    run_test_tc_00006_OnlyTrackinvalidid = 1

    global run_test_tc_00007_OnlyTrackinvalidtrackEnabled
    run_test_tc_00007_OnlyTrackinvalidtrackEnabled = 1

    global run_test_tc_00008_OnlyTrackinvalidpostinterval
    run_test_tc_00008_OnlyTrackinvalidpostinterval = 1

    global run_test_tc_00009_OnlyTrackinvalidversion
    run_test_tc_00009_OnlyTrackinvalidversion = 1

    global run_test_tc_00010_OnlyTrackinvalidevents
    run_test_tc_00010_OnlyTrackinvalidevents = 1





def test_run_changepassword():
    global run_test_tc_00012_change_password
    run_test_tc_00012_change_password = 1

    global run_test_tc_00013_invalidconfirmpassword
    run_test_tc_00013_invalidconfirmpassword = 1

    global run_test_tc_00014_invalidnewpassword
    run_test_tc_00014_invalidnewpassword = 1

    global run_test_tc_00015_invalidoldpassword
    run_test_tc_00015_invalidoldpassword = 1

    global run_test_tc_00016_invalidrequeststring
    run_test_tc_00016_invalidrequeststring = 1

    global run_test_tc_00017_invalidusername
    run_test_tc_00017_invalidusername = 1



if run_wetrack == 1 :
    test_run_wetrack()

if  run_changepassword == 1:
    test_run_changepassword()

if run_negative == 1:
    test_run_negative()

if run_positive == 1:
    test_run_positive()
