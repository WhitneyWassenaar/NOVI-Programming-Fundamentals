# Lijst met studenten en hun behaalde cijfers.
# Gebruik een lijst van tuples
# Elke tuple bevat een lijst van een student met zijn of haar cijfer
# Maak een lijst van tuples

# === VERSIE 1 ===
# aantal_studenten = len(studenten) hoeft nit in een for loop
# else statement is niet nodig, als de conditie niet waar is dan gebeurt er niets.

studenten = [("Maria", 8.3), ("Arnold", 3.9), ("Alice", 5.7), ("Sven", 6.2)]
sum_cijfer = 0
beste_student = ""
hoogste_cijfer = 0
aantal_studenten = 0

for student, cijfer in studenten:
    aantal_studenten = len(studenten)
    sum_cijfer += cijfer
    if cijfer > hoogste_cijfer:
        hoogste_cijfer = cijfer
        beste_student = student
    else:
        hoogste_cijfer = hoogste_cijfer

    print(f'{student} - {cijfer}')


print(f'Gemiddelde score: {(sum_cijfer/aantal_studenten):.1f}')
print(f'De beste student is {beste_student} met een {hoogste_cijfer}')

# === VERSIE 2 ===
# Ik heb aantal_studenten = len(studenten) uit de for loop gehaald en de else statement weggehaald
studenten = [("Maria", 8.3), ("Arnold", 3.9), ("Alice", 5.7), ("Sven", 6.2)]
sum_cijfer = 0
beste_student = ""
hoogste_cijfer = 0
aantal_studenten = len(studenten)

for student, cijfer in studenten:
    sum_cijfer += cijfer
    if cijfer > hoogste_cijfer:
        hoogste_cijfer = cijfer
        beste_student = student

    print(f'{student} - {cijfer}')

print(f'Gemiddelde score: {(sum_cijfer/aantal_studenten):.1f}')
print(f'De beste student is {beste_student} met een {hoogste_cijfer}')
