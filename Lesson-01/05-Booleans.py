# ==========================================
# Example exercise
# Use the not operator to print the opposite of the boolean value True.
# ==========================================
print(not True)     # The result is: False

# ==========================================
# Exercise 1
# Use logical operators to check if the number 5 is both greater than 3 and less than 10.
# Then check if 5 is greater than 10 or equal to 5.
#
# Expected output: True
# ==========================================
print(10 > 5 > 3)
print(10 < 5 or 5 == 5)

# ==========================================
# Exercise 2
# Evaluate if the number 7 is both greater than 5 and less than 12, and at the same time not equal to 10.
# Print the result.
#
# Expected output: True
# ==========================================
print(12 > 7 > 5 and 7 != 10)

# ==========================================
# Exercise 3
# Given x = 5 and y = -5
# Use logical operators to check if the variables are positive and less than 10. Print the result as a boolean value.
#
# Expected output for x: True
# Expected output for y: False
# ==========================================
x = 5
y = -5

# === MY ANSWER ===
print(10 > x > 0)
print(10 > y > 0)

# === SOLUTION ===
print(x > 0 and x < 10)
print(y > 0 and y < 10)

# Both answers are correct

# ==========================================
# Exercise 5
# Indicate what the result would be for the following code:

# A. print(True or 1 / 0)
# B. print(True or False)
# C. print(False and True and True)
# D. print(True or False or False)
# E. print(not True or False or not True)
# ==========================================

# === MY ANSWERS ===
# True (Because if one of the values is True, Python does not evaluate the rest)
# True (Same logic as above)
# False (With 'and', the result is only True if all are True)
# True (If any value in an 'or' expression is True, the result is True)
# False (Because not True == False, then you have False and again not True == False, so all False)

# ==========================================
# Exercise 6
# Evaluate whether a number is even or odd.
# Create a variable 'number' with the value 42.
# Write the evaluation that determines if the number is even or odd.
# Print 'Even' if it is even, otherwise print 'Odd'.
# Tip: If the number divided by 2 has no remainder, it is even. Otherwise, it is odd.
# ==========================================
number = 42

if number % 2 == 0:
    print('Even')
else:
    print('Odd')

# ==========================================
# Exercise 7
# Greeting based on the time of day
#
# Suppose you have a clock showing 9 a.m. (hour = 9).
# Depending on the time, you want to use an appropriate greeting: "Good morning", "Good afternoon", or "Good evening".
# With conditional expressions you can decide: if the hour is less than 12, say "Good morning"; if less than 18, say "Good afternoon"; otherwise say "Good evening".
# For 9 a.m., the chosen greeting should be "Good morning".
#
# Test the result with the print() method. Change the value of 'hour' to see the greeting change.
# ==========================================
# Morning 06:00 - 12:00
# Afternoon 12:00 - 18:00
# Evening 18:00 - 22:00

hour = 9

if hour >= 6 and hour < 12:
    print('Good morning!')
elif hour >= 12 and hour < 18:
    print('Good afternoon!')
else:
    print('Good evening!')

# Shortened version
hour = 12

if 12 > hour >= 6:
    print('Good morning!')
elif 18 > hour >= 12:
    print('Good afternoon!')
else:
    print('Good evening!')

# Variable assignment version
hour = 21
greeting = 'Good morning!' if 12 > hour >= 6 else 'Good afternoon!' if 18 > hour >= 12 else 'Good evening!'
print(greeting)

# ==========================================
# Exercise 8
# Write a program that asks the user to enter 2 numbers. Print the sum and the product of the numbers.
# The input function should ask: 'Enter the first number:' and 'Enter the second number:'
# Make sure the input can also accept decimal numbers.
#
# Expected output when entering 2 and 3: The sum of 2 and 3 is: 5
# ==========================================
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

print('The sum of', num1, 'and', num2, 'is:', (num1 + num2))

# Using a variable
sum_ = num1 + num2
print('The sum of', num1, 'and', num2, 'is:', sum_)

# Using f-string
print(f'The sum of {num1} and {num2} is: {sum_}')


# ==========================================
# Demonstration of short-circuit evaluation
# 1/0 would cause ZeroDivisionError, but because of short-circuiting Python never actually evaluates it.
print(True or 1 / 0)
