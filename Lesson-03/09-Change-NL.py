# Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent,
# en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.
# Het programma gebruikt een while-loop om de berekening stap voor stap uit te voeren,
# telkens de grootste munt eraf halend totdat het bedrag nul is.
#
# Stappenplan:
#
# 1. Vraag de gebruiker om een bedrag in centen in te voeren (bijvoorbeeld 87).
#       (Bonus: check of de gebruiker niet meer dan 100 invoert)
# 2. Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken.
#    De loop stopt wanneer het bedrag nul is.
# 3. Maak in de while-loop, voor elke munt waarde een (nested) if-statement, waarin je het volgende doet:
#       - Bereken hoe vaak die muntwaarde in het bedrag past.
#       - Trek zo vaak de muntwaarde van het bedrag af,
#         zodat de volgende iteratie van de while-loop het aangepast bedrag gebruikt
#       - Print hoeveel munten van deze waarde de gebruiker terug moet krijgen.
#
# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.

# === VERSIE 1 ===
# BUG: Het woord 'munt' of 'munten' wordt niet juist weergegeven in de print statement
vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

aantal_50 = 0
aantal_20 = 0
aantal_10 = 0
aantal_5 = 0
aantal_1 = 0

invoer = int(input('Voer aantal cent in: '))
while invoer <= 0 or invoer > 100:
    print('ongeldige hoeveelheid')
    invoer = int(input('Voer aantal cent in: '))

# while invoer <= 100 and invoer > 0: | Dit is overbodig want je controleert al in de vorige while loop of invoer groter is dan 100 of kleiner of gelijk is aan 0
# while invoer <= 100 or invoer > 0:  | Dit kan niet want als je bijvoorbeeld 50 zou invoeren dan is het True voor beiden condities, maar bij de volgende ronde wordt invoer = 0, voor invoer <= 100 is dat True, maar de loop blijft nu draaien omdat er verder niets meer wordt gedaan met 0 en de loop blijft altijd true.

while invoer > 0: # Dit klopt want, zolang invoer groter is dan 0 zal de loop draaien, wanneer het 0 is stopt de loop en gaan we door naar de volgende code
    if invoer >= vijftig_cent:
        invoer -= vijftig_cent
        aantal_50 += 1

    elif invoer >= twintig_cent:
        invoer -= twintig_cent
        aantal_20 += 1

    elif invoer >= tien_cent:
        invoer -= tien_cent
        aantal_10 += 1

    elif invoer >= vijf_cent:
        invoer -= vijf_cent
        aantal_5 += 1

    elif invoer >= een_cent:
        invoer -= een_cent
        aantal_1 += 1

# De bedoeling was om voor elke aantal munten per munteenheid de juiste vorm van het woord 'munt' weer te geven. Ik heb dus voor elke munteenheid een if statement geschreven.
# Het probleem is, dat op deze manier, de variabele 'munt' elke keer wordt overschreven. Omdat python van boven naar beneden werkt, wordt alleen de laatste if statement onthouden.
# Daarna geldt voor alle variabelen met de naam: 'munt' dat die afhankelijk van de conditie 'munt' of 'munten' wordt.
# Dus als er ergens in de code 'munt' verandert naar 'munten', dan blijft munt = 'munten'
# bijvoorbeeld je voert 81 in:

munt = 'munt'
meervoud = 'munten'

if aantal_50 == 1:   #| 81//50 = 1 dus munt = munt
    munt = munt
else:
    munt = meervoud

if aantal_20 == 1:   #| 31//20 = 1 dus munt = munt
    munt = munt
else:
    munt = meervoud

if aantal_10 == 1:   #| 11//10 = 1 dus munt = munt
    munt = munt
else:
    munt = meervoud

if aantal_5 == 1:    #|1//5 = 0 dus aantal_5 is niet gelijk aan 1 en wordt dus munt = meervoud. Vanaf nu is munt = meervoud
    munt = munt
else:
    munt = meervoud

