# Enter 2 numbers and check if they are equal
# Example: 5 and 5 are equal
# Example: 5 and 3 are not equal

num1 = int(input('Enter the first integer: '))
num2 = int(input('Enter the second integer: '))

if num1 == num2:
    print(f'{num1} and {num2} are equal')
else:
    print(f'{num1} and {num2} are not equal')

# Enter 2 numbers and check if num1 is greater than num2
# Example: 5 is greater than 3
# Example: 3 is not greater than 5

num1 = int(input('Enter the first integer: '))
num2 = int(input('Enter the second integer: '))

if num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is not greater than {num2}')

# Enter 2 numbers and check if num1 is less than or equal to num2
# Example: 5 is less than 3 → False
# Example: 3 is less than 5 → True
# Example: 5 is not less than 5 → False

# === MY SOLUTION ===
# I found it more logical to indicate 'greater than' instead of 'not less than'
num1 = int(input('Enter the first integer: '))
num2 = int(input('Enter the second integer: '))

if num1 < num2:
    print(f'{num1} is less than {num2}')
elif num2 < num1:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is equal to {num2}')

# === CORRECT SOLUTION ===
# Here, three numbers are used to show multiple scenarios
num1 = 5
num2 = 5
num3 = 3
print(f"{num1} is less than or equal to {num3} : {num1 < num3}")
print(f"{num3} is less than or equal to {num1} : {num3 < num1}")
print(f"{num1} is less than or equal to {num2} : {num1 <= num2}")

# Check if a string is equal to another string
# Example: John is equal to John
# Example: John is not equal to Doeg

# === MY SOLUTION ===
# I used the example from the previous solution.
# You can place a condition inside curly brackets to check if it is True or False.
john = "John"
doe = "Doe"
print(f'{john} is equal to {john} : {john == john}')
print(f'{john} is not equal to {doe} : {john != doe}')

print(john is doe)