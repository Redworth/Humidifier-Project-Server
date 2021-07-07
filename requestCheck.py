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
