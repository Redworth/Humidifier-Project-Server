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

    check = requestCheck.requestCheckFunc(req_data)

    return f"<h1>{check}</h1>"


@app.route('/app-request/OFF', methods=['GET', 'POST'])
def appRequestOFF():
    req_data = request.get_json()

    check = requestCheck.requestCheckFunc(req_data)

    return f"<h1>{check}</h1>"


@app.route('/app-request/SCH', methods=['GET', 'POST'])
def appRequestSCH():
    req_data = request.get_json()

    check = requestCheck.requestCheckFunc(req_data)

    return f"<h1>{check}</h1>"

