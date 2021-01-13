from flask import Flask, request
import json
import requestCheck
import databaseConnection

app = Flask(__name__)

import apiApp2
import apiAppSignIn

@app.route('/app-request/ON', methods=['GET', 'POST'])
def appRequestON():
    req_data = request.get_json()

    usernameCheck = requestCheck.requestCheck_username(req_data)
    targetCheck = requestCheck.requestCheck_targetDevice(req_data)
    intensityCheck = requestCheck.requestCheck_hum_intensity(req_data)
    detailsCheck = requestCheck.requestCheck_requestDetails(req_data)

    returnDict = {
        "Username": usernameCheck,
        "Target Device": targetCheck,
        "Intensity": intensityCheck,
        "Other Details": detailsCheck
    }

    if (usernameCheck == "Success" and targetCheck == "Success" and intensityCheck == "Success" and detailsCheck == "Success"):
        databaseConnection.updateData()

    jsonString = json.dumps(returnDict, indent=4)
    return jsonString


@app.route('/app-request/OFF', methods=['GET', 'POST'])
def appRequestOFF():
    req_data = request.get_json()

    try:
        tarDevice = req_data['targetDevice']
        requestDetails = req_data['requestDetails']
        intensityData = req_data['targetIntensity']
        username = req_data['username']
        returnJsonStr = json.dumps(req_data, indent=4)

    except:
        req_data = {
            "username": "Error",
            "targetDevice": "Error",
            "requestDetails": "Error",
            "targetIntensity": "Error"
        }
        returnJsonStr = json.dumps(req_data, indent=4)

    return returnJsonStr


@app.route('/app-request/SCH', methods=['GET', 'POST'])
def appRequestSCH():
    req_data = request.get_json()

    try:
        tarDevice = req_data['targetDevice']
        requestDetails = req_data['requestDetails']
        intensityData = req_data['targetIntensity']
        username = req_data['username']
        returnJsonStr = json.dumps(req_data, indent=4)

    except:
        req_data = {
            "username": "Error",
            "targetDevice": "Error",
            "requestDetails": "Error",
            "targetIntensity": "Error"
        }
        returnJsonStr = json.dumps(req_data, indent=4)

    return returnJsonStr

