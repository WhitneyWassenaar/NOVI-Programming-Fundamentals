# === BONUS ===
# Vraag de gebruiker om studenten en cijfers toe te voegen aan de lijst via 'input'
# Laat de gebruiker zoeken op naam om het cijfer van een specifieke student te kunnen zien
# Sorteer de lijst op cijfers en druk ze af
studenten = []

while True:
    naam_student = input('Naam student: (Druk op x om invoer te beëindigen) ')
    if naam_student == 'x':
        break
    invoer_cijfer = float(input('Cijfer: '))
    studenten_item = (naam_student, invoer_cijfer)

    studenten.append(studenten_item)

# === SORTEER DE LIJST OP CIJFERS ===
# sorted() geeft een lijst terug.
# Er wordt standaard op de eerste waarde van elke tuple gesorteerd. In dit geval is dat dus de naam van de student

# key=lambda x: x[1]
# key bepaalt waarop de sortering gebaseerd is
# lambda x: x[1] betekent: voor elke item x (in dit geval een tuple (naam_student, invoer_cijfer), gebruik het tweede element van de tuple x[1]
# x = studenten_item
# x[0] = "naam_student"
# x[1] = invoer_cijfer

# reverse=True
# Standaard sorteert sorted() van klein naar groot, maar je wil in dit geval dat het hoogste cijfer als eerste geprint wordt. Dus maak je er reverse=True van.

# sorted() maakt een nieuwe lijst aan het verandert het origineel niet tenzij je het toewijst. Bijvoorbeeld: studenten = sorted(studenten)

studenten = sorted(studenten, key=lambda x: x[1], reverse=True)

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

zoek_op_naam = input('Voer naam van student in om het cijfer te bekijken: ')
for student, cijfer in studenten:
    if zoek_op_naam == student:
        print(f'{student}, {cijfer}')



