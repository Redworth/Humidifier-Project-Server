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