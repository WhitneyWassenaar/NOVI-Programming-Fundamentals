# ==========================================
# Example exercise
# Given the string 'Python' and the number 3.
# Use these variables to create the following string: 'Python Python Python' using an operator.
# ==========================================
word = 'Python '
amount = 3

print(word * amount)  # The result is: Python Python Python

# ==========================================
# Exercise 1:
# Create the following sentence in Python: Bello is 4 years old. This is 28 years in human years.
# You have the following variables: age_dog = 4 and in_human_years = 7
# Create a variable called 'human_years' and assign it the value of age_dog multiplied by in_human_years.
# Now write the sentence using the print() method.

# Expected output: Bello is 4 years old. This is 28 years in human years.
# ==========================================
age_dog = 4
in_human_years = 7
human_years = age_dog * in_human_years

print(f'Bello is {age_dog} years old. This is {human_years} years in human years.')

# ==========================================
# Exercise 2:
# What are the data types of the given variables?
# Think of the answer in advance and check it using the print() method that shows the type of the variable.
# ==========================================
variable_one = '5' # string (Because the number is enclosed in quotation marks)
variable_two = 1 / 1 # Float (Because when dividing, the result is always a float)
variable_three = 'Python' * 3 #  # string (Drie keer de string 'Python' blijft alsnog een string)

print(type(variable_one ))
print(type(variable_two ))
print(type(variable_three))

# ==========================================
# Exercise 3:
# Not all variable names are allowed in Python. Some names are reserved for Python itself (keywords).
# Which of the following variable names can you use without getting an error? Think of the answer in advance and check by creating the variables.

# a.     And = ‘something’
# b.     while = ‘something’
# c.     Break = ‘something’
# d.     none = ‘something’
# ==========================================
# === MY ANSWER: NONE OF THEM ===
# In the solution, the variable values are shown between ‘ and ’. Those are typographic quotation marks and cannot be used in Python. Apparently, they were used because it looks “prettier.” You should just use the normal quotation marks like: " or '.
# a.     And = ‘something’    | Impossible
# b.     while = ‘something’  | Impossible
# c.     Break = ‘something’  | Impossible
# d.     none = ‘something’   | Impossible

# === CORRECT ANSWERS ===
# a.     And = 'something'    | Can be used, because in Python 'and' is a keyword. Python is case-sensitive, so 'And' can be used.
# b.     while = 'something'  | Cannot be used, because 'while' is a keyword and is used for while loops in Python.
# c.     Break = 'something'  | Can be used, because 'break' (with a lowercase b) is a keyword in Python, so with an uppercase 'Break' can be used.
# d.     none = 'something'   | Can be used, because 'None' is a keyword in Python, so 'none' (with a lowercase n) can be used.

# === BUT IT'S BETTER NOT TO USE THESE WORDS TO AVOID CONFUSION :) ===
And = 'something'
# while = 'something'
Break = 'something'
none = 'something'

print(And)
print(Break)
print(none)

# ==========================================
# Exercise 4:
# Write a good variable name for:

# A. The total number of a product (bananas)
# B. The minimum allowed height for a ride in an amusement park
# C. The largest number in a sequence of numbers

# Also consider the naming conventions for variable names.
# ==========================================
# In Python, it’s preferable to use snake_case
# === MY ANSWERS ===
# A. total_bananas
# B. min_length
# C. highest_number_in_row

# === SOLUTION ===
# A. total_amount_bananas
# B. min_length_for_attraction
# C. largest_number_in_sequence

# === WHAT HAVE I LEARNED? ===
# Variable names can be longer to clarify their meaning
# A variable name can also be written in Dutch :)

# ==========================================
# Exercise 5:
# Convert the number 3.14 to 3. You may only use the typecast function
# ==========================================
number = 3.14
number = int(number)

print(number)

# === SOLUTION ===
number = 3.14
print(int(number))

# ==========================================
# Exercise  6:
# Given my_variable = 5 and print(my_variable * 3)
# Make sure the output of the print() method is '555' without changing the numeric value of my_variable
# You cannot modify the given code, but you can add extra code
#
# Expected output: 555
# ==========================================
my_variable = 5

print(str(my_variable) * 3)  # Het resultaat is: 555

# === WHAT I LEARNED ===
# From the previous exercise, I learned that you can typecast a variable immediately in a print statement, so I converted the variable to a string to be able to print '555'.

# ==========================================
# Exercise 7:
# Will any of the given print() statements cause an error? Think of the answer in advance and check it by running the code.
# ==========================================

# Remove the # in front of the print statements to test the code.

# print(int('1490.99')) | Impossible

# print(float(12))      | Possible

# print(int('1plus1'))  | Impossible

# print(str(25E10))     | Possible

# === CORRECT ANSWERS ===

# print(int('1490.99')) | Impossible, because an int can be converted to a string, but a float cannot.

# print(float(12))      | Possible, because an int can be converted to a float.

# print(int('1plus1'))  | Impossible, because the string contains a word and cannot be converted to a number.

# print(str(25E10))     | Possible, 25E10 is a scientific notation, that is 250000000000, so it’s an int and an int can be converted to a string.