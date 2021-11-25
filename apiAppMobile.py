from flask import Flask, request
import json
import requestCheck
import databaseConnection
from flask_cors import *

app = Flask(__name__)

CORS(app)


@app.route('/app-request', methods=['POST'])
def appUpdateRequest():
    try:
        req_data = request.get_json()
        check = requestCheck.requestCheckUpdateData(req_data)
        jsonReturn = json.dumps(check)
        if check['Result'] == "Success":
            databaseConnection.updateData(
                req_data['username'], req_data['targetDevice'], req_data['targetIntensity'])
    except:
        jsonReturn = {
            "Result": "Failure"
        }

    return jsonReturn


@app.route('/create-user', methods=['POST'])
def createAccountRequest():
    try:
        req_data = request.get_json()

        check = requestCheck.requestCheckCreateAccount(req_data)

        jsonReturn = json.dumps(check)

        if check['Result'] == "Success":
            databaseConnection.createNewUser(req_data['new_username'])

        return jsonReturn
    except:
        return {
            "Result": "Failure"
        }


@app.route('/get-users', methods=['POST'])
def existingAccountRequest():
    try:
        req_data = request.get_json()

        check = requestCheck.requestCheckExistingUser(req_data)

        jsonReturn = json.dumps(check)

        return jsonReturn
    except:
        return {
            "Result": "Failure"
        }


@app.route('/register-device', methods=['POST'])
def registerDeviceRequest():
    try:
        req_data = request.get_json()

        check = requestCheck.requestCheckRegDevice(req_data)

        jsonReturn = json.dumps(check)

        if (req_data['register'] == "YES"):
            if check['Result'] == "Success":
                databaseConnection.registerNewDevice(
                    req_data['username'], req_data['new_device_name'])

        return jsonReturn

    except:
        return {
            "Result": "Failure"
        }


@app.route('/get-devices-info', methods=['POST'])
def getDevicesInfo():
    try:
        req_data = request.get_json()
        check = requestCheck.requestCheckExistingUser(req_data)

        if check['Result'] == 'Success':
            jsonReturn = databaseConnection.getAllDeviceData(
                req_data['username'])
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
    except:
        jsonReturn = {
            "Result": "Failure"
        }

    return jsonReturn


@app.route('/specific-device', methods=['POST'])
def appRequestOneDevice():
    try:
        req_data = request.get_json()

        check = requestCheck.requestCheckPoll(req_data)

        if check['Result'] == "Success":
            returnDict = {
                "intensity": ""
            }
            newVal = databaseConnection.getData(
                req_data['username'], req_data['targetDevice'])
            returnDict['intensity'] = newVal

            return json.dumps(returnDict)

        return {
            "Result": "Failure"
        }

    except:
        return {
            "Result": "Failure"
        }
