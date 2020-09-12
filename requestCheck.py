#Because most user info will be stored in a database and not as inputs, it makes more sense to use a dictionary as a temporary storage space instead of input.
#So, I am updating your files with the following. I will comment out your input statements for now.

users_temp_dict = {
    "rohit" : {
        "devices" : ["HUM1", "Rohit's Humidifier"]
    },
    "arav" : {
        "devices" : ["HUM1", "Arav's Humidifier"]
    },
    "tal" : {
        "devices" : ["HUM1", "Tal's Humidifier"]
    },
    "ethan" : {
        "devices" : ["HUM1", "Ethan's Humidifier"]
    },
    "ishaan" : {
        "devices" : ["HUM1", "Ishaan's Humidifier"]
    }
}

"""username = input("Enter username: ")
   targetdevice = input("Enter Device: ")
   requestdetails = input('Enter details: ')
   hum_intensity = input("Enter intensity of the humidifier")"""

def requestCheck(dict_check):
    while True:
        if username in  dict_check['username']:
            break
        else
            print("Not Valid Username. Try Again.")

    while True:
        if targetdevice in dict_check['targetDevice']:
            break
        else
            print("Not Valid Device Name. Try Again.")
    while True:
        if requestdetails in  dict_check['requestDetails']:
            break
        else
            print("Not Valid Details. Try Again.")
    while True:
        if 0 <= int(hum_intensity) <= 100 or hum_intensity == 'NA':
            break
        else
            print("Not Valid Intensity. Try Again.")

