# De 7 coördinaten vormen een woord van 7 letters
# Ontcijfer elk coördinaat één voor één tot een letter uit de puzzel lijst
# Sla jouw ontcijferde letters op in de "antwoord" variabele
# (tip: bekijk een woord als een lijst van letters)

#Print je antwoord uit:

# === VERSIE 1 ===
# Ik dacht dat het een goed idee zou zijn om de 2 parameters 'index' en 'letter' te noemen, maar niets verwijst nog naar een item in de puzzel lijst

puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0,0), (2,0), (0,-2),(1,3),(0,3),(2,4),(1,-1)]

antwoord = []

for index, letter in coordinaten:
    antwoord.append(letter)

print(antwoord)

# === VERSIE 2 ===
# variabele 'woord': dat is de eerste cijfer van de coördinaat, dus 0
# variabele 'coordinaten': dat is de tweede cijfer van de coördinaat, dus 1
# Maar als ik de lijst 'antwoord' print, dan krijg ik alleen maar coördinaten te zien

puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0, 0), (2, 0), (0, -2), (1, 3), (0, 3), (2, 4), (1, -1)]

antwoord = []

for index, letter in coordinaten:
    woord = coordinaten[0]
    letter = coordinaten[1]

    antwoord.append(letter)

print(antwoord)

# === VERSIE 3 ===
# IndexError: list index out of range
# letter = puzzel[letter], maar bijvoorbeeld (2,4) kan niet, want de lijst puzzel gaat maar tot 3.
# letter wordt zowel als variabele en als parameter gebruikt, dat klopt niet
#puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
#coordinaten = [(0, 0), (2, 0), (0, -2), (1, 3), (0, 3), (2, 4), (1, -1)]

#antwoord = []

#for index, letter in coordinaten:
#    woord = puzzel[index]
#    letter = puzzel[letter]

#    antwoord.append(letter)

#print(antwoord)

# === VERSIE 4 ===
# Het is logischer om de waarden in de tuple x en y te noemen. De parameters zijn x en y
# Een woord is de x coördinaat
# Er is sprake van tuple unpacking
# Python ziet het als: for 'element' in coordinaten
# element = (0,0) , dus (x,y)

puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0, 0), (2, 0), (0, -2), (1, 3), (0, 3), (2, 4), (1, -1)]

antwoord = []

for x, y in coordinaten:
    woord = puzzel[x]
    letter = woord[y]

    antwoord.append(letter)

print(antwoord)

# === VERSIE 5 ===
# "".join() voegt items in een lijst samen tot een string
puzzel = ["Albatros", "poncho", "vlinder", "glitter"]
coordinaten = [(0, 0), (2, 0), (0, -2), (1, 3), (0, 3), (2, 4), (1, -1)]

antwoord = []

for x, y in coordinaten:
    woord = puzzel[x]
    letter = woord[y]

    antwoord.append(letter)

print("".join(antwoord))