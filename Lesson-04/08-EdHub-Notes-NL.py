# === EEN LIJST AANMAKEN ===
# Bepaal en print de som van alle elementen in de lijst nummers met behulp van een for-statement.
# === VERSIE 1 ===
nummers = [2, 5, 7, 11, 15]
print(sum(nummers))

# === VERSIE 2 ===
numbers = [2, 5, 7, 11, 15]
totaal = 0
for i in numbers:
    totaal += i
print(totaal)


# === FUNCTIONALITEITEN VAN EEN LIJST ===
# Maak de lijst tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32] aan. Je ziet al dat er een aantal waardes niet kloppen.

# Gebruik een toekenning om 16 in 15 te veranderen
# Gebruik de methode remove() om 32 te verwijderen
# Gebruik de methode append() om 30 toe te voegen aan het eind van de lijst
# Gebruik de methode insert() om 21 toe te voegen tussen 18 en 24
# Print de lijst. Klopt de tafel nu?

tafel_van_drie = [3, 6, 9, 12, 16, 18, 24, 27, 32]

tafel_van_drie[4] = 15
tafel_van_drie.remove(32)
tafel_van_drie.insert(6, 21)
tafel_van_drie.append(30)

print(tafel_van_drie)

# Neem de lijst namen = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik'] over.

# Print de eerste 3 namen
# Vervang David en Erik door ['Daphne', 'Eva', 'Frederique'] en print de uitkomst

# === SLICES ===
#Neem de lijst namen = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik'] over.

#Print de eerste 3 namen
#Vervang David en Erik door ['Daphne', 'Eva', 'Frederique'] en print de uitkomst

namen = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik']
print(namen)
namen[3:5] = 'Daphne', 'Eva', 'Frederique'
print(namen)

# === LIST COMPREHENSION ===
# Gebruik list comprehension om een lijst te maken van alle even getallen tussen 1 en 20.

lijst = [i for i in range(1,21) if i % 2 == 0]
print(lijst)

# ________________________________

# === OVERIGE AANTEKENINGEN LISTS EN TUPLES ===

# Print de middelste items van de lijst
boodschappenlijst = ['Melk', 'Boter', 'Kaas', 'Eieren', 'Vlees']
print(boodschappenlijst[1:4])

# Print specifieke items uit de lijst
cijferlijst = [7.7, 8.3, 5.3, 6.7]
print(f'Eerste item uit cijferlijst: {cijferlijst[0]}')
print(f'Laatste item uit cijferlijst: {cijferlijst[-1]}')
print(f'Laatse item uit cijferlijst (moeilijke manier): {cijferlijst[len(cijferlijst)-1]}') # len() geeft 5 aan, maar index gaat tot 4 en dat geeft error, dus doe je -1 om op de laatste item uit te komen. Error geeft aan: list index out of range

# Verwijder een item uit de lijst
dieren = ['koe', 'paard', 'varken', 'kip']

verwijderd_dier = dieren.pop() # pop() slaat de waarde op in een variabele
print(f'In de rij dieren: {dieren} is {verwijderd_dier} verwijderd.')

# Gebruik del
del dieren[0] # Verwijdert item
print(dieren)

# gebruik remove()
# remove() verwijdert alleen de eerste exemplaar als er duplicaten aanwezig zijn
nummers = [1,4,2,6,7,8,54,3,2]
nummers.remove(2)
print(nummers)

# Gebruik een for loop om alle '3' te verwijderen
# De reden dat er een kopie wordt gemaakt is omdat in een for loop de indexen verschuiven als er items verwijderd worden. Dat voorkom je door een kopie te maken van de lijst. Die wordt op een andere plek opgeslagen
# Je gebruikt in de for loop de kopie als voorbeeld, en past de werkelijke lijst aan om toch alle '3' te verwijderen.
# Want als je toch voor kiest om kopie.remove(3) te doen, dan verander je de lijst tijdens de iteratie en verschuiven de indexen alsnog, en dat wil je niet.

# === JUISTE MANIER ===
cijfers = [1,3,6,8,4,5,66,22,6,3]
kopie = list(cijfers)

for i in kopie:
    if i == 3:
        cijfers.remove(3)

print(cijfers)

# === ONJUISTE MANIER ===
cijfers = [1,3,6,8,4,5,66,22,6,3]
kopie = list(cijfers)

for i in kopie:
    if i == 3:
        kopie.remove(3)

print(cijfers)
# Een lijst is iterable
letter_lijst = ['H', 'a', 'l', 'l', 'o']
print("".join(letter_lijst))

# Een lijst achterstevoren printen
letter_lijst.reverse()
print(letter_lijst) # print als lijst

print("".join(letter_lijst)) # print als string

# Verdubbel de waarden in de lijst
lijst_van_nummers = [1,3,5,8,9]
for nummer in lijst_van_nummers:
    print(f'De waarde wordt verdubbeld: {nummer * 2}')

lijst_van_tuples = [(1,4),(2,6),(6,7)]
for x,y in lijst_van_tuples:
    print(f'Het product van {x} en {y} is: {x * y}')

# coordinaat is het item in de list
# coordinaat item is een tupel, daarvan kan je de index aangeven dat is 0 en 1
lijst_van_coordinaten = [(2,5), (7,8), (3,5)]
for coordinaat in lijst_van_coordinaten:
    print(f'{coordinaat[0]},{coordinaat[1]}')

# Kortere manier
for x,y in lijst_van_coordinaten:
    print(f'Coordinaat ({x},{y})')

# Een lijst in hoofdletters printen met een for loop
# 1. Door de woordenlijst loopen
# 2. Alle woorden in hoofdletters zetten
# 3. Hoofdletter woord aan de hoofdletterlijst toevoegen
woorden = ['boek', 'computer', 'pen', 'potlood', 'rekenmachine']
hoofdletterlijst = []

for woord in woorden:
    hoofdletter = woord.upper()
    hoofdletterlijst.append(hoofdletter)
print(hoofdletterlijst)

# enumerate maakt van elke item in de lijst een tuple met een nummertje ervoor dus (0,item), (1,item) etc.
# === VERSIE 1 ===
for index,woord in enumerate(woorden):
    print(f'Het {index}e woord is {woord}')

# === VERSIE 2 ===
# enumerate telt vanaf 0, maar dat leest niet logisch. Je kan zelf het startnummer bepalen dat doe je door 1 achter de lijst: 'woorden' te plaatsen
# De eerste woord is dus nog steeds 'boek'
for index,woord in enumerate(woorden):
    print(f'Het {index}e woord is {woord}')