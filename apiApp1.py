from flask import Flask, request
import json
import requestCheck
import databaseConnection
from flask_cors import *

app = Flask(__name__)
CORS(app)

import apiAppIOT
import apiAppSignIn

@app.route('/app-request', methods=['GET', 'POST'])
def appRequestON():
    req_data = request.get_json()

    check = requestCheck.requestCheckFunc(req_data)

    jsonReturn = json.dumps(check)

    if check['Result'] == "Success":
        databaseConnection.updateData(req_data['username'], req_data['targetDevice'], req_data['targetIntensity'])

    return jsonReturn
