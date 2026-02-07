import requests
from ebird_apikey import ebird_apikey
# original API endpoint "https://api.ebird.org/v2/data/obs/geo/recent/{{speciesCode}}?lat={{lat}}&lng={{lng}}"

def recent_nearby_observations_of_species(apikey):

    enter_species_code = input("Enter bird speciescode: ")

    url = f"https://api.ebird.org/v2/data/obs/geo/recent/{enter_species_code}"

    headers = {
        "x-ebirdapitoken":ebird_apikey
    }

    params = {
        "lat":52.0622531,
        "lng":4.4901218,
        "maxResults":5,
        "dist":50
    }

    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        data = response.json()
        for observations in data:

            print(f"\n"
                  f"Bird species name: {observations['comName']}\n"
                  f"Location: {observations['locName']}\n"
                  f"Amount of birds seen within this area: {observations['howMany']}\n"
                  f"\n")
    else:
        print(f"{response.status_code}, {response.text}")

recent_nearby_observations_of_species(ebird_apikey)