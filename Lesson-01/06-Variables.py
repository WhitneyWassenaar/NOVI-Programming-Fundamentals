# ==========================================
# Example exercise
# Given is the variable 'age' with the value 25. Print the sentence: 'My age is 25'
# ==========================================

age = 25
print('My age is', age)  # The result is: My age is 25

# ==========================================
# Exercise 1.
# Given a variable 'name' with the value 'Jan' and a variable 'age' with the value 25
# print the sentence 'My name is Jan, and I am 25 years old'. Then change the age to 30.
# and print the sentence again.
#
# Expected output: 'My name is Jan, and I am 25 years old' and 'My name is Jan, and I am 30 years old'
# ==========================================

name = 'Jan'
age = 25

print(f'My name is {name} and I am {age} years old')

age = 30
print(f'My name is {name} and I am {age} years old')

# ==========================================
#Exercise 2.
# Given a few variables. What are their data types if you print them using the type() method?
# Guess the data type first, then check using the print function.
# ==========================================

a = 5 / 5  # float
b = '12'   # string
c = 5 * 5  # int
d = 'Python' * 4  # string

print(type(a), type(b), type(c), type(d))

# ==========================================
# Exercise 3.
# Write good variable names for the following items. Follow Python variable naming conventions.
#
# a. The total number of bananas in a shopping cart
# b. The minimum allowed height for a theme park ride
# c. The largest number in a row of numbers
# ==========================================
# In Python, use snake_case

# === MY ANSWERS ===
# a. total_bananas
# b. min_length
# c. highest_number_in_row

# === IMPLEMENTATION ===
# a.
total_bananas = 0
sum_bananas = 0
# b.
min_height_for_ride = 120
# c.
max_number_in_row = 1000

# There are multiple correct answers possible.
# Use snake_case and keep names descriptive. English is preferred in practice.

# ==========================================
# Exercise 4.
# Given a variable 'counter' with the value 10, increase it by 1 using a compound assignment operator.
# Print the counter. Then decrease the counter by 2 and print it again.
#
# Expected output: 11 and 9
# ==========================================

counter = 10
counter += 1

print(counter)  # Result: 11

counter -= 2
print(counter)  # Result: 9

# ==========================================
# Exercise 5.
# Given variables number_1 = 3 and number_2 = 5, print 'The product of 3 and 5 is 15'
# using the variables in the sentence with an f-string.

number_1 = 3
number_2 = 5
product = number_1 * number_2

print(f'The product of {number_1} and {number_2} is {product}')
