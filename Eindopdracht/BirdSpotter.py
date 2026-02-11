import requests
from ebird_apikey import ebird_apikey
from openweather_apikey import openweather_apikey
from datetime import datetime

# original API endpoint "https://api.ebird.org/v2/data/obs/geo/recent/{{speciesCode}}?lat={{lat}}&lng={{lng}}"
def weather(lat,lon, apikey,locname):
    url = f"https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": lat,
        "lon": lon,
        "appid":apikey,
        "units":"metric"
    }

    response = requests.get(url, params=params)

    if response.ok:
        data = response.json()

        weather_description = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        windspeed = data['wind']['speed']
        weather_text = f"The weather in {locname} is {weather_description} with a temperature of {temp}°C, "\
                       f"feels like {feels_like}°C, and a wind speed of {windspeed} m/s."
        print(weather_text)
    else:
        print("Could not fetch weather information")


def filter_data(data_list):
    if not data_list:
        return data_list

    original_list = data_list
    while True:
        print("\n---Filter options---\n"
              "[1] Number of birds\n"
              "[2] Bird species\n"
              "[3] Date\n"
              "[4] Quit")

        try:
            filter_option = int(input("Select a filter option: "))

            filtered_list = original_list

            if filter_option == 1:
                min_birds = int(input("Enter minimum number of birds observed: "))
                filtered_list = [obs for obs in filtered_list if obs['Amount of birds observed'] >= min_birds]
                print(f"{len(filtered_list)} observations remaining after filter.")
            elif filter_option == 2:
                species_name = input("Enter species name: ").lower()
                filtered_list = [obs for obs in filtered_list if obs['Species'].lower() == species_name]
                print(f"{len(filtered_list)} observations remaining after filter.")
            elif filter_option == 3:
                date_str = input("Enter earliest date (YYYY-MM-DD): ")
                date_limit = datetime.strptime(date_str,"%Y-%m-%d").date()
                filtered_list = [obs for obs in filtered_list if datetime.strptime(obs['Date'], "%Y-%m-%d %H:%M").date() >= date_limit]
                print(f"{len(filtered_list)} observations remaining after filter.")
            elif filter_option == 4:
                break
            else:
                print("Invalid option. Please try again.")
                continue

            for obs in filtered_list:
                print(f"\nSpecies:{obs['Species']}\n"
                      f"Scientific name:{obs['Scientific name']}\n"
                      f"Location:{obs['Location']}\n"
                      f"Date:{obs['Date']}\n"
                      f"Amount of birds observed:{obs['Amount of birds observed']}")

        except ValueError:
            print("Enter a valid input.")

    return  filtered_list

def sort_data(data_list):
    if not data_list: # Check of lijst leeg is
        return data_list, 'None' # Als de lijst leeg is, geef lijst en 'None' terug. Lijst moet je teruggeven omdat het programma nog wil sorteren.


    keys = data_list[0].keys()
    available_options = {}
    option_counter = 1

    if 'Species' in keys:
        available_options[option_counter] = 'Species'
        option_counter += 1
    if 'Date' in keys:
        available_options[option_counter] = 'Date'
        option_counter += 1
    if 'Amount of birds observed' in keys:
        available_options[option_counter] = 'Amount of birds observed'
        option_counter += 1

    print("Sort options")
    for key, value in available_options.items():
        print(f"[{key}] Sort {value}")



    while True:
        try:
            sort_option = int(input("\nSelect an option: "))



            if sort_option not in available_options:
                print("Invalid option. Please try again.")
                continue

            chosen = available_options[sort_option]

            if chosen == 'Species':
                data_list.sort(key=lambda dictionary: dictionary['Species'].lower())
                return data_list, 'species'
            elif chosen == 'Date':
                data_list.sort(key=lambda dictionary: datetime.strptime(dictionary['Date'],"%Y-%m-%d %H:%M"))
                return data_list, 'date'

            elif chosen == 'Amount of birds observed':
                data_list.sort(key=lambda dictionary: dictionary['Amount of birds observed'],reverse=True )
                return data_list, 'amount of birds observed'

            return data_list, chosen
        except ValueError:
            print("Enter valid number to select an option. PLease try again")




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

def recent_nearby_observations(lat,lon,max_results,dist_radius):
    url = f"https://api.ebird.org/v2/data/obs/geo/recent/"

    headers = {
        "x-ebirdapitoken": ebird_apikey
    }


    params = {
        "lat": lat,
        "lng": lon,
        "maxResults": max_results,
        "dist": dist_radius,

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
                "Date":observations.get('obsDt', 'Unknown'),
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
                "Date": observations.get('obsDt','Unknown'),
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
                print("\n---Find specific bird---")

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
                weather(lat, lon, openweather_apikey, loc_name)
                obs_list, sort_param = sort_data(obs_list)

                print(f"\n---{obs_count} results---\n"
                          f"You searched for {bird_name} in {loc_name} within a distance radius of {dist_radius} km.")
                for obs in obs_list:
                    print(f"\nLocation: {obs['Location']}\n"
                          f"Date: {obs['Date']}\n"
                              f"Amount of birds observed: {obs['Amount of birds observed']}")

                filter_data(obs_list)

                repeat_menu_option = input("Would you like to  search for another bird species? (y/n): ").lower()
                if repeat_menu_option == "y":
                    continue
                else:
                    break

            if menu_option == 2:

                print("\n---Discover birds nearby---")

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


                nearby_obs_list, nearby_obs_count = recent_nearby_observations(lat, lon, max_results, dist_radius)
                weather(lat, lon, openweather_apikey,loc_name)
                nearby_obs_list, sort_param = sort_data(nearby_obs_list)


                print(f"\n---{nearby_obs_count} results---\n"
                      f"You entered the location: {loc_name} within a distance radius of {dist_radius} km. The results are sorted in {sort_param}")

                for obs in nearby_obs_list:
                    print(f"\nSpecies:{obs['Species']}\n"
                    f"Scientific name:{obs['Scientific name']}\n"
                    f"Location:{obs['Location']}\n"
                    f"Date:{obs['Date']}\n"
                    f"Amount of birds observed:{obs['Amount of birds observed']}")

                filter_data(nearby_obs_list)

                repeat_menu_option = input("Would you like to discover birds again? (y/n): ").lower()
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
                      "and view additional weather information to decide if it's a good time to go birdwatching.\n"
                      "\n"
                      "3.\n"
                      "Use the menu options to repeat searches, return to the main menu, or exit BirdSpotter.")

                break
            if menu_option == 4:
                print("Exiting BirdSpotter. Don’t forget to check back for new bird sightings!")
                return



main()
