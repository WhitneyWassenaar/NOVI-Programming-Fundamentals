uber_collection ={
    1:"Uber Van",
    2:"Uber Black",
    3:"Uber X"
}

uber_prices = {
    "Uber Van":3.50,
    "Uber Black":2.00,
    "Uber X":1.50
}

USER = {
    "preference":"",
    "history":[]
}

def preference():
    """
    Allows the user to select their preferred Uber service.

    The selected service is stored in USER['preference'].
    :return: None
    """
    print("\n---Preference---\n"
          "Available services\n")

    for service in uber_collection:
        service_name = uber_collection[service]
        price = uber_prices[service_name]
        print(f"[{service}] {uber_collection[service]}: €{price:.2f}")

    while True:
        preference_option = int(input("\nSelect service by entering a number: "))
        if preference_option not in (1, 2, 3):
            print("Invalid service, try again")
            continue
        break

    USER["preference"] = uber_collection[preference_option]
    print(f"\nYour preferred service is now: {USER['preference']}\n")

def history():
    """
     Displays the user's booked ride history.

    Prints the contents of USER['history'] if any rides have been booked.
    If no rides are recorded, informs the user that the history is empty
    """
    if USER["history"] == []:
        print("There is no history, book a ride first\n")

    else:
        for id_ride, booked_ride in enumerate(USER['history'], start=1):
            print(f"-------------------------------\n"
                  f"ID-nummer: {id_ride}\n"
                  f"Service: {booked_ride['Service']}\n"
                  f"Distance: {booked_ride['Distance']} km\n"
                  f"Total price: €{booked_ride['Total price']}\n")

def service_option_from_preference():
    """
     Returns the key corresponding to the user's preferred Uber service.

    This function searches `uber_collection` for the service name stored in
    USER['preference']` and returns the associated key (integer) because
    other functions work with keys instead of service names.

    Example:
        If USER['preference'] = "Uber X", the function returns 3.
    :return: The key of the preferred service in `uber_collection` or None if no math is found
    """
    for key,value in uber_collection.items():
        if value == USER["preference"]:
            return key
    return None # If there is no match, return something, but not nothing

def book_a_ride():
    while True:
        ride_option = int(input("Would you like to book a ride with preferred service or would you  like to select a different service?\n"
                                "[1] Select preferred service\n"
                                "[2] Select a different service\n"
                                "\n"
                                "Enter a number: "))

        if ride_option not in (1,2):
            print("\nInvalid service, try again\n")
            continue

        elif ride_option == 1:
            if USER["preference"] == "":
                print("You did not select a preferred service yet. You can select a preferred service after you choose a different service.\n")
                continue

            else: # You only have to show the already existing preferred service. My mistake was that I thought I had to continue with km, total price in this else statement
                preferred_service = service_option_from_preference()
            print(f"Preferred service selected: {USER['preference']}")
            service_option, km = different_service(preferred_service)
            return service_option, km

        elif ride_option == 2:
            return different_service()

def different_service(preferred_service=None):  # parameter=None, is an optional parameter, not mandatory to fill in parameter

    if preferred_service is not None:
        different_service_option = preferred_service
    else:
        print("---Services---\n")
        for service in uber_collection:
            service_name = uber_collection[service]
            price = uber_prices[service_name]
            print(f"[{service}] {uber_collection[service]}: €{price:.2f}")
        while True:

            different_service_option = int(input("Enter a number: "))
            if different_service_option not in (1,2,3):
                print("Invalid service, try again")
                continue
            break

def start():
    while True:
        start_option = int(input("---Start---\n"
                                 "[1] Change service preference\n"
                                 "[2] View history\n"
                                 "[3] Book a ride\n"
                                 "\n"
                                 "Enter a number: "))
        if start_option == 1:
            preference()
            continue


        elif start_option == 2:
            history()
            continue


        elif start_option == 3:
            service_option, km = book_a_ride()

        else:

start()
