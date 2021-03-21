import time
import json
import requests

url = "http://redworth-linux-vm-1.westus2.cloudapp.azure.com/iot-poll"

data = json.dumps({
  "username": "rohit",
  "targetDevice": "HUM1",
})
headers = {
  'Content-Type': 'application/json'
}

while True:
  response = requests.request("POST", url, headers=headers, data=data)

  jsonRes = response.json()

  print(jsonRes['intensity'])
  time.sleep(1)