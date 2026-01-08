# === LESSON 1: STORYTELLING GAME ===
# English version

# Write a story of approximately 20 – 50 words, using at least 5 variables that the user must fill in.
# Ask the user for input for those variables.
# Example: print("{your_name} walks through the forest and meets {friend_name}. Together they decide to play {sport} under the big {tree_type}.")

name = input("What is your name?: ")
name_friend = input("What is the name of your friend?: ")
amount = int(input("Choose a number between 1 and 10: "))

while amount < 1 or amount > 10 :
    print("You MUST choose a number between 1 and 10!")
    amount = int(input("Choose a number between 1 and 10: "))

ingredient = input("Enter a delicious ingredient to use in a dish: ")
pizza_price = 12.00
total_price = pizza_price * amount
fav_place = input("Enter a location (use a preposition!): ")
discount_total_price = total_price * 0.85
emotion = input("Enter an emotion: ")
food_state = input("Enter the food condition. For example: raw, fresh, spoiled, etc: ")


print(f"{name} plans to order {amount} pizzas with delicious {ingredient} topping together with {name_friend} {fav_place} ! ")
print(f"A single pizza costs ${pizza_price:.2f} so they initially paid ${total_price:.2f}.")
print(f"On the way, they found a 15% discount coupon on the ground. They ordered  {amount} pizzas again and only had to pay ${discount_total_price:.2f}. ")
print(f"In the end, {name} and {name_friend} were very {emotion}. The pizzas were {food_state}.")