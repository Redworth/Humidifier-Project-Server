from apiApp1 import app
from flask import request

@app.route('/app-request/SignIn', methods=['GET', 'POST'])
def appRequestSIGNIN():
    req_data = request.get_json()
    
    try:
        username = req_data['username']
        password = req_data['password']

    except:
        username = "Not found"
        password = "Not found"
    
    return """<h1>Username: {}</h1>
              <h1>Password: {}</h1>""".format(username, password)