from flask import Flask, request
import json
from apiAppMobile import app
import databaseConnection

import logging

def process_sync_intent(req_data):
    devices = []

    for i in databaseConnection.getAllDeviceData("rohit"):
        devices.append({
            "id": i,
            "type": 'action.devices.types.HUMIDIFIER',
            "traits": [
                'action.devices.traits.OnOff',
                'action.devices.traits.HumiditySetting',
            ],
            "name": {
                "defaultNames": ['Redworth Humidifier'],
                "name": i,
            },
            "willReportState": False,
            "attributes": {
                "humiditySetpointRange": {
                    "minPercent": 0,
                    "maxPercent": 100,
                },
            },
        })

    app.logger.info(json.dumps({
        "requestId": req_data["requestId"],
        "payload": {
            "agentUserId": "rohit",
            "devices": devices,
        },
    }))

    return {
        "requestId": req_data["requestId"],
        "payload": {
            "agentUserId": "rohit",
            "devices": devices,
        },
    }


def process_query_intent(req_data):
    devices = {}

    for i in req_data['inputs'][0]['payload']['devices']:
        device_intensity = databaseConnection.getData("rohit", i["id"])
        on_status = True if (device_intensity != 0) else False

        devices[i["id"]] = {
            "status": "SUCCESS",
            "online": True,
            "on": on_status,
            "humiditySetpointPercent": device_intensity,
        }

    return {
        "requestId": req_data["requestId"],
        "payload": {
            "devices": devices,
        },
    }

def process_execute_intent(req_data):
    devices = []
    for i in req_data["inputs"][0]["payload"]["commands"][0]["devices"]:
        devices.append(i["id"])
    command = req_data["inputs"][0]["payload"]["commands"][0]["execution"][0]["command"]

    for i in devices:
        if (command == "action.devices.commands.SetHumidity"):
            newIntensity = req_data["inputs"][0]["payload"]["commands"][0]["execution"][0]["params"]["humidity"]
            databaseConnection.updateData("rohit", i, newIntensity)
        elif (command == "action.devices.commands.OnOff"):
            newIntensity = 50 if (req_data["inputs"][0]["payload"]["commands"][0]["execution"][0]["params"]["on"] == True) else 0
            databaseConnection.updateData("rohit", i, newIntensity)

    return {
        "requestId": req_data["requestId"],
        "payload": {
            "commands": [{
                "ids": [i for i in devices],
                "status": "SUCCESS",
                "states": {
                    "online": True,
                    "humiditySetpointPercent": newIntensity,
                    "on": True if (newIntensity != 0) else False,
                },
            }],
        },
    }

@app.route("/intent-webhook", methods=['POST'])
def intent_webhook():
    req_data = request.get_json()
    app.logger.info(json.dumps(req_data))

    if (req_data['inputs'][0]['intent'] == "action.devices.SYNC"):
        return process_sync_intent(req_data)
    elif (req_data['inputs'][0]['intent'] == "action.devices.QUERY"):
        return process_query_intent(req_data)
    elif (req_data['inputs'][0]['intent'] == "action.devices.EXECUTE"):
        return process_execute_intent(req_data)