if aantal_1 == 1:    #|1/1 = 1 dus munt = munt, maar de vorige if statement heeft bepaald dat munt = meervoud, dus als munt = munt, blijft munt = meervoud en verliest ook de else statement zijn functie.
    munt = munt
else:
    munt = meervoud

print(f'Je moet teruggeven: \n'
      '\n'
      f'{aantal_50} {munt} van 50 cent\n'
      f'{aantal_20} {munt} van 20 cent\n'
      f'{aantal_10} {munt} van 10 cent\n'
      f'{aantal_5} {munt} van 5 cent\n'
      f'{aantal_1} {munt} van 1 cent')


# === VERSIE 2 ===

vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

aantal_50 = 0
aantal_20 = 0
aantal_10 = 0
aantal_5 = 0
aantal_1 = 0

invoer = int(input('Voer aantal cent in: '))
while invoer <= 0 or invoer > 100:
    print('ongeldige hoeveelheid')
    invoer = int(input('Voer aantal cent in: '))

while invoer > 0:
    if invoer >= vijftig_cent:
        invoer -= vijftig_cent
        aantal_50 += 1

    elif invoer >= twintig_cent:
        invoer -= twintig_cent
        aantal_20 += 1

    elif invoer >= tien_cent:
        invoer -= tien_cent
        aantal_10 += 1

    elif invoer >= vijf_cent:
        invoer -= vijf_cent
        aantal_5 += 1

    elif invoer >= een_cent:
        invoer -= een_cent
        aantal_1 += 1


# === FUNCTIE ===
# Dit is een functie die bepaalt of het woord 'munt' in enkel of meervoud wordt weergegeven in de print statement.
# Gebruik een functie als een stuk code zich vaak herhaalt.
# Parameter in een functie kan elke naam hebben. Die kan dus ingevuld worden met een gedefinieerde variabele.

def munt(aantal):
    if aantal == 1:
        return 'munt'
    else:
        return 'munten'


print(f'Je moet teruggeven: \n'
      '\n'
      f'{aantal_50} {munt(aantal_50)} van 50 cent\n'
      f'{aantal_20} {munt(aantal_20)} van 20 cent\n'
      f'{aantal_10} {munt(aantal_10)} van 10 cent\n'
      f'{aantal_5} {munt(aantal_5)} van 5 cent\n'
      f'{aantal_1} {munt(aantal_1)} van 1 cent')

# === VERSIE 3 ===
# Geldbiljetten toegevoegd
vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

een_euro = 100
twee_euro = 200

vijf_euro = 500
tien_euro = 1000
twintig_euro = 2000
vijftig_euro = 5000

aantal_5000 = 0
aantal_2000 = 0
aantal_1000 = 0
aantal_500 = 0
aantal_200 = 0
aantal_100 = 0
aantal_50 = 0
aantal_20 = 0
aantal_10 = 0
aantal_5 = 0
aantal_1 = 0

invoer = int(input('Voer aantal eurocent in: '))
while invoer <= 0 or invoer > 1E6:
    print('ongeldige hoeveelheid')
    invoer = int(input('Voer aantal eurocent in: '))

while invoer > 0:
    if invoer >= vijftig_euro:
        invoer -= vijftig_euro
        aantal_5000 += 1

    elif invoer >= twintig_euro:
        invoer -= twintig_euro
        aantal_2000 += 1

    elif invoer >= tien_euro:
        invoer -= tien_euro
        aantal_1000 += 1

    elif invoer >= vijf_euro:
        invoer -= vijf_euro
        aantal_500 += 1

    elif invoer >= twee_euro:
        invoer -= twee_euro
        aantal_200 += 1

    elif invoer >= een_euro:
        invoer -= een_euro
        aantal_100 += 1

    elif invoer >= vijftig_cent:
        invoer -= vijftig_cent
        aantal_50 += 1

    elif invoer >= twintig_cent:
        invoer -= twintig_cent
        aantal_20 += 1

    elif invoer >= tien_cent:
        invoer -= tien_cent
        aantal_10 += 1

    elif invoer >= vijf_cent:
        invoer -= vijf_cent
        aantal_5 += 1

    elif invoer >= een_cent:
        invoer -= een_cent
        aantal_1 += 1


