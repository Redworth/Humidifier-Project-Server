from flask import Flask, request, redirect
import json
from apiAppMobile import app
import urllib.parse

import logging

@app.route("/fake-auth")
def fake_auth():
    app.logger.info(request)
    #responseUrl = "%s?code=%s&state=%s".format(urllib.parse())
    return_url = "{}?code={}&state={}".format(request.args.get("redirect_uri"), 'xxxxxx', request.args.get("state"))
    return redirect(return_url)

@app.route("/fake-token", methods=['POST'])
def fake_token():
    app.logger.info(request)

    if (request.args.get("grant_type")):
        grant_type = request.args.get("grant_type") 
    else:
        grant_type = request.form.get("grant_type")
    
    secondsInDay = 86400
    HTTP_STATUS_OK = 200

    if (grant_type == "authorization_code"):
        obj = {
            "token_type": 'bearer',
            "access_token": '123access',
            "refresh_token": '123refresh',
            "expires_in": secondsInDay,
        }
    elif (grant_type == "refresh_token"):
        obj = {
            "token_type": 'bearer',
            "access_token": '123access',
            "expires_in": secondsInDay,
        }
    
    return obj