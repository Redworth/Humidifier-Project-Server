from apiAppMobile import app
from flask import request
import requestCheck
import databaseConnection
import json

@app.route('/iot-poll', methods=['GET', 'POST'])
def appRequestIOT():
    try:
        req_data = request.get_json()

        check = requestCheck.requestCheckPoll(req_data)

        if check['Result'] == "Success":
            returnDict = {
                "intensity": ""
            }
            newVal = databaseConnection.getData(req_data['username'], req_data['targetDevice'])
            returnDict['intensity'] = newVal

            return json.dumps(returnDict)
        
        return {
            "Result": "Failure"
        }

    except:
        return {
            "Result": "Failure"
        }
