# ==========================================
# Example Exercise
# Given variables a = 3 and b = 10, use an if statement to check if 'a' is greater than 'b'.
# If so, print 'a'. Otherwise, print 'b'.
# ==========================================

a = 3
b = 10

if a > b:
    print(a)
else:
    print(b)

# ==========================================
# Exercise 1:
# Given two integer inputs, number_1 and number_2, write an if statement to check:
# - if number_1 is a multiple of number_2
# - if number_2 is a multiple of number_1
# - or if neither is a multiple of the other
# Place the correct print statement in each branch.
# Example output: 10 is a multiple of 5
# ==========================================

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter another number: "))

if number_1 % number_2 == 0:
    print(f'{number_1} is a multiple of {number_2}')
elif number_2 % number_1 == 0:
    print(f'{number_2} is a multiple of {number_1}')
else:
    print(f'Neither {number_1} nor {number_2} is a multiple of the other')


# ==========================================
# Exercise 2:
# The base price of a cinema ticket is 12 euros.
# - Children under 5 are free
# - Children 5-12 pay half price
# - People aged 13-54 pay full price
# - From 55 years onward, admission is free
# Write a program that prints the ticket price after inputting the age.
# Example output: For age 10, price: 6.0
# ==========================================

age = int(input("Enter your age: "))
ticket = 12.00

if age < 5:
    print(f'You are {age} years old. Admission is free!')
elif 5 <= age <= 12:
    ticket = ticket / 2
    print(f'You are {age} years old. Half price applies: €{ticket:.2f}.')
elif 13 <= age <= 54:
    print(f'You are {age} years old. Full price applies: €{ticket}.')
else:
    print(f'You are {age} years old. Admission is free!')

# Corrected version for edge cases:
age = int(input("Enter your age: "))
price = 12
if age < 5:
    price = 0
elif 5 <= age <= 12:
    price = price / 2
elif 13 <= age <= 54:
    price = price
else:
    price = 0

print(f"For age {age}, the ticket price is: {price}")


# ==========================================
# Exercise 3:
# Write a program that sorts 3 integers. Inputs are stored in variables num1, num2, num3.
# Arrange the smallest in num1, the middle in num2, and the largest in num3.
# Print the variables in order: num1, num2, num3
# Example input: 3 1 2
# Example output: 1 2 3
# ==========================================

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

# === MY SOLUTION ===
# I just couldn't understand why the output wasn't sorted in the correct order.
# Incorrect approach (used elif incorrectly)
if num1 > num2:
    num1, num2 = num2, num1
elif num2 > num3:
    num2, num3 = num3, num2
elif num1 > num3:
    num1, num3 = num3, num1

print(num1, num2, num3)

# === CORRECT SOLUTION ===
# If you use elif in an if-statement, and you have, for example, 3 elifs,
# only the first elif whose condition is True will be executed,
# and the rest will be skipped.

# Correct approach using separate ifs
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num3:
    num1, num3 = num3, num1

print(num1, num2, num3)

# ==========================================
# Exercise 4:
# Given variable 'total' with a value of 0. Repeatedly ask for integer input.
# Add each number to 'total'. When 0 is entered, stop and print the total and the average (total / number of inputs).
# If no numbers were entered, print: "No numbers were entered".
# Example input: 2, 4, 6, 0
# Example output: total: 12, average: 4.0
# ==========================================

total = 0
num_inputs = 0
user_input = int(input('Enter a number: '))

while user_input != 0:
    total += user_input
    num_inputs += 1
    user_input = int(input('Enter a number: '))

if num_inputs != 0:
    average = total / num_inputs
    print(f'Total: {total}, Average: {average}')
else:
    print('No numbers were entered')

# ==========================================
# Exercise 5:
# Ask for an integer input and store it in variable "factor".
# Print the multiplication table for "factor" from 1 to 10.
# Example input: 5
# Example output:
#   1 x 5 = 5
#   2 x 5 = 10
#   ...
#   10 x 5 = 50
# ==========================================

# == MY SOLUTION ===
# Completely wrong, but I thought you could use 'range' like this.
# Here, 'i' represents the counter in the range.
# So if you use range(1, 11), 'i' will take values from 1 to 10.

factor = int(input('Enter an integer: '))

for factor in range(1, 11):
    result = factor * range
    print(f'{range} x {factor} = {result}')

# === SOLUTION ===
factor = int(input('Enter an integer: '))

for i in range(1, 11):
    result = i * factor
    print(f'{i} x {factor} = {result}')
