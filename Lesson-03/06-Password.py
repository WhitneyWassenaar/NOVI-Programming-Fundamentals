# Write a program that asks the user for a password. The user has a maximum of 3 attempts to enter the correct password.
# If the correct password is entered, print a success message and end the loop.
# If the user enters the wrong password 3 times, display an "access denied" message.
#
# Step-by-step plan:
#
# 1. Set a fixed password (for example: "python123") by creating a variable for it.
# 2. Ask the user to enter the password.
# 3. Use a while-loop to give the user a maximum of 3 chances to enter the correct password.
# 4. If the user enters the correct password, end the loop with a success message.
# 5. If the user still enters the wrong password after 3 attempts, display an error message.

#print("passwords")

# === VERSION 1 ===
# BUG: If you enter the correct password, you still get the message: 'Access denied'.
# CAUSE: This is because the last if statement only checks if attempt == 3,
# but it should also check if the password is incorrect, which is not done.

attempt = 0
code = 'python123'

while attempt != 3:
    password = input('Enter password: ')
    attempt += 1

    if password == code:
        print('Welcome')
        break
    else:
        print('Wrong password')

if attempt == 3:
    print('Access denied')

# === VERSION 2 ===
# The code works but is not very neat, because attempt starts at 1 instead of 0.
# It makes more sense to change attempt != 3 to attempt < 3, because you are dealing with a number range.

attempt = 1
code = 'python123'
password = input('Enter password: ')

while password != code:
    if attempt != 3:
        print('Wrong password')
        password = input('Enter password: ')
        attempt += 1
    else:
        print('Access denied')
        break

if password == code:
    print('Welcome')

# === VERSION 3 ===
# Input is underlined in yellow because it is not defined outside the while loop,
# but it is defined inside the while loop. Not sure if this is a big issue.

attempt = 0
max_attempt = 3
password = 'python123'
entry = ""

while attempt < max_attempt:
    entry = input('Enter password: ')

    if entry == password:
        print('Welcome')
        break
    else:
        attempt += 1
        print('Wrong password, try again')

if attempt == max_attempt and entry != password:
    print('Access denied')

# === VERSION 4 ===
# Focus is on the number of attempts. Then it immediately checks if the password is correct.
# If it is correct, attempt is not incremented and the program ends.
# If it is incorrect, attempt increases by 1.

attempt = 0
max_attempt = 3
password = 'python123'

while attempt < max_attempt:
    entry = input('Enter password: ')
    if entry == password:
        print('Welcome')
        break
    else:
        attempt += 1
        print('Wrong password, try again')
else:
    print('Access denied')

# === VERSION 5 ===
# This version shows the user how many attempts they have made.

attempt = 0
max_attempt = 3
password = 'python123'

while attempt < max_attempt:
    entry = input('Enter password: ')
    if entry == password:
        print('Welcome')
        break
    else:
        attempt += 1
        print(f'Wrong password, try again. Attempt {attempt}/{max_attempt}')
else:
    print('Access denied')
