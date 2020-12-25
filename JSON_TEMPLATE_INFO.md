# JSON Template File Explanation

This template is for moving the requests from one end to the other (i.e: phone to server). Use this template to input the values necessary for the request. For example, to turn a person's humidifier named myHumidifier1 on with intensity 80, this would be the JSON for it:

{
    "targetDevice" : "myHumidifier1",
    "requestType" : "hum_on",
    "requestDetails": "NA",
    "targetIntensity" : 80
}
