username = input("Enter username: ")
targetdevice = input("Enter Device: ")
requestdetails = input('Enter details: ')
hum_intensity = input("Enter intensity of the humidifier")

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

