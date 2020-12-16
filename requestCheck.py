# Because most user info will be stored in a database and not as inputs, it makes more sense to use a dictionary as a temporary storage space instead of input.
# So, I am updating your files with the following. I will comment out your input statements for now.
users_temp_dict = {
    "rohit": {
        "devices": ["HUM1", "Rohit's Humidifier"]
    },
    "arav": {
        "devices": ["HUM1", "Arav's Humidifier"]
    },
    "tal": {
        "devices": ["HUM1", "Tal's Humidifier"]
    },
    "ethan": {
        "devices": ["HUM1", "Ethan's Humidifier"]
    },
    "ishaan": {
        "devices": ["HUM1", "Ishaan's Humidifier"]
    },
    "ted": {
        "devices": ["HUM1", "taperoll"]
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
