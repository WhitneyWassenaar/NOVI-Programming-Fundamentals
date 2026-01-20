#---Start met pseudocode---
# 1. Methode die namen ontvangt
# receive_list (variabele voor de in te voeren lijst?)

# 2. Methode zorgt vervolgens dat de namen uit de lijst met en hoofdletter beginnen
# receive_list.capitalize()
# [X] FOUT, je moet de items in de list aanspreken, niet de lijst zelf, maar je zorgt er wel voor dat je de nieuwe lijst een eigen variabele geeft

# 3. De items moeten gescheiden worden door een komma
# sep=","
# [X] LET OP, dit is inderdaad een seperator, dit werkt niet op de lijst zelf. Je moet er voor zorgen dat de items van de lijst worden aangesproken, door de lijst uit te pakken.
# Maar je kan ook join() gebruiken om strings aan elkaar te plakken.

# 4. Behalve de laatste item dat moet gescheiden worden met een 'en'
# input: ["mark", "elwyn", "nova" en "frans"]
# output: "mark, elwyn, nova en frans"
#print("eerste 2 items sep=",") + laatste 2 items sep="en"")

#def namen(namen_lijst):
#    namen_lijst = namen_lijst.capitalize()
#    print(namen_lijst[0:1],sep="," , namen_lijst[2:3],sep="en")

#---V1---
# Dit werkt niet want print() heeft nu maar 1 argument om te scheiden, en dat kan niet.
#def namen(namen_lijst):
#    namen_lijst_capitalized = [naam.capitalize() for naam in namen_lijst]
#    print(namen_lijst_capitalized[:3],sep=" en ")

#namen(["mark", "elwyn", "nova","frans"])

#---V2---
# Dit werkt niet want bij de print statement zeg ik eigenlijk: neem de laatste item in de lijst en scheid het item met "en".
# Dus bijvoorbeeld: "frans" is de laatste item van de lijst. Dat wordt: F en r en a en n en s
# Ik dacht dat op deze manier de "en" voor de laatste item werd geplakt, maar dat was niet zo.
def mooie_namen(lijst_van_namen):
    lijst_van_namen_cap = [naam.capitalize() for naam in lijst_van_namen]
    print(" en ".join(lijst_van_namen_cap[-1]))

lieve_docenten = ["mark", "elwyn", "nova","frans"]
mooie_namen(lieve_docenten)

#---V3---
# Er gebeurt niets, alleen de laatste list-item wordt geprint. sep="" werkt niet op 1 argument
def unieke_namen(unieke_namen_lijst):
    unieke_namen_lijst_cap = [namen.capitalize() for namen in unieke_namen_lijst]
    print(unieke_namen_lijst_cap[-1], sep=" en ")
unieke_namen(lieve_docenten)


#---V4---
# Je kunt een lijst in 2 delen scheiden. [Eerste item tot één na laatste item] en [de laatste item]
# Met ", ".join() kan je het eerste deel scheiden met komma's.
# 'en' kan gewoon als string gebruikt worden tussen de items
# Daarna plak je de laatste item erachter
def fantastische_namen(namen_lijst):
    namen_lijst_cap = [namen.capitalize() for namen in namen_lijst]
    print(", ".join(namen_lijst_cap[:-1]) + " en " + namen_lijst_cap[-1])
fantastische_namen(lieve_docenten)
# Wat ik heb geleerd

print(lieve_docenten[:3],sep=" en ")