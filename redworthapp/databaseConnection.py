import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv

cred = credentials.Certificate(getenv('FIREBASE_ADMIN'))

app = firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://humidifier-project---redworth-default-rtdb.firebaseio.com/"
})

#def updateData():
    