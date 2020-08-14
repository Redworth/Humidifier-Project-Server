from flask import Flask, request

app = Flask(__name__)

@app.route('/app-request/<string:username>', methods=['GET', 'POST'])   
def appRequest(username):
    req_data = request.get_json()
    
    tarDevice = req_data['targetDevice']
    requestValue = req_data['requestType']
    intensityData = req_data['targetIntensity']
    
    return """Target Device: {}
              Request Value: {}
              Intensity (if needed): {}
              User In Question: {}""".format(tarDevice, requestValue, intensityData, username)

if __name__ == "__main__":
    app.run(debug=True)