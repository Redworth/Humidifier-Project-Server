import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv

cred = credentials.Certificate(getenv('FIREBASE_ADMIN'))

#def updateData():
    