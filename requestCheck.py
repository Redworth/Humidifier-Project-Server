import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv
from firebase_init import main_app

users_temp_dict = {}

def refreshOrInitDB():
    global users_temp_dict
    ref = db.reference('/')
    users_temp_dict = ref.get()

refreshOrInitDB()

username = ''

usernameSuccess = ''
targetSuccess = ''
detailsSuccess = ''
intensitySuccess = ''

def requestCheckRegDevice(dict_check):
    new_device_name = dict_check['new_device_name']
    username = dict_check['username']

    userCheck = requestCheckExistingUser(dict_check)

    if userCheck['Result']== "Success":
        try:
            if new_device_name in users_temp_dict[username]['devices']:
                new_device_success = "Failure"
            else:
                new_device_success = "Success"
        except:
            new_device_success = "Success"
    else:
        new_device_success = "Failure"

    return {
        "Result": new_device_success
    }

def requestCheckExistingUser(dict_check):
    username = dict_check['username']
    try:
        if username in users_temp_dict:
            username_success = "Success"
        else:
            username_success = "Failure"
    except:
        username_success = "Failure"

    return {
        "Result": username_success
    }

def requestCheckCreateAccount(dict_check):
    new_username = dict_check['new_username']
    try:
        if new_username in users_temp_dict:
            new_username_success = "Failure"
        else:
            new_username_success = "Success"
    except:
        new_username_success = "Success"

    return {
        "Result": new_username_success
    }

def requestCheckUpdateData(dict_check):
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
        if 0 <= int(intensity) <= 100:
            intensitySuccess = "Success"
        else:
            intensitySuccess = "Failure"

    except:
        intensitySuccess = "Failure"

    if usernameSuccess == "Success" and targetSuccess == "Success" and intensitySuccess == "Success" and detailsSuccess == "Success":
        return {
            "Result": "Success"
        }
    else:
        return {
            "Result": "Failure"
        }

def requestCheckPoll(dict_check):
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
    
    if usernameSuccess == "Success" and targetSuccess == "Success":
        return {
            "Result": "Success"
        }
    else:
        return {
            "Result": "Failure"
        }
