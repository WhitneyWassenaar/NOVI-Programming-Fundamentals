import random
int_letters = int(input("How mant letters would you like in your password?"))
int_symbols = int(input("How mant symbols would you like in your password?"))
int_numbers = int(input("How mant numbers would you like in your password?"))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "=", "_", "+", "?", ">", "<", ",", ".", ";",":", "'","`", "~","|"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

password = ""

# Letters, symbols and numbers are next to each other
for i in range(0,int_letters):
    password += random.choice(letters)
for i in range(0,int_symbols):
    password += random.choice(symbols)
for i in range(0,int_numbers):
    password += random.choice(numbers)
print(f"Your password is: {password}")

# Letters, symbols and numbers are shuffled
new_password = []
for i in range(0,int_letters):
    new_password.append(random.choice(letters))
for i in range(0,int_symbols):
    new_password.append(random.choice(symbols))
for i in range(0,int_numbers):
    new_password.append(random.choice(numbers))

random.shuffle(new_password)
print(f"Your improved password is: {"".join(new_password)}")

# ---Notities NL---
# random.randint(a,b) Kies een willekeurig geheel getal tussen a en b (inclusief beide). Werkt alleen met numerieke intervallen, niet met lijsten of strings
# random.choice(seq) Kies een willekeurig element uit een sequentie (list, tuple, string, etc.). Perfect voor wanneer je een letter, symbool of object uit een lijst wilt.