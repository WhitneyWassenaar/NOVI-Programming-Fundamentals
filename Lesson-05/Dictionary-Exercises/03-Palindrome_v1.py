# Palindroom:
# Een palindroom is een woord dat hetzelfde is als je het van achter naar voren leest.

# Programmeer een applicatie die controleert of een woord een palindroom is.

woord = input("Voer woord in: ")

if woord == woord[::-1]:
    print("Palindroom")
else:
    print("Geen palindroom")

# bonus 1: maak het hoofdletter ongevoelig

woord = input("Voer woord in: ").lower()

if woord == woord[::-1]:
    print("Palindroom")
else:
    print("Geen palindroom")

# bonus 2: probeer hetzelfde te doen met een zin

zin = input("Voer zin in: ").lower().replace(" ", "")

nieuwe_zin = ""

for letters in zin:
    if letters.isalpha():
        nieuwe_zin += letters

if nieuwe_zin == nieuwe_zin[::-1]:
   print("Palindroom")
else:
    print("Geen palindroom")

# bonus2: DRY

zin = input("Voer zin in: ").lower()

nieuwe_zin = "".join(char for char in zin if char.isalpha()) # join() voegt characters in string die letters zijn

if nieuwe_zin == nieuwe_zin[::-1]:
   print("Palindroom")
else:
    print("Geen palindroom")

# bonus3: SUPER DRY

def palindrome(text):
    text = text.lower()
    text = "".join(c for c in text if c.isalpha())
    return text == text[::-1]

sentence = input("Enter sentence: ")

if palindrome(sentence):
    print("Palindrome")
else:
    print("Not a palindrome")

