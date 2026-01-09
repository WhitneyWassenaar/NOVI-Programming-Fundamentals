# In this exercise, you will write a script where the user has to guess a secret number.
#
# Step-by-step plan:
#
# 1. Create a variable "random_number" and give it a random integer value between 1 and 10.
# 2. Ask the user to guess the number.
# 3. Use a while-loop that continues running as long as the user guesses the wrong number.
# 4. Give feedback if the entered value is too high or too low.
# 5. When the user guesses the correct number, end the loop and print a congratulatory message.
#
# BONUS: Use `import random` and `random.randint(1, 10)` to generate your secret number,
# so it remains hidden from yourself as well.

# === VERSION 1 ===
# Without 'import random', using 'random.randInt(1,10)'
# Here you have to manually adjust random_number

random_number = 6
user_input = int(input('Guess the number between 1 and 10: '))
while user_input != random_number:
    if user_input == random_number:
        print('You guessed the number!')
        break
    elif user_input < random_number:
        print("HIGHER!")
        user_input = int(input('Guess the number: '))
    else:
        print('LOWER!')
        user_input = int(input('Guess the number: '))
else:
    print(f'The number was {random_number}\n'
          f'CONGRATULATIONS!')

# === VERSION 2 ===
# BONUS
# In this code, I use 'import random' and 'random.randint(1,10)'
# In Python, 'random.randInt(1,10)' does NOT work!
# In Python, 'random.randint(1,10)' DOES work!
# Both 1 and 10 are included in random.randint(1,10)
import random

random_number = random.randint(1, 10)
user_input = int(input('Guess the number between 1 and 10: '))
while user_input != random_number:
    if user_input == random_number:
        print('You guessed the number!')
        break
    elif user_input < random_number:
        print("HIGHER!")
        user_input = int(input('Guess the number: '))
    else:
        print('LOWER!')
        user_input = int(input('Guess the number: '))
else:
    print(f'The number was {random_number}\n'
          f'CONGRATULATIONS!')
