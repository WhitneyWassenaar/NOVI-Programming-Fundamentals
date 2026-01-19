# ==========================================
# Voorbeeld Opdracht
# Schrijf een functie die de tekst “Hello, World!” print. Roep vervolgens de functie aan.
# ==========================================

def print_hello_world():
    print('Hello, World!')

print_hello_world()  # Uitkomst: Hello, World!


# ==========================================
# Opdracht 1:
# Print de tafel van 5 met behulp van een for-loop en een functie (genaamd 'print_tafel_regel').
# De factor en for-loop zijn al gegeven. Schrijf de functie om de regel van de tafel te printen.
#
# Verwachte uitkomst:
# 1  x  5  =  5
# 2  x  5  =  10
# 3  x  5  =  15 enz.
# ==========================================
factor = 5
def print_tafel_regel(x):
    for i in range(x):
        print(f'{i} x {x} = {i * x}')

print_tafel_regel(factor)

# ==========================================
# Opdracht 2:
# Maak een dobbelsteen met de volgende deelopdrachten.
#
# Opdracht 2a:
# Maak met behulp van de bibliotheek (library) 'random' een functie die een willekeurig getal tussen 1 en 6 genereert.
# Zorg dat de functie twee argumenten ontvangt, namelijk 'min' en 'max'. Voor het minimum (1) en maximum (6).
# Voer de functie 10 keer uit (met een for-loop). Als het willekeurige getal is gegenereert print je het getal.

import random
# Zonder (min,max) parameters

#def random_number_0():
#    print(random.randint(1,6))
#random_number_0()

#def random_number(min,max):
#    for i in range(10):
#        print(random.randint(min,max), end=" ")

#random_number(1,6)

# Maak een variabele aan 'aantal_keer_zes' en zet deze op 0. Schrijf een functie die aan het eind print hoe vaak er een 6 is gegooid.
# De variabele 'aantal_keer_zes' moet in de print statement worden gebruikt.
#
# Verwachte uitkomst (voorbeeld):
# 3 7 2 6 1 4 5 6 2 1
# Er is 2 keer een 6 gegooid
# ==========================================
import random

# Genereert random getal
def random_number(min_num,max_num):
        return random.randint(min_num,max_num)

def aantal_keer_zes_gegooid(random_getal):
    return random_getal == 6

# Genereert 10 x een random getal
def tel_zessen():
    aantal_keer_zes = 0

    for i in range(10):
        random_getal = random_number(1,6)
        print(random_getal, end=" ")
        if aantal_keer_zes_gegooid(random_getal):
            aantal_keer_zes += 1

    print(f"\nEr is {aantal_keer_zes} keer zes gegooid")

# ==========================================
# Opdracht 3:
# Omrekenen van Fahrenheit naar Celsius. Gegeven zijn temperaturen van drie steden in Fahrenheit.
#
# Schrijf een functie die de temperatuur in Fahrenheit ontvangt als argument en deze omrekent naar Celsius.
# De formule voor de conversie is als volgt: celsius = (fahrenheit - 32) * 5/9
# Schrijf ook een functie die de temperatuur afrond in hele getallen.
# print de temperatuur in Celsius afgerond op hele getallen.
#
# Verwachte uitkomst:
# 18
# 24
# 40
# ==========================================

temp_in_fahr_stockholm = 65
temp_in_fahr_sydney = 75
temp_in_fahr_cairo = 104

def naar_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

def getal_afronden(celsius):
    return round(celsius)

def resultaat(fahrenheit):
    celsius = naar_celsius(fahrenheit)
    return getal_afronden(celsius)

print(resultaat(temp_in_fahr_stockholm))

# Als je een float naar int maakt, rond je niet echt af. Het is wel een heel getal maar wordt altijd naar beneden afgerond.
# round() , daar rond je een getal goed mee af.