import requests
from ebird_apikey import ebird_apikey

# original API endpoint "https://api.ebird.org/v2/data/obs/geo/recent/{{speciesCode}}?lat={{lat}}&lng={{lng}}"

def comname_to_speciescode(comname,apikey):
    url = "https://api.ebird.org/v2/ref/taxonomy/ebird"

    params = {
        "fmt":"json"
    }

    headers = {
        "x-ebirdapitoken": ebird_apikey
    }

    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        data = response.json()
        for species in data:
            if species['comName'].lower() == comname.lower():
                return species['speciesCode']
        print("Bird species not found")
        return None
    else:
        print(response.status_code)
        return None

def recent_nearby_observations_of_species(species_code,apikey):

    #enter_species_code = input("Enter bird speciescode: ")

    url = f"https://api.ebird.org/v2/data/obs/geo/recent/{species_code}"

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
            if 'howMany' not in observations:
                continue
            print(f"\n"
                  f"Bird species name: {observations['comName']}\n"
                  f"Location: {observations['locName']}\n"
                  f"Amount of birds seen within this area: {observations['howMany']}\n"
                  f"\n")
    else:
        print(f"{response.status_code}, {response.text}")

def main():
    bird_name = input("Enter common bird name: ")
    species_code = comname_to_speciescode(bird_name,ebird_apikey)
    recent_nearby_observations_of_species(species_code,ebird_apikey)
main()
