# ==========================================
# Example exercise
# Enter your name using the input() method and then print your name to the console
# ==========================================

name = input('Enter your name: ')  # example input: Bart
print('Your name is: ', name)  # The result is: Your name is: Bart


# ==========================================
# Exercise 1:
# Given the word 'Python', write a program that asks the user for input. If the user enters 'Python', print the boolean True; otherwise, print False.
# ==========================================
word = input('Enter the correct word: ')

if word == 'Python':
    print(True)
else:
    print(False)

# === IT'S MORE FUN WITH A WHILE LOOP ===
password = input('Enter the correct word: ')
while password != 'Python':
    if password == 'Python':
       print('Yes')
    else:
        print('Try again')
        password = input('Enter the correct word: ')
print('This is the correct word, see you next time!')

# ==========================================
# Exercise 2:
# Write a program that asks the user for a number. Then ask for another number and print the sum of the two numbers.

# Expected output when entering the numbers 2 and 3:  The sum of 2 and 3 is: 5
# ==========================================
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))
sum_number = number1 + number2
print(f'The sum of {number1} and {number2} is : {sum_number}')