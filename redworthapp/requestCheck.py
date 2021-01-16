import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv

cred = credentials.Certificate(getenv('FIREBASE_ADMIN'))

firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://humidifier-project---redworth-default-rtdb.firebaseio.com/"
})

users_temp_dict = {
    "arav": {
        "devices": {
            "Arav's Humidifier": "off",
            "HUM1": "off"
        }
    },
    "rohit": {
        "devices": {
            "HUM1": "off",
            "Rohit's Humidifier": "off"
        }
    },
    "ted": {
        "devices": {
            "HUM1": "off",
            "taperoll": "off"
        }
    }
}


username = ''


def requestCheck_username(dict_check):
    global username
    if dict_check['username'] in users_temp_dict:
        username = dict_check['username']
        return "Success"
    else:
        return "Failure"


def requestCheck_targetDevice(dict_check):
    global username
    try:
        if dict_check['targetDevice'] in users_temp_dict[username]['devices']:
            return "Success"
        else:
            return 'Failure'
    except:
        return "Failure"


def requestCheck_requestDetails(dict_check):
    # only check if it is NA for no
    if dict_check['requestDetails'] == 'NA':
        return "Success"
    else:
        return "Failure"


def requestCheck_hum_intensity(dict_check):
    intensity = dict_check["targetIntensity"]
    try:
        if 0 <= int(intensity) <= 100 or intensity == 'NA':
            return "Success"

    except:
        return "Failure"
