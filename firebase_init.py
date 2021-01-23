from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate("credentials.json")

main_app = firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://humidifier-project---redworth-default-rtdb.firebaseio.com/"
})