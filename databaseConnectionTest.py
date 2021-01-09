import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

cred = credentials.Certificate(os.getenv('FIREBASE_CERT'))

firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://humidifier-project---redworth-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')
print(ref.get())

ref = db.reference('/rohit/devices/HUM1')
ref.set('on')

ref = db.reference('/')
print(ref.get())

ref = db.reference('/rohit/devices/HUM1')
ref.set('off')

ref = db.reference('/')
pythonDict = ref.get()

