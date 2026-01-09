# ==========================================
# Pizza Price Calculator Exercise
# You work in a pizzeria and must write a program that calculates the cost of a pizza.
# Pizza sizes: Small (S), Medium (M), Large (L)
# Base prices: Small $15, Medium $20, Large $25
# Extra toppings: Pepperoni $2 (S) / $3 (M or L), Extra cheese $1
# ==========================================

# === VERSION 1 ===
# Very redundant, lots of input required
s = 15.00
m = 20.00
l = 25.00
pizza_price = 0.00

order_size = input("Which pizza size would you like? (S, M, L): ").upper()
topping = input("Which topping do you want? (pepperoni, cheese, none): ").lower()
topping_amount = int(input("How many of this topping do you want?: "))
order_amount = int(input("How many pizzas do you want to order?: "))

def calculate_pizza_price(pizza):
    if order_size == "S":
        pizza += 15.00
    elif order_size == "M":
        pizza += 20.00
    elif order_size == "L":
        pizza += 25.00
    else:
        print("Please choose a valid pizza size")

    if topping == "none":
        pizza = pizza
    elif topping == "pepperoni":
        if order_size == "S":
            pizza += 2.00 * topping_amount
        else:
            pizza += 3.00 * topping_amount
    elif topping == "cheese":
        pizza += 1.00 * topping_amount
    else:
        print("Please choose a valid topping")
    return pizza

def total_order(pizza):
    total = order_amount * calculate_pizza_price(pizza)
    return total

total = total_order(pizza_price)
print(f"You ordered {order_amount} pizza(s) with {topping_amount} {topping} topping(s) each. Total: ${total:.2f}")


# === VERSION 2 ===
# Shorter, still redundant, no loops
bill = 0
size = input("Which pizza size? (S, M, L): ").upper()
pepperoni = input("Add extra pepperoni? (yes/no): ").lower()
cheese = input("Add extra cheese? (yes/no): ").lower()

if size == 'S':
    bill += 15
    if pepperoni == 'yes':
        bill += 2
elif size == 'M':
    bill += 20
    if pepperoni == 'yes':
        bill += 3
elif size == 'L':
    bill += 25
    if pepperoni == 'yes':
        bill += 3
else:
    print("No valid pizza size chosen")

if cheese == 'yes':
    bill += 1

print(f"You chose a {size} pizza. Total bill: ${bill}")


# === VERSION 3 ===
# Shorter and structured using separate if's
bill = 0
size = input("Pizza size? (S, M, L): ").upper()
pepperoni = input("Extra pepperoni? (yes/no): ").lower()
cheese = input("Extra cheese? (yes/no): ").lower()

# Size
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("Invalid pizza size")

# Pepperoni
if pepperoni == 'yes':
    if size == 'S':
        bill += 2
    else:
        bill += 3

# Cheese
if cheese == 'yes':
    bill += 1

if size not in ['S', 'M', 'L']:
    print("No pizza ordered")
else:
    print(f"You ordered a {size} pizza. Total: ${bill}")


# === VERSION 4 ===
# Clean, checks toppings per pizza size
bill = 0
size = input("Pizza size? (S, M, L): ").upper()
pepperoni = input("Extra pepperoni? (yes/no): ").lower()
cheese = input("Extra cheese? (yes/no): ").lower()

if size == 'S':
    bill += 15
    if pepperoni == 'yes':
        bill += 2
    if cheese == 'yes':
        bill += 1
elif size == 'M':
    bill += 20
    if pepperoni == 'yes':
        bill += 3
    if cheese == 'yes':
        bill += 1
elif size == 'L':
    bill += 25
    if pepperoni == 'yes':
        bill += 3
    if cheese == 'yes':
        bill += 1
else:
    print("Invalid pizza size")

if size in ['S', 'M', 'L']:
    print(f"{size} pizza ordered. Total: ${bill}")


# === VERSION 5 ===
# Shorter version using .upper() and .lower()
bill = 0
size = input("Pizza size? (S, M, L): ").upper()
pepperoni = input("Extra pepperoni? (yes/no): ").lower()
cheese = input("Extra cheese? (yes/no): ").lower()

if size == 'S':
    bill = 15
    if pepperoni == 'yes':
        bill += 2
    if cheese == 'yes':
        bill += 1
elif size == 'M':
    bill = 20
    if pepperoni == 'yes':
        bill += 3
    if cheese == 'yes':
        bill += 1
elif size == 'L':
    bill = 25
    if pepperoni == 'yes':
        bill += 3
    if cheese == 'yes':
        bill += 1

print(f"{size} pizza ordered. Total bill: ${bill}")


# === VERSION 6 ===
# Cleanest and most readable version
bill = 0
size = input("Pizza size? (S, M, L): ").upper()
pepperoni = input("Extra pepperoni? (yes/no): ").lower()
cheese = input("Extra cheese? (yes/no): ").lower()

# Size
if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25

# Pepperoni
if pepperoni == 'yes':
    if size == 'S':
        bill += 2
    else:
        bill += 3

# Cheese
if cheese == 'yes':
    bill += 1

if size in ['S', 'M', 'L']:
    print(f"Pizza {size} ordered. Total: ${bill}")
else:
    print("No pizza was ordered.")
