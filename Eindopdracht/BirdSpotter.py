import requests
from ebird_apikey import ebird_apikey
from openweather_apikey import openweather_apikey
from datetime import datetime
from prettytable import PrettyTable

def ask_repeat(prompt="Would you like to discover birds again? (y/n): "):
    """
    Asks if user would like to discover birds again
    :param prompt:
    :return: True or False
    """
    while True:
        answer = input(prompt).lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Invalid input. Enter 'y' or 'n'")

def print_observations_1(obs_list):

    """
    Print a formatted table of bird observations for a bird specific species at a given location and distance. (Menu option 1)
    :param obs_list:
    :return: None
    """
    if not obs_list:
        print("No observations found.")
        return

    table_1 = PrettyTable()
    table_1.field_names = ["Location", "Date", "Amount of birds observed"]

    for obs in obs_list:
       table_1.add_row([obs['Location'], obs['Date'], obs['Amount of birds observed']])

    table_1.align["Location"] = "l"
    table_1.align["Date"] = "l"
    table_1.align["Amount of birds observed"] = "c"

    print(table_1)

def print_observations_2(obs_list):

    """
    Print a formatted table of discovered bird species observations at a given location and distance. (Menu option 2)
    param obs_list:
    :return: None
    """
    table_2 = PrettyTable()
    table_2.field_names = ["Species","Scientific name","Location", "Date", "Amount of birds observed"]

    for obs in obs_list:
        table_2.add_row([obs['Species'],obs['Scientific name'],obs['Location'], obs['Date'], obs['Amount of birds observed']])

    table_2.align["Species"] = "l"
    table_2.align["Scientific name"] = "l"
    table_2.align["Location"] = "l"
    table_2.align["Date"] = "l"
    table_2.align["Amount of birds observed"] = "c"

    print(table_2)

def weather(lat,lon, apikey,loc_name):
    """
     Retrieve and display the current weather information for a given location using the OpenWeatherMap API.

    :param lat:
    :param lon:
    :param apikey:
    :param loc_name:
    :return: None
    """
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
        weather_text = f"  The weather in {loc_name} is {weather_description} with a temperature of {temp}°C, but it feels like {feels_like}°C, and in this location the wind speed is {windspeed} m/s.\n"
        weather_text_frame_top = f" ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗ \n"
        weather_text_frame_bot ="╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ "

        print(weather_text_frame_top,weather_text,weather_text_frame_bot)

    else:
        print("Could not fetch weather information")

