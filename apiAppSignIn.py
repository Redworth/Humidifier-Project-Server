from apiApp1 import app

@app.route('/app-request/SignIn', methods=['GET', 'POST'])
def appRequestSIGNIN():
    req_data = request.get_json()
    
    try:
        username = req_data['username']
        password = req_data['password']

    except:
        username = "Not found"
        password = "Not found"
    
    return """Username: {}
              Password: {}""".format(username, password)