UBER_COLLECTION ={
    1:"Uber Van",
    2:"Uber Black",
    3:"Uber X"
}

UBER_PRICES = {
    "Uber Van":3.50,
    "Uber Black":2.00,
    "Uber X":1.50
}

user = {
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

    for service in UBER_COLLECTION:
        service_name = UBER_COLLECTION[service]
        price = UBER_PRICES[service_name]
        print(f"[{service}] {UBER_COLLECTION[service]}: €{price:.2f}")

    while True:
        try:

            preference_option = int(input("\nSelect service by entering a number: "))

            if preference_option not in (1, 2, 3):
                print("Invalid service, try again")
                continue
            break

        except ValueError:
            print("To select a service, enter a number. Other characters are not allowed. Try again.")
            continue

    user["preference"] = UBER_COLLECTION[preference_option]
    print(f"\nYour preferred service is now: {user['preference']}\n")

def history():
    """
     Displays the user's booked ride history.

    Prints the contents of USER['history'] if any rides have been booked.
    If no rides are recorded, informs the user that the history is empty
    """
    if user["history"] == []:
        print("There is no history, book a ride first\n")

    else:
        for id_ride, booked_ride in enumerate(user['history'], start=1):
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
    for key,value in UBER_COLLECTION.items():
        if value == user["preference"]:
            return key
    return None # If there is no match, return something, but not nothing

def book_a_ride():
    while True:
        try:
                ride_option = int(input("Would you like to book a ride with preferred service or would you  like to select a different service?\n"
                                        "[1] Select preferred service\n"
                                        "[2] Select a different service\n"
                                        "\n"
                                        "Enter a number: "))


                if ride_option not in (1,2):
                    print("\nInvalid service, try again\n")
                    continue

                elif ride_option == 1:
                    if user["preference"] == "":
                        print("You did not select a preferred service yet. You can select a preferred service after you booked a ride with a different service.\n")
                        continue

                    else: # You only have to show the already existing preferred service. My mistake was that I thought I had to continue with km, total price in this else statement
                        preferred_service = service_option_from_preference()
                    print(f"Preferred service selected: {user['preference']}")
                    service_option, km = different_service(preferred_service)
                    return service_option, km
        except ValueError:
            print("To select preferred service, enter a number. Other characters are not allowed. Try again.\n")

        else:
            return different_service()



def different_service(preferred_service=None):  # parameter=None, is an optional parameter, not mandatory to fill in parameter

    if preferred_service is not None:
        different_service_option = preferred_service
    else:
        print("---Services---\n")
        for service in UBER_COLLECTION:
            service_name = UBER_COLLECTION[service]
            price = UBER_PRICES[service_name]
            print(f"[{service}] {UBER_COLLECTION[service]}: €{price:.2f}")
        while True:
            try:

                different_service_option = int(input("Enter a number: "))
                if different_service_option not in (1,2,3):
                    print("Invalid service, try again")
                    continue
                break
            except ValueError:
                print("To select a different service, enter a number. Other characters are not allowed. try again.\n")

    while True:
        try:

            km = int(input("Enter km: "))

            if km <=5:
                print("We do not accept distance shorter than 6 km")
                continue
            else:
                break

        except ValueError:
            (print("To select km, enter whole numbers only. Other characters are not allowed. Try again.\n"))
    return different_service_option, km

def total_price(service_option, distance):
    service_name = UBER_COLLECTION[service_option]
    price = UBER_PRICES[service_name]
    total = distance * price
    print(f"Your chosen service: {service_name}\n"
          f"Price per km: €{price:.2f}\n"
          f"Distance: {distance}\n"
          f"Total price: €{total:.2f}\n")
    booked_ride = {
        "Service":service_name,
        "Distance":distance,
        "Total price":total
    }
    user['history'].append(booked_ride)

def start():
    while True:
        try:
            start_option = int(input("---Start---\n"
                                     "[1] Change service preference\n"
                                     "[2] View history\n"
                                     "[3] Book a ride\n"
                                     "\n"
                                     "Enter a number: "))
        except ValueError:
            print("Only numbers are allowed, try again\n")
            continue

        if start_option == 1:
            preference()
            continue


        elif start_option == 2:
            history()
            continue


        elif start_option == 3:
            service_option, km = book_a_ride()
            total_price(service_option, km)

        else:
            print("Invalid number, try again\n")
            continue


start()
