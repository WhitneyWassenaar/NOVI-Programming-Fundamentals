text = "No lemon, no melon!"
leeg = ""

for char in text:
    if char.isalpha():
        leeg += char
print(leeg)

# ---isalpha()---
# Checks if all characters in the text are letters. returns True or False.
# "No lemon, no melon"

word = input("Enter a word: ").lower()
empty = ""

for char in word:
    if char.isalpha():
        empty += char

if empty == empty[::-1]:
    print('Palindrome')
else:
    print('Not palindrome')

# strings support slicing

zin = "lol lol".replace(" ", "")
print(zin)