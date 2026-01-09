# ==========================================
# Example Exercise
# Create a list containing the following numbers: 10, 20, and 30
#
# Perform the following tasks:
# - Add the number 40 to (the end of) the list
#
# At the end, print the list 'numbers'.
# ==========================================


# list with numbers
numbers = [10, 20, 30]

# Add the number 40 to (the end of) the list
numbers.append(40)
print('list after adding 40 to the end of the list: ', numbers)  # The result is: [10, 20, 30, 40]


# ==========================================
# Exercise 1:
# Create a list containing the following numbers: 2, 4, 7, 11, and 19
# Perform the following tasks:
# - Add the number 22 to (the end of) the list
# - Add the number 6 between 4 and 7
# - Replace the number 4 with the number 5
# - Print the list 'numbers'
#
# Expected output: [2, 5, 6, 7, 11, 19, 22]
# ==========================================

numbers = [2, 4, 7, 11, 19]
numbers.append(22)
print(numbers)
numbers.insert(2, 6)
print(numbers)
numbers[1] = 5
print(numbers)


# ==========================================
# Exercise 2:
# In the Fibonacci sequence, each number is the sum of the two previous numbers:
# 1, 1, 2, 3, 5, 8, etc.
# The sum of 1 and 1 is 2, the sum of 1 and 2 is 3, and so on.
# Implement the function 'fibonacci', which receives a list as a parameter.
#
# Perform the following tasks:
# - Create a variable called 'fibonacci_start_sequence' and assign it the first two elements of the Fibonacci sequence
# - Create a function called fibonacci that extends the fibonacci sequence with a new element
# - Call the function 5 times (for example, using a for loop)
# - Print the value of the fibonacci sequence
#
# Expected output: [1, 1, 2, 3, 5, 8, 13]
# ==========================================

# === VERSION 1 ===
# The line 'return fibonacci' is incorrect; in this case, you return the function instead of the value.
# Why does the code still work? Because append works and is called inside the for loop,
# but nothing is done with the return value of the function.
# The function itself does not return anything useful.
print('=== VERSION 1 ===')
fibonacci_start_sequence = [1, 1]

def fibonacci(fibonacci_start_sequence):
    fibonacci_start_sequence.append(
        fibonacci_start_sequence[-1] + fibonacci_start_sequence[-2]
    )
    return fibonacci

for i in range(1, 6):
    fibonacci(fibonacci_start_sequence)

print(fibonacci_start_sequence)


# === VERSION 2 ===
# In this version, the function returns the value of the list, which is correct.
# The for loop defines how many times the function is called.
# The return statement is unnecessary here: it is correct, but the returned value is not used.
print('=== VERSION 2 ===')
fibonacci_start_sequence = [1, 1]

def fibonacci(fibonacci_start_sequence):
    fibonacci_start_sequence.append(
        fibonacci_start_sequence[-1] + fibonacci_start_sequence[-2]
    )
    return fibonacci_start_sequence

for i in range(1, 6):
    fibonacci(fibonacci_start_sequence)

print(fibonacci_start_sequence)


# === VERSION 3 ===
# The function modifies the list directly.
# The return statement is not needed in this case.
print('=== VERSION 3 ===')
fibonacci_start_sequence = [1, 1]

def fibonacci(fibonacci_start_sequence):
    fibonacci_start_sequence.append(
        fibonacci_start_sequence[-1] + fibonacci_start_sequence[-2]
    )


for i in range(1, 6):
    fibonacci(fibonacci_start_sequence)

print(fibonacci_start_sequence)


# === VERSION 4 ===
# If you place the print statement outside the for loop, you see the full list at once.
# If you place the print statement inside the for loop, it prints the list during each iteration.
print('=== VERSION 4 ===')
fibonacci_start_sequence = [1, 1]

def fibonacci(fibonacci_start_sequence):
    fibonacci_start_sequence.append(
        fibonacci_start_sequence[-1] + fibonacci_start_sequence[-2]
    )


for i in range(1, 6):
    fibonacci(fibonacci_start_sequence)
    print(fibonacci_start_sequence)


# ==========================================
# Exercise 3:
# Create a list 'squares' that contains the squares of the numbers from 1 to 10.
# Use a for loop.
#
# Expected output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# ==========================================

# === VERSION 1 ===
# I thought this was the correct approach, but 'x' cannot be used because it is not defined

# squares = [x**2 for i in range(1, 11)]
# print(squares)

# === VERSION 2 ===
# 'i' is the value that gets squared
squares = [i**2 for i in range(1, 11)]
print(squares)

# === VERSION 3 ===
# This version follows the original exercise instructions
# You can also use range together with a len() function
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(squares)):
    squares[i] = squares[i] ** 2
print(squares)
