# basic
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

def total_price(choice,distance):

    choice = choose_uber_collection[choice]
    price = uber_prices[choice]
    print(f"You choose {choice} with a price of €{price:.2f} per km. You want to travel {distance} km. The total price is €{price * distance:.2f}\n")


while True:
    try:
        choose_uber = int(input("Choose your uber:\n"
                                "[1] Uber Van  : €3,50 per km\n"
                                "[2] Uber Black: €2,00 per km\n"
                                "[3] Uber X    : €1,50 per km\n"
                                "\n"
                                "Enter a number of choice: "))

        if choose_uber not in choose_uber_collection:
            print("You can only choose from 1, 2 and 3")

        km = int(input("Enter distance (whole numbers only): "))

        if choose_uber in choose_uber_collection:
            total_price(choose_uber, km)

        else:
            print("Invalid input try again\n")

    except ValueError:
        print("Invalid input. Input must be an integer. Try again\n")

