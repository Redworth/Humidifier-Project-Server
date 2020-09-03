from apiApp1 import app
from flask import request
import json

@app.route('/app-request/SignIn', methods=['GET', 'POST'])
def appRequestSIGNIN():
    req_data = request.get_json()
    
    try:
        username = req_data['username']
        password = req_data['password']
        returnJsonStr = json.dumps(req_data, indent=4)

    except:
        req_data = {
            "username" : "Error",
            "password" : "Error"
        }
        returnJsonStr = json.dumps(req_data, indent=4)
    
    return returnJsonStr