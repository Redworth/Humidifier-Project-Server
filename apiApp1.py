from flask import Flask, request
import json
import requestCheck
import databaseConnection

app = Flask(__name__)

import apiApp2
import apiAppSignIn

@app.route('/app-request', methods=['GET', 'POST'])
def appRequestON():
    req_data = request.get_json()

    check = requestCheck.requestCheckFunc(req_data)

    jsonReturn = json.dumps(check)

    if check['Result'] == "Success":
        databaseConnection.updateData(req_data['username'], req_data['targetDevice'], req_data['targetIntensity'])

    return jsonReturn
