import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv

cred = credentials.Certificate(getenv('FIREBASE_ADMIN'))

firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://humidifier-project---redworth-default-rtdb.firebaseio.com/"
}, name='demo')

#retrieving data using requestCheck.py
ref = db.reference('/', app='demo')
dataDict = ref.get()

print(dataDict['arav'])
dataDict['arav']['devices']['HUM1'] = 'on'

ref.set(dataDict)


#setting data for databaseConnection.py
ref = db.reference(f'/{username}/devices/{targetDevice}')
ref.set(intensity)
