# === HOOFDSTUK 8 DICTIONARIES ===
# Twee woordenboeken zijn gelijk als ze precies dezelfde sleutel-waarde paren bevatten,
# waarbij die paren niet in dezelfde volgorde hoeven te staan.
# We kunnen dit testen met behulp van ‘==’.
producten = {"crispy chicken": 3.99,
             "yakitori": 4.99,
             "tempura seaweed": 1.99}

actie = {"yakitori": 4.99,
         "crispy chicken": 3.99,
         "tempura seaweed": 1.99}

print(producten == actie)

# vervang een value van key-value pair, je kan ook nieuw key-value pair toevoegen in de dictionary
actie.update({"tempura seaweed":7.59})

# gebruik get, want als de key-value pair niet wordt gevonden dan krijg je none terug en geen value error
print(actie.get("tempura seaweed"))

dieren = {"hond": 1,
          "kat": 2}

dieren.update({"paard":3})

print(dieren)

# Verwijder key-value pair
del dieren["hond"]

print(dieren)

dieren.update(vogel = 4)

print(dieren)

for dier, nummer in dieren.items():
    if nummer > 2:
     print(dier)


dierenbende = {
    "hond": 2,
    "kat": 4,
    "paard": 1
}

dierenbende.update(vogel = 3)
dierenbende.update(kat = 5)
del dierenbende["paard"]

print(dierenbende)

for dier, nummer in dierenbende.items():
    if nummer > 2:
        print(f'{dier} heeft {nummer}')

hoogste_aantal = 0
totaal = 0
for dier, nummer in dierenbende.items():
    totaal += nummer
    if nummer > hoogste_aantal:
        hoogste_aantal = nummer
print(f'Het totaal aantal dieren is: {totaal} en de hoogste aantal is {hoogste_aantal}')

for dier in sorted(dierenbende.keys()): # keys() is eigenlijk niet nodig want, for dier in sorted(dierenbende): doet precies hetzelfde
    print(dier, end=' ')

# end=' ' , de output wordt op dezelfde regel gezet in plaats van onder elkaar

for dier in list(dierenbende.items()):
    print(dier)


# === NIEUWE DICTIONARY AANMAKEN VANUIT COMPREHENSION ===

cijfers = {'Jan': [6.6, 4.4, 8.8], 'Piet': [8.5, 9.9, 3.7]}

gemiddelde_cijfers = {n : sum(c) / len(c) for n, c in cijfers.items()}

print(gemiddelde_cijfers)


paarden = {"Jip":"Hengst",
           "Olly": "Merrie",
           "Rocky": "Ruin"}
paarden.setdefault("Baco","Hengst")
print(paarden)

paarden.setdefault("Jip", "Ruin")

print(paarden)

nummer_lijst = {1,2,3,4,5,6,6,7}
print(nummer_lijst)

# === HOOFDSTUK 9 SETS ===
# === Ik wil weten welke items niet in beide sets aanwezig zijn ===
symbolen = {"leeuw", "ster", "maan", "oog"}
sterrenbeeld = {"stier", "leeuw", "maagd", "vissen"}

# 1 methode
print(symbolen.symmetric_difference(sterrenbeeld))

# 2 Operator
print(symbolen^sterrenbeeld)

# === Ik wil weten welke items set(symbolen) wel heeft en set(sterrenbeeld) niet ===

# 1 methode
print(symbolen.difference(sterrenbeeld))

# 2 Operator
print(symbolen-sterrenbeeld)