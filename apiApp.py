from flask import Flask, request

app = Flask(__name__)

@app.route('/app-request/ON', methods=['GET', 'POST'])
def appRequestON():
    req_data = request.get_json()
    
    tarDevice = req_data['targetDevice']
    requestDetails = req_data['requestDetails']
    intensityData = req_data['targetIntensity']
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestDetails, intensityData, username)

@app.route('/app-request/OFF', methods=['GET', 'POST'])   
def appRequestOFF():
    req_data = request.get_json()
    
    tarDevice = req_data['targetDevice']
    requestDetails = req_data['requestDetails']
    intensityData = req_data['targetIntensity']
    username = req_data['username']
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestDetails, intensityData, username)

def appRequestSCH():
    req_data = request.get_json()
    
    tarDevice = req_data['targetDevice']
    requestDetails = req_data['requestDetails']
    intensityData = req_data['targetIntensity']
    username = req_data['username']
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestDetails, intensityData, username)


