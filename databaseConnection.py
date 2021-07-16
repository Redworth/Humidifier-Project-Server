import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv
from firebase_init import main_app

def updateData(username, device, value):
    ref = db.reference('/' + username + '/devices/' + device)
    ref.set(value)

def getData(username, device):
    ref = db.reference('/' + username + '/devices/' + device)
    return ref.get()

def getAllDeviceData(username):
    ref = db.reference('/' + username + '/devices/')
    return ref.get()

def registerNewDevice(username, new_device_name):

    no_devices_dict = {
        "no_device": "no_device"
    }
    ref = db.reference('/' + username + '/devices/')
    print(ref.get())
    if ref.get() == no_devices_dict:
        ref.set({
            new_device_name : 0
        })
    else:
        ref.update({
            new_device_name : 0
        })

def createNewUser(new_username):
    ref = db.reference('/')

    update_dict = {
        new_username: {
            "devices": {
                "no_device": "no_device"
            }
        }
    }

    ref.update(update_dict)