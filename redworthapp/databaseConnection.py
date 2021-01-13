import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from decouple import config

cred = credentials.Certificate(config('FIREBASE_ADMIN'))

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://humidifier-project---redworth-default-rtdb.firebaseio.com/'
})

#def updateData():
    