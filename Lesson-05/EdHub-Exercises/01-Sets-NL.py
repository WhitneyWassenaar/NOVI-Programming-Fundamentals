# ==========================================
# Voorbeeld Opdracht
# Gegeven is een set met de getallen 1, 2 en 3.
# Voeg het getal 1 toe aan de set en daarna het getal 4.
#
# Print de set 'getallen'.
# Het getal 1 stond al in de set, dus wordt niet nogmaals toegevoegd. Het getal 4 wordt wel toegevoegd.
# ==========================================

# set met getallen
getallen = {1, 2, 3}

# getal 1 en 4 worden toegevoegd aan de set
getallen.add(1)
getallen.add(4)

print('getallen: ', getallen)  # Het resultaat is: {1, 2, 3, 4}


# ==========================================
# Opgave 1:
# Gegeven de verzameling {3, 44, 17, 23, 58, 9, 36}
# Voer de volgende opdrachten uit:
# - Voeg de value 27 aan de verzameling toe.
# - Verwijder de value 23 uit de verzameling.
# - Druk alle values in de verzameling tussen 20 en 50 af. Gebruik hiervoor een for loop.
#
# Verwachte uitkomst: 36, 27, 44
# ==========================================
verzameling = {3,44,17,23,58,9,36}

verzameling.add(27)

print(verzameling)

verzameling.remove(23)

print(verzameling)

for cijfer in verzameling:
    if 20 < cijfer < 50:
        print(cijfer)

# ==========================================
# Opgave 2:
# Gegeven de verzamelingen {red, blue, green} en {yellow, blue, green}
# Zoek uit met behulp van wiskundige verzamelingsoperatoren of methodes:
# - Welke kleur zit wel in verzameling_kleuren_1 maar niet in verzameling_kleuren_2?
# - Welke kleuren zitten niet in beide sets? ('red' en 'yellow')
#
# Print de resultaten.
# ==========================================
rgb = {'red', 'blue', 'green'}
bgy = {'yellow', 'blue', 'green'}


# methode of wiskundige operaties
print(rgb.difference(bgy)) #
print(rgb-bgy)

print(rgb.symmetric_difference(bgy))
print(rgb^bgy)

# ==========================================
# Opgave 3:
# Gegeven de verzamelingen {11, 22, 33} en {5, 11, 16, 22}
# Gebruik wiskundige verzamelingsoperatoren om de volgende verzamelingen te printen:
#     {33}
#     {5, 16}
#     {5, 11, 16, 22, 33}
#     {11, 22}
#
# (LET OP: De volgorde van de values in de verzamelingen is niet belangrijk, die kan namelijk veranderen omdat een set unordered is.)
# ==========================================

nummers_1 = {11, 22, 33}
nummers_2 = {5, 11, 16, 22}

print(nummers_1-nummers_2)
print(nummers_2-nummers_1)
print(nummers_1|nummers_2)
print(nummers_1 & nummers_2)



