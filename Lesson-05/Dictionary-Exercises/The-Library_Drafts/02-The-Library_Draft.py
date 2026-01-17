"""bibliotheek = {
    "The Silent Patient": {
        "auteur": "Alex Michaelides",
        "genre": "Thriller",
        "publicatiejaar": 2019
    },
    "Where the Crawdads Sing": {
        "auteur": "Delia Owens",
        "genre": "Fictie",
        "publicatiejaar": 2018
    },
    "The Night Circus": {
        "auteur": "Erin Morgenstern",
        "genre": "Fantasy",
        "publicatiejaar": 2011
    },
    "Educated": {
       "auteur": "Tara Westover",
       "genre": "Memoir",
       "publicatiejaar": 2018
    },
   "Circe": {
        "auteur": "Madeline Miller",
       "genre": "Fantasy",
       "publicatiejaar": 2018
    }
}
"""
#Je gaat een bibliotheekprogramma maken. Het programma moet de volgende functionaliteiten hebben:
#1. De gebruiker moet boeken kunnen toevoegen aan de bibliotheek. Een boek heeft de volgende eigenschappen:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

# ---Eenmalig 1 boek toevoegen---
"""
bibliotheek = {}

titel_boek = input("Voer titel van boek in: ")
auteur = input("Voer naam van auteur in: ")
genre = input("Voer genre in: ")
publicatiejaar = input("Voer publicatiejaar in: ")

boek = {
    "Auteur": auteur,
    "Genre":genre,
    "Publicatiejaar": publicatiejaar
}

bibliotheek[titel_boek] = boek

for titel, gegevens in bibliotheek.items():
    print(f"Titel: {titel}")
    for key, value in gegevens.items():
        print(f"{key}: {value}")
"""
# --- Meerdere boeken toevoegen


bibliotheek = {}

while True:

    titel_boek = input("Voer titel van boek in: ")
    auteur = input("Voer naam van auteur in: ")
    genre = input("Voer genre in: ")
    publicatiejaar = input("Voer publicatiejaar in: ")

    boek = {
        "Auteur": auteur,
        "Genre": genre,
        "Publicatiejaar": publicatiejaar
    }

    bibliotheek[titel_boek] = boek
    optie = input("Wil je nog een boek toevoegen?: ")
    if optie.lower() != "ja":
        break

for titel, gegevens in bibliotheek.items():
    print(f"\n"
          f"Titel: {titel}")
    for key, value in gegevens.items():
        print(f"{key}: {value}")
"""
#2. De gebruiker moet een lijst van alle boeken in de bibliotheek kunnen opvragen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar
"""
alle_boeken = input("Wil je alle boeken in de bibliotheek bekijken? (ja/nee: ")
if alle_boeken.lower() == "ja":
    for titel, gegevens in bibliotheek.items():
        print(f"Titel: {titel}")
        for key, value in gegevens.items():
            print(f"{key}:{value}")
"""
#3. De gebruiker moet een lijst van alle boeken in een bepaald genre kunnen opvragen. De gebruiker moet het genre kunnen invoeren en het programma moet alle boeken in dat genre tonen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Publicatiejaar

"""
genre_check = input("Welke categorie genre wil je boeken bekijken?\n"
                    "[1] Drama"
                    "[2] Avontuur"
                    "[3] Horror"
                    "\n"
                    "Kies 1, 2 of 3")

if genre_check == "1":
    for titel, boek in bibliotheek.items():
        if boek["Genre"] == "Drama":
            print(f'{titel}\n'
                  f'{boek["Auteur"]}\n'
                  f'{boek["Publicatiejaar"]}')

"""
#4. De gebruiker moet het programma kunnen stoppen.

#Een paar tips voor het maken van dit programma:
# Als je een keuze menu maakt, kun je een while loop gebruiken die blijft loopen totdat de gebruiker kiest om te stoppen.
# Je keuze menu is eigenlijk een if-elif-else statement. Je kunt de keuze van de gebruiker opslaan in een variabele en dan met if-elif-else bepalen wat er moet gebeuren.

"""