def filter_data(data_list, menu_option):
    """
    Interactively filter a list of bird observation data based on user-selected criteria.

    The function provides different filtering options depending on the selected menu context. Users can filter observations by:
    - Minimum number of birds observed
    - Bird species (if available in the dataset)
    - Earliest observation date

    Filtering is applied cumulatively, meaning each new filter is applied to the currently filtered results.

    :param data_list:
    :param menu_option:
    :return: current_list
    """
    if not data_list:
        return data_list

    current_list = data_list

    # All filter options
    available_filter_options = {
        1:"Number of birds",
        2:"Bird species",
        3:"Date",
        4:"Quit"
    }

    if  menu_option == 1:
        available_filter_options = {
            1: "Number of birds",
            2: "Date",
            3: "Quit"
        }

    elif menu_option == 2:
        available_filter_options = {
            1: "Number of birds",
            2: "Bird species",
            3: "Date",
            4: "Quit"
        }

    while True:
        print("\n")
        print(f"╔════════════════════════╗ ")
        print(f"║     Filter options     ║ ")
        print(f"╚════════════════════════╝ ")

        for key,value in available_filter_options.items():
            print(f"[{key}]: {value}")
        try:
            filter_option = int(input("\nSelect a filter option: "))
            if filter_option not in available_filter_options:
                print("Invalid option. PLease try again")
                continue

            filtered_list = current_list

            if filter_option == 1:
                min_birds = int(input("Enter minimum number of birds observed: "))
                filtered_list = [obs for obs in filtered_list if obs['Amount of birds observed'] >= min_birds]
                print(f"\n{len(filtered_list)} observations remaining after filter.")
                current_list = filtered_list

                if menu_option == 1:
                    print_observations_1(current_list)
                else:
                    print_observations_2(current_list)

            elif filter_option == 2:

                if menu_option == 2:
                    species_name = input("Enter species name: ").lower()
                    filtered_list = [obs for obs in filtered_list if obs['Species'].lower() == species_name]
                    print(f"\n{len(filtered_list)} observations remaining after filter.")
                    current_list = filtered_list
                    print_observations_2(current_list)

                else:
                    date_str = input("Enter earliest date (YYYY-MM-DD): ")
                    date_limit = datetime.strptime(date_str, "%Y-%m-%d").date()
                    filtered_list = [obs for obs in filtered_list if datetime.strptime(obs['Date'], "%Y-%m-%d %H:%M").date() >= date_limit]
                    print(f"\n{len(filtered_list)} observations remaining after filter.")
                    current_list = filtered_list
                    print_observations_1(current_list)


            elif filter_option == 3:

                if menu_option == 2:
                    date_str = input("Enter earliest date (YYYY-MM-DD): ")
                    date_limit = datetime.strptime(date_str,"%Y-%m-%d").date()
                    filtered_list = [obs for obs in filtered_list if datetime.strptime(obs['Date'], "%Y-%m-%d %H:%M").date() >= date_limit]
                    print(f"\n{len(filtered_list)} observations remaining after filter.")
                    current_list = filtered_list
                    print_observations_2(current_list)

                else:
                    break

            elif filter_option == 4:
                break

            else:
                print("Invalid option. Please try again.")
                continue

        except ValueError:
            print("Enter a valid input.")

    return  current_list

def sort_data(data_list):
    """
    Interactively sort a list of bird observation data based on user-selected criteria.

    The function displays sorting options depending on the keys present in the first observation dictionary. Users can sort the data by:
    - Species (alphabetically)
    - Date (chronologically)
    - Amount of birds observed (descending)

    :param data_list:
    :return: data_list, chosen
    """
    if not data_list:
        return data_list, 'None'

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

    print("\n")
    print(f"╔══════════════════════╗ ")
    print(f"║     Sort options     ║ ")
    print(f"╚══════════════════════╝ ")

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
    """
    Helper function
    Convert a location name to geographic coordinates using the Nominatim/OpenStreetMap API.(no api key required)

    :param loc_name:
    :return: tuple (lat,lon) else: None if location is not found
    """
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

