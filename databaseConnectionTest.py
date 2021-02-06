import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv
from firebase_init import main_app

#retrieving data using requestCheck.py
ref = db.reference('/')
dataDict = ref.get()

print(dataDict['arav'])
dataDict['arav']['devices']['HUM1'] = 'on'

ref.set(dataDict)


#setting data for databaseConnection.py. variables used below will be set to blank default values before usage.

username = ''
targetDevice = ''
intensity = 0

ref = db.reference(f'/{username}/devices/{targetDevice}')
ref.set(intensity)
