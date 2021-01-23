import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from os import getenv

cert_dict = {
  "type": "service_account",
  "project_id": "humidifier-project---redworth",
  "private_key_id": "8c13851320b7b642ca871d46e73416fa68c5b760",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCXyLkITf8AR21j\nQMrn4HomgI7YRfVuxeBK08nvq6cHcLXqN/Umu/0SYeGRDmPB/i/SZHectpU1hAsB\n2vDNe9p4bS+BG3KCADLK4Adb40NIinK7dJp5OYwxDuFs/sqj+09PlxUcI2UrHljv\nhd6Yt5LwzF52aZh3RqgJu6a6Ji0t0w7DEcLqpWwiMl9b2+kp/2cjCn9Rxo/Ru27L\ndvGoqFylHqMzgeS+3XD5HccI8l1OIdsJFfi7khazxbdhmJICacff/FPLzYrVVsFa\nCZGqXbG7mdOFzt+nvzJMlCqKuGGTqoWzn6alr4o9OuqmhYhJXOsy25TfVBSJpreW\nW+dn+wqzAgMBAAECggEASKMLQZkp1nVYOO5x6+O2MSTGt2NLYBacDtMpyWOpDFt5\nAzyCOmYuZxSmgOeU/+pn8lSYFUwfPbwSFHI1WPDTjVwbJrr+4o27wPDTNLseoOF4\npJLZtfe/Sl7nrGSGj1EeFGWl+ZBKwwbD4uR6sTTwwgHblulTyIjss7O0x1KrvkiN\nEJIyaXNCiGTkE+HbKWxzcpc0tM41Hr6knnQMQ44LdlUSF6gsAI8h1NNKVx7UvuyQ\nVG+Veb8pIUjfkiqA1T4+yAGbdmVVyG6EoFvBmr/OImffRG/s9fGMZJs2xpN1XjpT\npksgOcnUSmLl4YKHFhZrfn/mUWydltOXpGB8UJoBmQKBgQDIAkrrHR4STQLAtOJd\nu5WD5igLIu+GL+YD4JQzCw5QHmotblIrGY3EMpuUeFbBtg7/LexfxYNMdalVdPfE\nsJ5YSeQ73kVxpK6iPqBL9CvNHq3khVYXzfshmPIG5XZGW8iDb/J+P9QzTmQiKlbv\n5mw0GrotT9WWSpspK92Rt068jwKBgQDCRmDNzGvaBOzIDeE4V9TI2zkpV09vVDXa\nvA9tp7qXtbVUeDQxXfpqIQu+AFF1+7oW+AR/7qpgSjlWBeo3Je/ffe4TzDCFinEM\nezYPqexfxE44groml/rycS14QFwe4K1nEvsY3Yjhq0CIu5W5L722FTBTuRlNfw3J\n/G30g9mpnQKBgQCKsPRMhvtkS1yeTpAt2Tb7qKyZ1Fbt4OcKRz/dCUyaiAyuhjKa\nSnUA2OsDkFLwrpNFpg2j961tZqXOaXaqQKL8q/iE/0N+Y2jpfq3fHWkGKsEAluk1\nRpNfH9SsrY9PiLPJWOZ5Xz+BeFl9S4jPgCQGGYaChzqfpgpkCVPyiH8jxwKBgAn0\nTTV+SfBr3C4L+ARJC9AW24DwxlMv/2prxGab94Wae+YOGq6E4DXb55werA3djhVr\nM9/SPMyeQP3VY8DbosTS0QYWqk3NYCmBjq2SyVfG2TMwD5W2p9cQUYId2hqC7J+h\na1hE0aSuf6oB4pQQjCnuQAGqNE+yOOSmmIO01cxJAoGBALbA0PODhpdkYnoAevmw\njDXrkwUvhf/K26SYKdZVJalt42uCbvZ+/vosT4wCOVJ337A7Wm6kuvq+F1da4KoR\n5lxae3Oxlp/K38T41/dB5bGBFgEh6mqojugcoH+ZePFNl7gtBwzYv/n3inZvie+z\n+mXrBp1HhEdtUoCfiFE9wShv\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-cwmf6@humidifier-project---redworth.iam.gserviceaccount.com",
  "client_id": "100802438235452884402",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-cwmf6%40humidifier-project---redworth.iam.gserviceaccount.com"
}

cred = credentials.Certificate(cert_dict)

firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://humidifier-project---redworth-default-rtdb.firebaseio.com/"
})

users_temp_dict = {
    "arav": {
        "devices": {
            "Arav's Humidifier": "off",
            "HUM1": "off"
        }
    },
    "rohit": {
        "devices": {
            "HUM1": "off",
            "Rohit's Humidifier": "off"
        }
    },
    "ted": {
        "devices": {
            "HUM1": "off",
            "taperoll": "off"
        }
    }
}


username = ''


def requestCheck_username(dict_check):
    global username
    if dict_check['username'] in users_temp_dict:
        username = dict_check['username']
        return "Success"
    else:
        return "Failure"


def requestCheck_targetDevice(dict_check):
    global username
    try:
        if dict_check['targetDevice'] in users_temp_dict[username]['devices']:
            return "Success"
        else:
            return 'Failure'
    except:
        return "Failure"


def requestCheck_requestDetails(dict_check):
    # only check if it is NA for no
    if dict_check['requestDetails'] == 'NA':
        return "Success"
    else:
        return "Failure"


def requestCheck_hum_intensity(dict_check):
    intensity = dict_check["targetIntensity"]
    try:
        if 0 <= int(intensity) <= 100 or intensity == 'NA':
            return "Success"

    except:
        return "Failure"
