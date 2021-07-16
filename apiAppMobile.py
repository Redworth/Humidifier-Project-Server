from flask import Flask, request
import json
import requestCheck
import databaseConnection
from flask_cors import *

app = Flask(__name__)

CORS(app)

import apiAppIOT

@app.route('/app-request', methods=['GET', 'POST'])
def appUpdateRequest():
    req_data = request.get_json()

    check = requestCheck.requestCheckUpdateData(req_data)

    jsonReturn = json.dumps(check)

    if check['Result'] == "Success":
        databaseConnection.updateData(req_data['username'], req_data['targetDevice'], req_data['targetIntensity'])

    return jsonReturn

@app.route('/create-user', methods=['POST'])
def createAccountRequest():
    req_data = request.get_json()

    check = requestCheck.requestCheckCreateAccount(req_data)
    
    jsonReturn = json.dumps(check)

    if check['Result'] == "Success":
        databaseConnection.createNewUser(req_data['new_username'])
        pass
    
    requestCheck.refreshOrInitDB()

    return jsonReturn

@app.route('/register-device', methods=['POST'])
def registerDeviceRequest():
    req_data = request.get_json()

    check = requestCheck.requestCheckRegDevice(req_data)

    jsonReturn = json.dumps(check)

    if check['Result'] == "Success":
        databaseConnection.registerNewDevice(req_data['username'], req_data['new_device_name'])

    requestCheck.refreshOrInitDB()

    return jsonReturn

@app.route('/get-devices-info', methods=['GET'])
def getDevicesInfo():
    req_data = request.get_json()
    
    if req_data == None:
        jsonReturn = {
            "Result": "no_data_sent"
        }
    else:
        check = requestCheck.requestCheckExistingUser(req_data)

        if check['Result'] == 'Success':
            jsonReturn = databaseConnection.getAllDeviceData(req_data['username'])
            no_devices_dict = {
                "no_device": "no_device"
            }
            if jsonReturn == no_devices_dict:
                jsonReturn = {
                    "Result": "no_devices_found"
                }
        else:
            jsonReturn = {
                "Result": "user_not_found"
            }

    return jsonReturn