# === FUNCTIE ===
# Dit is een functie die bepaalt of het woord 'munt' in enkel of meervoud wordt weergegeven in de print statement.
# Gebruik een functie als een stuk code zich vaak herhaalt.
# Parameter in een functie kan elke naam hebben. Die kan dus ingevuld worden met een gedefinieerde variabele.

def munt(aantal):
    if aantal == 1:
        return 'munt'
    else:
        return 'munten'

# === FUNCTIE ===
# Dit is een functie die bepaalt of het woord 'brief' in enkel of meervoud wordt weergegeven in de print statement. Omdat het om geldbiljetten gaat, heb ik als enkelvoud 'briefje' gekozen i.p.v. brief.
# Gebruik een functie als een stuk code zich vaak herhaalt.
# Parameter in een functie kan elke naam hebben. Die kan dus ingevuld worden met een gedefinieerde variabele.

def brief(aantal):
    if aantal == 1:
        return 'briefje'
    else:
        return 'brieven'


print(f'Je moet teruggeven: \n'
      '\n'
      f'{aantal_5000} {brief(aantal_5000)} van 50 euro\n'
      f'{aantal_2000} {brief(aantal_2000)} van 20 euro\n'
      f'{aantal_1000} {brief(aantal_1000)} van 10 euro\n'
      f'{aantal_500} {brief(aantal_500)} van 5 euro\n'
      f'{aantal_100} {munt(aantal_100)} van 1 euro\n'
      f'{aantal_50} {munt(aantal_50)} van 50 cent\n'
      f'{aantal_20} {munt(aantal_20)} van 20 cent\n'
      f'{aantal_10} {munt(aantal_10)} van 10 cent\n'
      f'{aantal_5} {munt(aantal_5)} van 5 cent\n'
      f'{aantal_1} {munt(aantal_1)} van 1 cent')


# === VERSIE 4 ===
vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

een_euro = 100
twee_euro = 200

vijf_euro = 500
tien_euro = 1000
twintig_euro = 2000
vijftig_euro = 5000

# === FUNCTIE ===
# Dit is een functie die bepaalt of het woord 'munt' in enkel of meervoud wordt weergegeven in de print statement.
# Gebruik een functie als een stuk code zich vaak herhaalt.
# Parameter in een functie kan elke naam hebben. Die kan dus ingevuld worden met een gedefinieerde variabele.

def munt(aantal):
    if aantal == 1:
        return 'munt'
    else:
        return 'munten'

# === FUNCTIE ===
# Dit is een functie die bepaalt of het woord 'brief' in enkel of meervoud wordt weergegeven in de print statement. Omdat het om geldbiljetten gaat, heb ik als enkelvoud 'briefje' gekozen i.p.v. brief.
# Gebruik een functie als een stuk code zich vaak herhaalt.
# Parameter in een functie kan elke naam hebben. Die kan dus ingevuld worden met een gedefinieerde variabele.

def brief(aantal):
    if aantal == 1:
        return 'briefje'
    else:
        return 'brieven'

invoer = int(input('Voer aantal eurocent in: '))
while invoer <= 0 or invoer > 1E6: # Tot 100.0000 eurocent kan je invoeren
    print('ongeldige hoeveelheid')
    invoer = int(input('Voer aantal eurocent in: '))

