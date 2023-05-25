import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "gGnzy9gRAR4JjSRksNVK2GahhgUrsej0"

while True:
    orig = input("Ciudad de origen: ") 
    if orig == "quit" or orig == "q":
        break
    dest = input("Ciudad de destino: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
	    print("API Status: " + str(json_status) + " = A successful route call.\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
    print("=============================================")
    print("Direccion de " + (orig) + " a " + (dest))
    print("Tiempo Duracion del viaje: " + (json_data["route"]["formattedTime"]))
    print("Kilometros: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    print("=============================================")
    print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    print("=============================================\n")
