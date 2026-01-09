# Write a program for cashiers where you enter an amount (in cents), for example 87 cents,
# and the program returns how many coins of 50, 20, 10, 5, and 1 cent you should give back.
# The program uses a while-loop to perform the calculation step by step,
# subtracting the largest coin each time until the amount is zero.
#
# Step-by-step plan:
#
# 1. Ask the user to enter an amount in cents (e.g., 87).
#       (Bonus: check if the user does not enter more than 100)
# 2. Use a while-loop to repeatedly subtract the largest coin value from the amount.
#    The loop stops when the amount is zero.
# 3. Inside the while-loop, create (nested) if-statements for each coin value, in which you:
#       - Calculate how many times that coin fits into the amount.
#       - Subtract that coin value that many times from the amount,
#         so the next iteration of the while-loop uses the updated amount.
#       - Print how many coins of this value the user should give back.
#
# Bonus: Extend the program so it can also return bills and euro coins.

# === VERSION 1 ===
# BUG: The word 'coin' or 'coins' is not displayed correctly in the print statement
fifty_cent = 50
twenty_cent = 20
ten_cent = 10
five_cent = 5
one_cent = 1

count_50 = 0
count_20 = 0
count_10 = 0
count_5 = 0
count_1 = 0

user_input = int(input('Enter the number of cents: '))
while user_input <= 0 or user_input > 100:
    print('invalid amount')
    user_input = int(input('Enter the number of cents: '))

while user_input > 0:  # This is correct: as long as user_input > 0, the loop runs; when it is 0, the loop stops
    if user_input >= fifty_cent:
        user_input -= fifty_cent
        count_50 += 1

    elif user_input >= twenty_cent:
        user_input -= twenty_cent
        count_20 += 1

    elif user_input >= ten_cent:
        user_input -= ten_cent
        count_10 += 1

    elif user_input >= five_cent:
        user_input -= five_cent
        count_5 += 1

    elif user_input >= one_cent:
        user_input -= one_cent
        count_1 += 1

# The intention was to show the correct singular or plural form of the word 'coin'.
# In the original code, the variable 'coin' was overwritten repeatedly,
# so only the last check counted. This caused wrong singular/plural usage.
# For example, if you entered 81:
# - 50-cent coins: 1 → correct
# - 20-cent coins: 1 → correct
# - 10-cent coins: 1 → correct
# - 5-cent coins: 0 → 'coin' becomes plural incorrectly
# - 1-cent coin: 1 → still plural due to previous step

coin = 'coin'
plural = 'coins'

# Version 2 fixes this using a function:

def coin_word(amount):
    if amount == 1:
        return 'coin'
    else:
        return 'coins'

print(f'You must give back: \n'
      f'{count_50} {coin_word(count_50)} of 50 cents\n'
      f'{count_20} {coin_word(count_20)} of 20 cents\n'
      f'{count_10} {coin_word(count_10)} of 10 cents\n'
      f'{count_5} {coin_word(count_5)} of 5 cents\n'
      f'{count_1} {coin_word(count_1)} of 1 cent')

# === VERSION 3 ===
# Added bills
fifty_cent = 50
twenty_cent = 20
ten_cent = 10
five_cent = 5
one_cent = 1

one_euro = 100
two_euro = 200

five_euro = 500
ten_euro = 1000
twenty_euro = 2000
fifty_euro = 5000

# Function to handle coins
def coin_word(amount):
    if amount == 1:
        return 'coin'
    else:
        return 'coins'

# Function to handle bills
def bill_word(amount):
    if amount == 1:
        return 'bill'
    else:
        return 'bills'

user_input = int(input('Enter amount in euro cents: '))
while user_input <= 0 or user_input > 1E6:
    print('invalid amount')
    user_input = int(input('Enter amount in euro cents: '))

# Loop through values from largest to smallest
while user_input > 0:
    if user_input >= fifty_euro:
        count_5000 = user_input // 5000
        user_input -= 5000 * count_5000
        print(f'{count_5000} {bill_word(count_5000)} of 50 euros')
    elif user_input >= twenty_euro:
        count_2000 = user_input // 2000
        user_input -= 2000 * count_2000
        print(f'{count_2000} {bill_word(count_2000)} of 20 euros')
    elif user_input >= ten_euro:
        count_1000 = user_input // 1000
        user_input -= 1000 * count_1000
        print(f'{count_1000} {bill_word(count_1000)} of 10 euros')
    elif user_input >= five_euro:
        count_500 = user_input // 500
        user_input -= 500 * count_500
        print(f'{count_500} {bill_word(count_500)} of 5 euros')
    elif user_input >= two_euro:
        count_200 = user_input // 200
        user_input -= 200 * count_200
        print(f'{count_200} {coin_word(count_200)} of 2 euros')
    elif user_input >= one_euro:
        count_100 = user_input // 100
        user_input -= 100 * count_100
        print(f'{count_100} {coin_word(count_100)} of 1 euro')
    elif user_input >= fifty_cent:
        count_50 = user_input // 50
        user_input -= 50 * count_50
        print(f'{count_50} {coin_word(count_50)} of 50 cents')
    elif user_input >= twenty_cent:
        count_20 = user_input // 20
        user_input -= 20 * count_20
        print(f'{count_20} {coin_word(count_20)} of 20 cents')
    elif user_input >= ten_cent:
        count_10 = user_input // 10
        user_input -= 10 * count_10
        print(f'{count_10} {coin_word(count_10)} of 10 cents')
    elif user_input >= five_cent:
        count_5 = user_input // 5
        user_input -= 5 * count_5
        print(f'{count_5} {coin_word(count_5)} of 5 cents')
    elif user_input >= one_cent:
        count_1 = user_input // 1
        user_input -= 1 * count_1
        print(f'{count_1} {coin_word(count_1)} of 1 cent')

# === VERSION 5 ===
# Using a tuple, functions, and a for-loop
coin_and_bill_values = [
    (5000, bill_word, '50 euro'),
    (2000, bill_word, '20 euro'),
    (1000, bill_word, '10 euro'),
    (500, bill_word, '5 euro'),
    (200, coin_word, '2 euro'),
    (100, coin_word, '1 euro'),
    (50, coin_word, '50 eurocent'),
    (20, coin_word, '20 eurocent'),
    (10, coin_word, '10 eurocent'),
    (5, coin_word, '5 eurocent'),
    (1, coin_word, '1 eurocent')
]

user_input = int(input('Enter amount in euro cents: '))
while user_input <= 0 or user_input > 1E6:
    print('invalid amount')
    user_input = int(input('Enter amount in euro cents: '))

print('You must give back: ')
for value, function, name in coin_and_bill_values:    # These 3 values are also in your tuple
    count = user_input // value                       # This is how many times a value fits into the input
    if count > 0:                                     # If the count is greater than 0, then execute the print statement
        print(f'{count} {function(count)} of {name}') # {count} = how many times the value fits into the input,{function(count)} = the tuple already specifies which function to use; the count determines whether the function returns singular or plural,{name} = the name of the coin or bill
        user_input -= count * value                   # This action is performed during each iteration of the for loop
