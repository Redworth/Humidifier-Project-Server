from flask import Flask, request

app = Flask(__name__)

import apiAppSignIn
import apiApp2

@app.route('/app-request/ON', methods=['GET', 'POST'])
def appRequestON():
    req_data = request.get_json()
    
    try:
        tarDevice = req_data['targetDevice']
        requestDetails = req_data['requestDetails']
        intensityData = req_data['targetIntensity']
        username = req_data['username']

    except:
        tarDevice = "Not Found"
        requestDetails = "Not Found"
        intensityData = "Not Found"
        username = "Not Found"
    
    return """<h1>Target Device: {}</h1>
              <h1>Request Value: {}</h1>
              <h1>Intensity (if needed): {}</h1>
              <h1>User In Question: {}</h1>""".format(tarDevice, requestDetails, intensityData, username)

@app.route('/app-request/OFF', methods=['GET', 'POST'])   
def appRequestOFF():
    req_data = request.get_json()
    
    try:
        tarDevice = req_data['targetDevice']
        requestDetails = req_data['requestDetails']
        intensityData = req_data['targetIntensity']
        username = req_data['username']

    except:
        tarDevice = "Not Found"
        requestDetails = "Not Found"
        intensityData = "Not Found"
        username = "Not Found"
    
    return """<h1>Target Device: {}</h1>
              <h1>Request Value: {}</h1>
              <h1>Intensity (if needed): {}</h1>
              <h1>User In Question: {}</h1>""".format(tarDevice, requestDetails, intensityData, username)

@app.route('/app-request/SCH', methods=['GET', 'POST'])
def appRequestSCH():
    req_data = request.get_json()
    
    try:
        tarDevice = req_data['targetDevice']
        requestDetails = req_data['requestDetails']
        intensityData = req_data['targetIntensity']
        username = req_data['username']

    except:
        tarDevice = "Not Found"
        requestDetails = "Not Found"
        intensityData = "Not Found"
        username = "Not Found"
    
    return """<h1>Target Device: {}</h1>
              <h1>Request Value: {}</h1>
              <h1>Intensity (if needed): {}</h1>
              <h1>User In Question: {}</h1>""".format(tarDevice, requestDetails, intensityData, username)


