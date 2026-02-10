import requests
from ebird_apikey import ebird_apikey
from datetime import datetime

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

def recent_nearby_observations(lat,lon,max_results,dist_radius,sort_param):
    url = f"https://api.ebird.org/v2/data/obs/geo/recent/"

    headers = {
        "x-ebirdapitoken": ebird_apikey
    }


    params = {
        "lat": lat,
        "lng": lon,
        "maxResults": max_results,
        "dist": dist_radius,
        "sort": sort_param
    }

    response = requests.get(url, headers=headers, params=params)
    nearby_obs_list = []
    nearby_obs_count = 0
    if response.ok:
        data = response.json()
        found_observation = False
        for observations in data:
            if 'howMany' not in observations:
                continue
            found_observation = True
            nearby_obs_count += 1
            nearby_obs_list.append({
                "Species":observations['comName'],
                "Scientific name":observations['sciName'],
                "Location":observations['locName'],
                "Date and time":observations.get('obsDt', 'Unknown'),
                "Amount of birds observed":observations['howMany']
            })
        if not found_observation:
            print("No observations of this species found nearby")
    return nearby_obs_list, nearby_obs_count






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
        1:"Find specific bird",
        2:"Discover birds nearby",
        3:"Instructions",
        4:"Quit"
    }

    while True:
        print("\n---Menu---")
        for key, value in menu_options.items():
            print(f"[{key}] {value}")

        try:
            menu_option = int(input("\nSelect an option: "))

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

            if menu_option == 2:

                print("\n---Discover bird species nearby---")

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

                while True:
                    try:
                        sort_option = int(input("Would you like to sort the results in date and time or species?\n"
                                                "[1] Species\n"
                                                "[2] Date and time\n"
                                                "\n"
                                                "Select an option: "))

                        if sort_option not in (1,2):
                            print("Invalid option, select option 1 or 2. Please try again.")
                            continue
                        elif sort_option == 1:
                            sort_param = "species"
                            break
                        elif sort_option == 2:
                            sort_param = "date"

                            break
                        else:
                            break
                    except ValueError:
                        print("Enter valid number to select an option. PLease try again")

                nearby_obs_list, nearby_obs_count = recent_nearby_observations(lat, lon, max_results, dist_radius,sort_param)
                if sort_param == "species":
                    nearby_obs_list.sort(key=lambda dictionary: dictionary['Species'].lower())
                elif sort_param == "date":
                    nearby_obs_list.sort(key=lambda dictionary: datetime.strptime(dictionary['Date and time'], "%Y-%m-%d %H:%M"))

                print(f"\n---{nearby_obs_count} results---\n"
                      f"You entered the location: {loc_name} within a distance radius of {dist_radius} km. The results are sorted in {sort_param}")
                for obs in nearby_obs_list:
                    print(f"\nSpecies:{obs['Species']}\n"
                    f"Scientific name:{obs['Scientific name']}\n"
                    f"Location:{obs['Location']}\n"
                    f"Date and time:{obs['Date and time']}\n"
                    f"Amount of birds observed:{obs['Amount of birds observed']}")

                repeat_menu_option = input("Would you like to search for bird species based on location again? (y/n): ").lower()
                if repeat_menu_option == "y":
                    continue
                else:
                    break

            if menu_option == 3:
                print("\n---Welcome to BirdSpotter!---\n"
                      "BirdSpotter is your handy command-line companion for discovering bird species worldwide and choosing the perfect time for birdwatching adventures.\n"
                      "\n"
                      "How to use BirdSpotter\n"
                      "\n"
                      "1.\n"
                      "Select [1] to find a specific bird at a specific location and distance. \n"
                      "Select [2] to discover different kinds of birds in a specific location and distance.\n"
                      "\n"
                      "2. \n"
                      "After results are displayed, you can sort and filter the observations, "
                      "or view additional weather information to decide if it's a good time to go birdwatching.\n"
                      "\n"
                      "3.\n"
                      "Use the menu options to repeat searches, return to the main menu, or exit BirdSpotter.")

                break
            if menu_option == 4:
                print("Exiting BirdSpotter. Don’t forget to check back for new bird sightings!")
                return



main()
