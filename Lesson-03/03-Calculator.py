# To run a specific version, comment out the rest of the code or copy-paste the specific version in a new file
# ==========================================
# Write a simple calculator. The user must input two numbers and an operation.
# The program should perform the calculation and print the result.
#
# Example:
# Enter the first number: 5.1
# Enter the second number: 3
# Enter the operation: +
# The result is: 8.1
#
# Supported operations: +, -, *, /
# If the user enters an invalid operation, print "Invalid operation".
# ==========================================

# === VERSION 1 ===
# If the user inputs nothing for first_number, they must re-enter
# If the user inputs nothing for second_number, they must start over from first_number
# If the user inputs nothing for operation, they must start over from first_number

while True:
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        multiply = first_number * second_number
        subtract = first_number - second_number
        add = first_number + second_number
        divide = first_number / second_number

        if operation == "*":
            print(f"The result is: {multiply}")
        elif operation == "-":
            print(f"The result is: {subtract}")
        elif operation == "+":
            print(f"The result is: {add}")
        elif operation == "/":
            print(f"The result is: {divide}")
        else:
            print("Invalid operation. Please choose only '+', '*', '-' or '/'")

    except ValueError:
        print("Invalid input. Please enter a number.")


# === VERSION 2 ===
# This version allows the user to retry the same input without starting over

# First number input with error handling
while True:
    try:
        first_number = float(input("Enter the first number: "))
        break
    except ValueError:
        print("You must enter a valid first number.")

# Second number input with error handling
while True:
    try:
        second_number = float(input("Enter the second number: "))
        break
    except ValueError:
        print("You must enter a valid second number.")

# Operation input (always a string, no need for exception handling)
while True:
    operation = input("Enter the operation (+, -, *, /): ")
    if operation in ["*", "/", "+", "-"]:
        break
    else:
        print("Invalid operation. Please enter '+', '-', '*', or '/'.")

# Perform calculation
if operation == "*":
    result = first_number * second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "+":
    result = first_number + second_number
elif operation == "/":
    # Division by zero check
    while True:
        if second_number == 0:
            print("Can't divide by zero.")
            try:
                second_number = float(input("Enter the second number again: "))
            except ValueError:
                print("You must enter a valid number.")
        else:
            result = first_number / second_number
            break

print(f"{first_number} {operation} {second_number} = {result}")


# === SIMPLE VERSION ===
# Basic version without error handling for learning purposes
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print(f"The result is: {first_number + second_number}")
elif operation == "-":
    print(f"The result is: {first_number - second_number}")
elif operation == "*":
    print(f"The result is: {first_number * second_number}")
elif operation == "/":
    print(f"The result is: {first_number / second_number}")
else:
    print("Invalid operation")

