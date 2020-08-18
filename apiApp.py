from flask import Flask, request

app = Flask(__name__)

@app.route('/app-request/ON', methods=['GET', 'POST'])   
def appRequestON():
    req_data = request.get_json()
    
    tarDevice = req_data['targetDevice']
    requestValue = req_data['requestType']
    intensityData = req_data['targetIntensity']
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestValue, intensityData, username)

@app.route('/app-request/OFF', methods=['GET', 'POST'])   
def appRequestOFF():
    req_data = request.get_json()
    
    tarDevice = req_data['targetDevice']
    requestValue = req_data['requestType']
    intensityData = req_data['targetIntensity']
    username = req_data['username']
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestValue, intensityData, username)