def comname_to_species_code(comname):
    """
    Helper function
    Retrieve the eBird species code for a given common bird name from eBird API taxonomy endpoint.

    :param comname:
    :return: str (speciesCode) or None of speciesCode does not exist
    """
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
    """
    Retrieve recent bird observations near a specified location from the eBird API.
    :param lat:
    :param lon:
    :param max_results:
    :param dist_radius:
    :return: str: (comName,sciName,locName,obsDt), int: (howMany)
    """
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
    """
       Retrieve recent bird observations near a specified location from the eBird API.
       :param species_code:
       :param lat:
       :param lon:
       :param max_results:
       :param dist_radius:
       :return: str: (locName,obsDt), int: (howMany)
       """

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
    red = "\033[38;5;208m"
    reset = "\033[0m"
    black = "\033[40m"

    menu_options = {
        1:"Find specific bird",
        2:"Discover birds nearby",
        3:"Instructions",
        4:"Quit"
    }

    while True:
        print(f"{black}{red} ╔══════════════════════╗ {reset}"  )
        print(f"{black}{red} ║         Menu         ║ {reset}")
        print(f"{black}{red} ╚══════════════════════╝ {reset}")
        print("Welcome to BirdSpotter!\n"
              "BirdSpotter is your handy command-line companion for discovering bird species worldwide and choosing the perfect time for birdwatching adventures.\n"
              "Please note: BirdSpotter uses data from the eBird community. Observations are contributed by birdwatchers worldwide, so results may vary and are dependent on what users report.\n")

        for key, value in menu_options.items():
            print(f" [{key}] {value} ")

        try:
            menu_option = int(input("\nSelect an option: "))

            if menu_option not in menu_options:
                print("Invalid option, try again")
                continue

        except ValueError:
            print("Only numbers are allowed")
            continue

        while True:

            if menu_option == 1:

                print("\n")
                print(f"{black}{red} ╔═══════════════════════════════════════╗ {reset}")
                print(f"{black}{red} ║          Find specific bird           ║ {reset}")
                print(f"{black}{red} ╚═══════════════════════════════════════╝ {reset}")

                while True:
                    bird_name = input("Enter common bird name: ")
                    species_code = comname_to_species_code(bird_name)

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

                weather(lat, lon, openweather_apikey, loc_name)
                obs_count, obs_list = recent_nearby_observations_of_species(species_code, lat, lon, dist_radius, max_results)

                if obs_count == 0:
                    continue
                else:

                    print(f" ╔══════════════════╗ ")
                    print(f"     {obs_count}   results")
                    print(f" ╚══════════════════╝ ")
                    print(f"You searched for {bird_name} in {loc_name} within a distance radius of {dist_radius} km.")
                    print_observations_1(obs_list)

                    obs_list, sort_param = sort_data(obs_list)
                    print(f"Results sorted by {sort_param}")

                    print_observations_1(obs_list)
                    filter_data(obs_list,menu_option)

                    if not ask_repeat():
                        break

            if menu_option == 2:

                print(f"{black}{red} ╔═══════════════════════════════════════╗ {reset}")
                print(f"{black}{red} ║         Discover birds nearby         ║ {reset}")
                print(f"{black}{red} ╚═══════════════════════════════════════╝ {reset}")

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

                weather(lat, lon, openweather_apikey, loc_name) # weather info
                nearby_obs_list, nearby_obs_count = recent_nearby_observations(lat, lon, max_results, dist_radius) # get observations

                if nearby_obs_count == 0:
                    continue
                else:

                    print(f"\n---{nearby_obs_count} results---\n") # Display raw result
                    print_observations_2(nearby_obs_list)

                    nearby_obs_list, sort_param = sort_data(nearby_obs_list) # sort
                    print(f"Results sorted by {sort_param}")
                    print_observations_2(nearby_obs_list)

                    filter_data(nearby_obs_list,menu_option) # filter

                if not ask_repeat():
                    break

            if menu_option == 3:

                print(f"{black}{red} ╔═══════════════════════════════════════╗ {reset}")
                print(f"{black}{red} ║              Instructions             ║ {reset}")
                print(f"{black}{red} ╚═══════════════════════════════════════╝ {reset}")
                print("\nWelcome to BirdSpotter!\n"
                      "BirdSpotter is your handy command-line companion for discovering bird species worldwide and choosing the perfect time for birdwatching adventures.\n"
                      "\n"
                      "How to use BirdSpotter\n"
                      "\n"
                      f"1. Select preferred search\n"
                      "Select [1] to find a specific bird at a specific location and distance. \n"
                      "Select [2] to discover different kinds of birds in a specific location and distance.\n"
                      "\n"
                      "2. Current weather information\n"
                      "The application provides current weather information of the location you entered in the search, to decide if it's a good time to go birdwatching.\n"
                      "\n"
                      "3. Sort and filter\n"
                      "After results are displayed, you can sort and filter the observations\n"
                      "\n"
                      "3. Repeat, return or quit\n"
                      "Use the menu options to repeat searches, return to the main menu, or exit BirdSpotter.\n")
                print("Press any key to get back to the menu")
                input()
                break

            if menu_option == 4:

                print("\nExiting BirdSpotter. Don’t forget to check back for new bird sightings!")
                return
main()
