<h1>JSON Template File Explanation</h1>

This template is for moving the requests from one end to the other (i.e: phone to server). Use this template to input the values necessary for the request. For example, to turn a person's humidifier named myHumidifier1 on with intensity 80, this would be the JSON for it:

{
    "targetDevice" : "myHumidifier1",
    "requestType" : "hum_on",
    "requestDetails": "NA",
    "targetIntensity" : 80
}

This is conjunction with the URL (in this case the URL is for the movement from phone to server): "redworth-linux-vm-1.westus2.cloudapp.azure.com/app-request/<<string:username>>", where <string:username> is a variable part of the URL that accepts any string. In this case, that string is the username for the person in question.
