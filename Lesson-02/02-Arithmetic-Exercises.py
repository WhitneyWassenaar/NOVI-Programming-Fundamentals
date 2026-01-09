# Arithmetic exercises (NL: Reken oefeningen)
### Let Python add 2 numbers and print the result
# Example: 5 + 3 = 8

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
sum_result = num1 + num2
print(f'{num1} + {num2} = {sum_result}')

### Let Python multiply 2 numbers and print the result
# Example: 3 * 4 = 12

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
product = num1 * num2
print(product)

### Now display the result in a string including the numbers and result
print(f'{num1} * {num2} = {product}')

### Let Python calculate the square root (NL: Wortel) of a number and print the result
# Example: The square root of 16 is 4
# Tip: use ** to calculate the root

num1 = int(input('Enter a number: '))
root = num1 ** 0.5
print(root)

### Let Python calculate the remainder (NL: rest) of a division and print the result
# Example: The remainder of 10 / 3 is 1

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
remainder = num1 % num2
print(remainder)

### Create a calculator that adds, subtracts, multiplies, and divides 2 numbers
# Use input to ask for the numbers
# Example input:
# Enter number 1: 5
# Enter number 2: 3
# Output:
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

# === MY SOLUTION ===
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print(f'{num1} + {num2} = {sum_result}')
print(f'{num1} - {num2} = {difference}')
print(f'{num1} * {num2} = {product}')
print(f'{num1} / {num2} = {quotient}')