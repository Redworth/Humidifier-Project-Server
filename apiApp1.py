from flask import Flask, request

app = Flask(__name__)

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
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestDetails, intensityData, username)

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
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestDetails, intensityData, username)

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
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestDetails, intensityData, username)


