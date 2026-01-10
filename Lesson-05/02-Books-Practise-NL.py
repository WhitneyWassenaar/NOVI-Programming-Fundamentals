# Dutch
# Deze oefening is gebaseerd op de oefening: 01-Books.py om het beter te begrijpen

# Je werkt voor een natuurreservaat en moet de populatie wilde paarden in de gaten houden.
# Je houdt 2 kudde paarden in de gaten. Je registreert de vachtkleuren in een lijst per kudde

kudde_1 = ["zwart", "vos", "bruin", "wildkleur", "vos","bruin","zwart", "bruin", "grijs"]
kudde_2 = ["grijs", "zwart", "wildkleur", "grijs", "vos", "grijs", "zwart", "vos", "bruin"]

# Maak een dictionary voor kudde_1 en kudde_2

kudde_paarden = [(kudde_1,{}),(kudde_2,{})]

# Dit is een for loop die je op item 0 en 1 van de lijst kan toepassen

for kudde, dictionary in kudde_paarden: # kudde_1 krijgt de naam: kudde en {} krijgt de naam: dictionary, je pakt de tuple meteen uit
    for kleur in kudde:                 # Nu vergelijk je het item in de lijst kudde_1 met de items in dictionary.
        if kleur not in  dictionary:    # Als het item van de lijst kudde_1 niet in de dictionary staat, dan voeg je dit item met waarde 1 toe
            dictionary[kleur] = 1
        else:
            dictionary[kleur] += 1      # De 5de item is "vos", "vos" was al een keer voorgekomen in de lijst. Omdat "vos" nu voor de tweede keer voorkomt, wordt de waarde met 1 verhoogd dus wordt de value van "vos" 2

print(kudde_paarden[0][1]) # Dictionary voor 1ste tuple van de lijst kudde_paarden
print(kudde_paarden[1][1]) # Dictionary voor 2de tuple van de lijst kudde_paarden

# Welke kleur komt het vaakst voor bij beide kuddes?

# Je maakt een variabele aan voor beide kuddes om te kunnen printen. Hier wordt de keur die het meest bij beide kuddes is geteld weergegeven
kudde_1_aantal = ("",0)
kudde_2_aantal = ("",0)

for kleur, aantal in kudde_paarden[0][1].items(): # Je geeft voor de key en de value een naam. Key is 'kleur' en value is 'aantal'
    if kudde_1_aantal[1] < aantal:                # Voor elke item (kleur, aantal) in de dictionary wordt gekeken of het aantal kleiner of groter is dan de value van kudde_1_aantal
        kudde_1_aantal = (kleur,aantal)           # Als de value van het item in de dictionary groter is dan de value van kudde_1_aantal, dan wordt de tuple geupdate met de key-value pair die op dat moment door de for loop is gegaan

for kleur, aantal in kudde_paarden[1][1].items():
    if kudde_2_aantal[1] < aantal:
        kudde_2_aantal = (kleur,aantal)

print(kudde_1_aantal)
print(kudde_2_aantal)