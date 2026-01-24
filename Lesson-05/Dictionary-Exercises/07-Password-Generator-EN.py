import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '_', '-', '=']

password = ""

int_letters = int(input("Hoeveel letters wil je in je wachtwoord?: "))
int_symbols = int(input("Hoeveel symbolen wil je in je wachtwoord?: "))
int_numbers = int(input("Hoeveel nummers wil je in je wachtwoord?: "))

for i in range(0,int_letters):
    password += random.choice(letters)
for i in range(0,int_symbols):
    password += random.choice(symbols)
for i in range(0,int_numbers):
    password += random.choice(numbers)
print(f"Jouw nieuwe wachtwoord is: {password}")

password = list(password)
random.shuffle(password)
print("".join(password))

# ---Notes---
# random.randint(a, b) Choose a random integer between a and b (inclusive). Works only with numeric ranges, not with lists or strings.
# random.choice(seq) Choose a random element from a sequence (list, tuple, string, etc.).Perfect for when you want a letter, symbol, or object from a list.
# random.shuffle() changes the order of items in a list.
