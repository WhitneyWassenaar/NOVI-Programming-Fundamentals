choose_uber_collection ={
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

menu = {
    1:"Change uber preference",
    2:"View history"
}

#def start(option):
    #if option == 1:
        # check of USER["preference"] is ingevuld
        # Zo ja ga dan verder met km

        # zo niet ga dan naar menu_option == 1

   # elif option ==2:
        # check of USER["history"] gevuld is
        # zo ja, print for items in USER["history"]

        # Zo niet ga naar choose_uber


def preference():
    print("\n---Available ubers---")
    for ubers in choose_uber_collection:
        print(f"{ubers}:{choose_uber_collection[ubers]}")
    choose_preference = int(input("\nEnter number of choice: "))

    USER["preference"] = choose_uber_collection[choose_preference]
    print(f"\nYour preference is now {USER["preference"]}")

def view_history():
    print("---History---")
    for items in USER:
        print(f"{items}:{USER[items]}")

def get_user_choice():
    while True:

        try:
            start_option = int(input("Choose preferred uber or choose different uber?"))

            menu_option = int(input("---Menu---\n"
                                    "[1] Change uber preference\n"
                                    "[2] View history\n"
                                    "\n"
                                    "Enter a number of choice: "))
            if menu_option not in menu:
                print("You can only choose from 1 and 2\n")
                continue

            if menu_option == 1:
                preference()
            elif menu_option == 2:
                view_history()

            choose_uber = int(input("Choose your uber:\n"
                                    "[1] Uber Van  : €3,50 per km\n"
                                    "[2] Uber Black: €2,00 per km\n"
                                    "[3] Uber X    : €1,50 per km\n"
                                    "\n"
                                    "Enter a number of choice: "))

            if choose_uber not in choose_uber_collection: # this statement is True if choose_uber is not in choose_uber_collection, because it's True the program goes to the next if statement, after that, it returns to the while True
                print("You can only choose from 1, 2 and 3")
                continue # Makes it clear that all the if statements in the loop will be skipped, returns back to while True


            if choose_uber in choose_uber_collection:
                while True:
                    km = int(input("Enter distance (whole numbers only): "))
                    if km < 6:
                        print("We do not accept distance smaller than 6 km, try again\n")
                    else:
                        break

                return choose_uber, km # return results to save in tuple


        except ValueError:
            print("Invalid input. Input must be an integer. Try again\n")

def calculate_cost(choice,distance):
    name_uber = choose_uber_collection[choice]
    price = uber_prices[name_uber]
    print(f"You choose: {name_uber}. For distance of {distance} the total price is €{distance * price}")

while True:
    user_choice,distance_in_km = get_user_choice() # results are saved in tuple for example: choose_uber = 1 and km=20, gets stored in  user_choice,distance_in_km (1,20)
    calculate_cost(user_choice,distance_in_km)
