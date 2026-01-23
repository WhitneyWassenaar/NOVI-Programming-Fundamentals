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


        elif start_option == 3:

        else:

start()