while invoer > 0:
    if invoer >= vijftig_euro:
        aantal_5000 = invoer // 5000
        invoer -= vijftig_euro * aantal_5000
        print(f'{aantal_5000} {brief(aantal_5000)} van 50 euro')

    elif invoer >= twintig_euro:
        aantal_2000 = invoer // 2000
        invoer -= twintig_euro * aantal_2000

        print(f'{aantal_2000} {brief(aantal_2000)} van 20 euro')

    elif invoer >= tien_euro:
        aantal_1000 = invoer // 1000
        invoer -= tien_euro * aantal_1000

        print(f'{aantal_1000} {brief(aantal_1000)} van 10 euro')

    elif invoer >= vijf_euro:
        aantal_500 = invoer // 500
        invoer -= vijf_euro * aantal_500

        print(f'{aantal_500} {brief(aantal_500)} van 5 euro')

    elif invoer >= twee_euro:
        aantal_200 = invoer // 200
        invoer -= twee_euro * aantal_200

        print(f'{aantal_200} {munt(aantal_200)} van 2 euro')

    elif invoer >= een_euro:
        aantal_100 = invoer // 100
        invoer -= een_euro * aantal_100

        print(f'{aantal_100} {munt(aantal_100)} van 1 euro')

    elif invoer >= vijftig_cent:
        aantal_50 = invoer // 50
        invoer -= vijftig_cent * aantal_50

        print(f'{aantal_50} {munt(aantal_50)} van 50 eurocent')

    elif invoer >= twintig_cent:
        aantal_20 = invoer // 20
        invoer -= twintig_cent * aantal_20

        print(f'{aantal_20} {munt(aantal_20)} van 20 eurocent')

    elif invoer >= tien_cent:
        aantal_10 = invoer // 10
        invoer -= tien_cent * aantal_10

        print(f'{aantal_10} {munt(aantal_10)} van 10 eurocent')

    elif invoer >= vijf_cent:
        aantal_5 = invoer // 5
        invoer -= vijf_cent * aantal_5

        print(f'{aantal_5} {munt(aantal_5)} van 5 eurocent')

    elif invoer >= een_cent:
        aantal_1 = invoer // 1
        invoer -= een_cent * aantal_1

        print(f'{aantal_1} {munt(aantal_1)} van 1 eurocent')


# === VERSIE 5 ===
# Er wordt gebruik gemaakt van een tuple, functies en een for loop
vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

een_euro = 100
twee_euro = 200

vijf_euro = 500
tien_euro = 1000
twintig_euro = 2000
vijftig_euro = 5000

def munt(aantal):
    if aantal == 1:
        return 'munt'
    else:
        return 'munten'

def brief(aantal):
    if aantal == 1:
        return 'briefje'
    else:
        return 'brieven'

invoer = int(input('Voer aantal eurocent in: '))
while invoer <= 0 or invoer > 1E6: # Tot 100.0000 eurocent kan je invoeren
    print('ongeldige hoeveelheid')
    invoer = int(input('Voer aantal eurocent in: '))

# Dit is een tuple
wisselgeld = [
    (5000, brief, '50 euro'),
    (2000, brief, '20 euro'),
    (1000, brief, '10 euro'),
    (500, brief, '5 euro'),
    (200, munt, '2 euro'),
    (100, munt, '1 euro'),
    (50, munt, '50 eurocent'),
    (20, munt, '20 eurocent'),
    (10, munt, '10 eurocent'),
    (5, munt, '5 eurocent'),
    (1, munt, '1 eurocent')
]

print('Je moet teruggeven: ')
for waarde, functie, naam in wisselgeld:                # Deze 3 waarden heb je ook in je tuple
    aantal = invoer // waarde                           # Dit is hoe vaak een waarde in invoer past
    if aantal > 0:                                      # Als het aantal groter is dan 0, voer dan print statement uit
        print(f'{aantal} {functie(aantal)} van {naam}') # {aantal} = Hoe vaak past de waarde in invoer, {functie(aantal)} = in de tuple is al aangegeven welke functie erbij hoort, aantal bepaalt of de functie een enkelvoud of meervoud returned, {naam} = naam van munteenheid/biljetten
        invoer -= aantal * waarde                       # Bij elke iteratie voert de for loop deze actie uit