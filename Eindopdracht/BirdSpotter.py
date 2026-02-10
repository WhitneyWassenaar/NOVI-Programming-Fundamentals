import requests
from ebird_apikey import ebird_apikey

# original API endpoint "https://api.ebird.org/v2/data/obs/geo/recent/{{speciesCode}}?lat={{lat}}&lng={{lng}}"
def location_name_to_coordinate(loc_name):
    url = "https://nominatim.openstreetmap.org/search?"

    params = {
        "q":loc_name,
        "format":"json"
    }

    headers = {
        "User-Agent": "BirdSpotter/1.0 (school assignment) using Nominatim/OpenStreetMap API endpoint (contact: user@education.nl)"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    for location in data:
        return location['lat'], location['lon']
    return None

def comname_to_speciescode(comname):
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
        return None
    else:
        print(f"Something went wrong", response.status_code)
        return None

def recent_nearby_observations_of_species(species_code, lat, lon, dist_radius,max_results):

    url = f"https://api.ebird.org/v2/data/obs/geo/recent/{species_code}"

    headers = {
        "x-ebirdapitoken":ebird_apikey
    }

    params = {
        "lat":lat,
        "lng":lon,
        "maxResults":max_results,
        "dist":dist_radius
    }

    response = requests.get(url, headers=headers, params=params)

    obs_count = 0
    obs_list = []

    if response.ok:
        data = response.json()
        found_observation = False


        for observations in data:
            if 'howMany' not in observations:
                continue
            found_observation = True
            obs_count += 1
            obs_list.append({
                "Location": observations['locName'],
                "Date and time": observations.get('obsDt','Unknown'),
                "Amount of birds observed":observations['howMany']
            })


        if not found_observation:
            print("No observations of this species found nearby")

    else:
        print(f"{response.status_code}, {response.text}")
    return obs_count, obs_list

def main():
    print("""                                                                                              
                                                 ███                                                                                            
                                               ██████                                                                                           
                                             ████████                                                                                           
                                            █████████                                                                                           
                                           █████████                                                                                            
                                         ██████████                                                                                             
                                        ██████████                                                                                              
                                     ██████████                                                                                                 
                                  ███████████                                                                                                   
                               ███████████                                                                                                      
                            ████████████                                                                                                        
                          ████████████                                                                                                          
                          ███████████                                                                                                           
                          ██████████                                                                                                            
                         ███████████                                                                                                            
                       █████▓▓▓▓▓▓▓▓███████                                                                                                     
                  █████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                                                                                   
               ███▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████                                                                                                  
          ██▓▓▓▓▓▓█▓▓▓▓▓█████████████████████████                                                                                               
        █▓▓▓▓▓▓▓██████████████████████████████████                                                                                              
    ██▓▓▓▓▓▓███████████████████████████         █                                                                                               
    ██▓▓▓█████████████████████████                                                                                                              
             ███████████                                                                                                                        
            ██████████                                                                                                                          
          ████████████                                                                                                                          
         ████████████  ███████████     ████                 █████    ████████                                                                   
        █████████████    ███   ████                          ████   ███    ██                              ███      ██                          
        ████████████     ███    ███   █████    ██████    ████████   ████   ██    █████████     ███████    ██████  ██████    ██████    ███████   
        ████████████     █████████     ████  ████████   ███  ████    ██████     ██████ ████   ███   ███   ████     ███     ███  ███  ████████   
        ███████████      ███   █████   ████    ███     ███   ████       █████    ████   ████  ██    ████  ████     ███    █████████   ████      
       ████████████      ███    ████   ████    ███     ███   ████          ███   ████   ████ ███    ████  ████     ███    ███         ████      
       ███████████       ███    ████   ████    ███     ████  ████   ██     ███   ████   ███   ███   ████  ████     ███    ████        ████      
       ██████████      ███████████    ██████  █████     ██████████  █████████    █████████     ███████    ██████   █████   ████████  ██████     
       █████████                                          ██           ███       ██████          ███        ██      ██        ██                
      ██████████                                                                 █████                                                          
     ██████████                                                                  █████                                                          
    ██████████                                                                                                                                  
   █████████                                                                                                                                    
   ███████                                                                                                                                      
   ██████                                                                                                                                       
   ███                                                                                                                                          
                                                                                                                                                """
    )


    menu_options = {
        1:"View observed species at a specific location within a given distance"
    }
    while True:
        print("\n---Menu---")
        for key, value in menu_options.items():
            print(f"[{key}] {value}")
        try:
            menu_option = int(input("Select an option: "))

            if menu_option not in menu_options:
                print("Invalid option, try again")
        except ValueError:
            print("Only numbers are allowed")
            continue

        while True:
            if menu_option == 1:
                print("\n---View observed species at a specific location within a given distance---")

                while True:
                    bird_name = input("\nEnter common bird name: ")
                    species_code = comname_to_speciescode(bird_name)
                    if species_code is None:
                        print(f"{bird_name} not found in the eBird database. Please try again.")
                        continue
                    else:
                        break
                while True:
                    loc_name = input("Enter location name: ")
                    coordinates = location_name_to_coordinate(loc_name)

                    if coordinates is None:
                        print(f"{loc_name} not found. Please try again.")
                        continue
                    else:
                        lat,lon = map(float,coordinates)
                        break


                while True:
                    try:
                        dist_radius = int(input("Enter distance radius in km: "))
                        if dist_radius < 1:
                            print("Distance between 1 km and 50 km are accepted. Please try again.")
                            continue
                        elif dist_radius > 50:
                            print("Distance between 1 km and 50 km are accepted. Please try again.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Enter valid number for distance. Please try again.")


                while True:
                    try:
                        max_results = int(input("Enter amount of maximum observations: "))

                        if max_results < 1:
                            print("Enter valid number between 1 and 30. Please try again.")
                            continue
                        elif max_results > 30:
                            print("Enter valid number between 1 and 30. Please try again.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Enter valid number for maximum observations. PLease try again")


                obs_count, obs_list = recent_nearby_observations_of_species(species_code, lat, lon, dist_radius, max_results)
                print(f"\n---{obs_count} results---\n"
                          f"You searched for {bird_name} in {loc_name} within a distance radius of {dist_radius} km.")
                for obs in obs_list:
                    print(f"\nLocation: {obs['Location']}\n"
                          f"Date and time: {obs['Date and time']}\n"
                              f"Amount of birds observed: {obs['Amount of birds observed']}")

                repeat_menu_option = input("Would you like to  search another bird species? (y/n): ").lower()
                if repeat_menu_option == "y":
                    continue
                else:
                    break

main()
