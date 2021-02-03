import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv
from firebase_init import main_app

ref = db.reference('/')
users_temp_dict = ref.get()

username = ''

usernameSuccess = ''
targetSuccess = ''
detailsSuccess = ''
intensitySuccess = ''

def requestCheckFunc(dict_check):
    global username
    try:
        if dict_check['username'] in users_temp_dict:
            username = dict_check['username']
            usernameSuccess = "Success"
        else:
            usernameSuccess = "Failure"
    except:
        usernameSuccess = "Failure"

    try:
        if dict_check['targetDevice'] in users_temp_dict[username]['devices']:
            targetSuccess = "Success"
        else:
            targetSuccess = 'Failure'
    except:
        targetSuccess = "Failure"

    # only check if it is NA for no
    try: 
        if dict_check['requestDetails'] == 'NA':
            detailsSuccess = "Success"
        else:
            detailsSuccess = "Failure"
    except:
        detailsSuccess = "Failure"

    try:
        intensity = dict_check["targetIntensity"]
    except:
        pass

    try:
        if 0 <= int(intensity) <= 100 or intensity == 'NA':
            intensitySuccess = "Success"
        else:
            intensitySuccess = "Failure"

    except:
        intensitySuccess = "Failure"

    if usernameSuccess == "Success" and targetSuccess == "Success" and intensitySuccess == "Success" and detailsSuccess == "Success":
        return "Success"
    else:
        return "Failure"
