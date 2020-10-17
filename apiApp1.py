import apiApp2
import apiAppSignIn
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/app-request/ON', methods=['GET', 'POST'])
def appRequestON():
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
