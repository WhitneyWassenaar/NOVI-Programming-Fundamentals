#import requests
import json
#from ebird_apikey import ebird_apikey

#url = "https://api.ebird.org/v2/ref/taxonomy/ebird"
#headers = {
#    "x-ebirdapitoken":ebird_apikey
#}
#params = {
#    "fmt":"json"
#}
#response = requests.get(url,headers=headers, params=params)

#if response.ok:
#    data = response.json()
#    for species in data:
#        if 'yellow-collared chlorophonia' in species['comName'].lower():
#            print(species['comName'])
#else:
#    print(response.status_code, response.text)


#def recent_nearby_observations_of_species(apikey):

#    invoer = input("Enter bird species name: ")

#    url = f"https://api.ebird.org/v2/data/obs/geo/recent/{invoer}"
#    #payload =
#    headers = {
#        "x-ebirdapitoken":ebird_apikey
#    }
#    params = {
#        "lat":52.0622531,
#        "lng":4.4901218,
#        "maxResults":5,
#        "dist":50
#    }

#    response = requests.get(url, headers=headers, params=params)

#    if response.ok:
#        data = response.json()
#        for observations in data:
#            print(f"\n"
#                  f"Bird species name: {observations.get('comName')}\n"
#                  f"Location: {observations.get('locName')}\n"
#                  f"Amount of birds seen within this area: {observations.get('howMany', 'No birds found')}\n"
#                  f"\n")

#    else:
#        print("response.status_code, response.text")

#recent_nearby_observations_of_species(ebird_apikey)


# MENU in tabel
#def print_menu(menu):
#    table_menu = PrettyTable()

#    table_menu.field_names = ["Menu"]
#    table_menu.align["Menu"] = "l"

#    for key,value in menu.items():

#        table_menu.add_row([f"{key} {value}"])

#    print(table_menu)


# ask als je nog een keer wil doen is vervangen door helper functie
#repeat_menu_option = input("Would you like to  search for another bird species? (y/n): ").lower()#

                  #  if repeat_menu_option == "y":
                  #      continue

                   # else:
                    #    break