# ---Menu---
# [?] Instructies
# [1] Boeken toevoegen (naam, auteur, genre , publicatiejaar)
# [2] Alle boeken bekijken (naam, auteur, genre, publicatiejaar)
# [3] Boeken zoeken op genre (naam, auteur, publicatiejaar)
# [4] Programma afsluiten

bibliotheek = {}

genre_dictionary = {
    "1": "Avontuur",
    "2": "Biografie",
    "3": "Detective",
    "4": "Dieren",
    "5": "Thriller",
    "6": "Fantasy",
    "7": "Science Fiction",
    "8": "Horror",
    "9": "Zelfhulp",
    "10": "Kinderboeken"
}

while True:
    while True:
        menu_option = input('\nWelkom bij de bibliotheek!\n'
              '\n'
              '---Menu---\n'
              '[?] Instructies\n' 
              '[1] Boeken toevoegen\n'
              '[2] Alle boeken bekijken\n'
              '[3] Boeken zoeken op genre\n'
              '[4] Programma afsluiten\n'
              '\n'
              'Maak een keuze: ')
        if menu_option not in ("?","1", "2", "3", "4"):
            print("\nOngeldige keuze, probeer het nog eens")
        else:
            break

# ---[?] Instructies---
    if menu_option == "?":
        print("---Instructies---\n"
              "\n"
              "=== 1. Boeken toevoegen ===\n"
              "Boeken kun je toevoegen door de juiste informatie in te voeren.\n"
              "Titel: Vul de titel van het boek in.\n"
              "Auteur: Vul de naam van de auteur in.\n"
              "Genre: Vul de genre in van het boek.\n"
              "\n"
              "---LET OP---\n"
              "Alleen deze genres zijn geldig:\n"
              "---Genres---\n"
              "Avontuur\n"
              "Biografie\n"
              "Detective\n"
              "Dieren\n"
              "Thriller\n"
              "Fantasy\n"
              "Science Fiction\n"
              "Horror\n"
              "Zelfhulp\n"
              "Kinderboeken\n"
              "\n"
              "Publicatiejaar: Vul publicatiejaar in.\n"
              "\n"
              "---LET OP---\n"
              "1. Boeken met een publicatiejaar ouder dan 1930 en nieuwer dan 2026 kunnen niet toegevoegd worden.\n"
              "2. Publicatiejaar moet een getal zijn.\n"
              "\n"
              "=== 2. Alle boeken bekijken ===\n"
              "Kies voor deze optie als je alle boeken wil bekijken die je deze sessie hebt toegevoegd.\n"
              "Je kunt tijdens de sessie altijd alle boeken terugkijken nadat je er weer een paar hebt toegevoegd.\n"
              "\n"
              "=== 3. Boeken zoeken op genre ===\n"
              "Kies voor deze optie als je graag alleen boeken per genre wil bekijken.\n"
              "\n"
              "=== 4. Programma afsluiten ===\n"
              "Als je voor deze optie kiest, sluit je het programma af en gaat alle data verloren.")

# ---[1] Boeken toevoegen---
    if menu_option == "1":
        while True:
            print("\n---Boek toevoegen---\n"
                  "Je gaat nu een boek toevoegen\n")
            titel = input("Voer titel van boek in: ")
            auteur = input("Voer auteur in: ")

            while True:
                genre = input("Voer genre in: ").title()
                if genre not in genre_dictionary.values():
                    print("Ongeldige genre\n"
                          "\n"
                          "Kies uit:\n"
                          "Avontuur\n"
                          "Biografie\n"
                          "Detective\n"
                          "Dieren\n"
                          "Thriller\n"
                          "Fantasy\n"
                          "Science Fiction\n"
                          "Horror\n"
                          "Zelfhulp\n"
                          "Kinderboeken")
                else:
                    break

            while True:
                try:
                    publicatiejaar = int(input("Voer publicatiejaar in: "))
                    if publicatiejaar > 2026:
                        print("Boeken kunnen niet in de toekomst al gepubliceerd worden, probeer opnieuw")
                    elif publicatiejaar < 1930:
                        print("Helaas is het niet mogelijk om een boek die vòòr 1930 gepubliceerd is toe te voegen, probeer opnieuw")
                    else:
                        break
                except ValueError:
                    print("Publicatiejaar moet een getal zijn, probeer opnieuw")

            boek = {
                "Auteur": auteur,
                "Genre": genre,
                "Publicatiejaar": publicatiejaar
            }

            bibliotheek[titel] = boek
            print(f"\nHet boek: '{titel}' is toegevoegd!\n")

            opnieuw_toevoegen = input("Wil je nog een boek toevoegen? (ja / nee): ")
            if opnieuw_toevoegen.lower() != "ja":
                break

# ---[2] Alle boeken bekijken---
    if menu_option == "2":
        print("\n---Boek bekijken---\n"
              "Je gaat nu alle boeken in de bibliotheek bekijken\n")
        for titel, boek in bibliotheek.items():
            print(f'--------------------\n'
                  f'Titel: {titel}')
            for key, value in boek.items():
                print(f'{key}:{value}')
        print("--------------------")

# ---[3] Boeken zoeken op genre---
    if menu_option == "3":
        while True:
            print("\n---Boek zoeken op genre---\n"
                  "Je gaat een boek zoeken op genre\n"
                  "\n---Genres---\n"
                                "[1] Avontuur\n"
                                "[2] Biografie\n"
                                "[3] Detective\n"
                                "[4] Dieren\n"
                                "[5] Thriller\n"
                                "[6] Fantasy\n"
                                "[7] Science Fiction\n"
                                "[8] Horror\n"
                                "[9] Zelfhulp\n"
                                "[10] Kinderboeken\n")

            while True:
                keuze_genre = input("Voer nummer in: ")
                if keuze_genre in genre_dictionary:
                    break
                else:
                    print("Ongeldige keuze, je moet een nummer invoeren")

            genre_gevonden = False

            for titel, boek in bibliotheek.items():
                if genre_dictionary[keuze_genre] == boek["Genre"]:
                        print(f'Boeken in het genre: {genre_dictionary[keuze_genre]}'
                              f'Titel: {titel}\n'
                              f'Auteur: {boek["Auteur"]}\n'
                              f'Publicatiejaar: {boek["Publicatiejaar"]}\n')
                        genre_gevonden = True

            if not genre_gevonden:
                print("Geen boeken gevonden in deze genre")

            terug = input("Wil je terug naar het menu?")
            if terug.lower() == "ja":
                break

# ---[4] Programma afsluiten---
    if menu_option == "4":
        print("\n---Programma aflsuiten---\n"
              "Je sluit het programma af\n"
              "\n"
              "Tot ziens!")
        break

# ---Notities---
# 1. Hoe weet ik waar ik de lege dictionaries moet plaatsen in de code?
#    bibliotheek = {}: Dit hoef je maar éénmalig aan te maken, daarna ga je boeken toevoegen
#    boek = {}: boek ga je meerdere keren moeten toevoegen aan de dictionary: bibliotheek. boek mag in de while loop blijven staan. Zorg er voor dat deze na de inputs staan zodat de variabelen gedefinieerd zijn.

# 2. for x,y in dict , je doorloopt altijd door alle items in de dictionary.

# 3. je kunt gebruikmaken van flags. Een flag is meestal een boolean variabele (True of False) die je gebruikt om bij te houden of iets is gebeurd tijdens het uitvoeren van je code.

# ---not in en != zijn niet hetzelfde!---
# != 'Niet gelijk aan'. Hier kijk je naar exact één waarde, niet naar een lijst of collectie.
# not in 'zit niet in'. Controleert of een waarde niet voorkomt in een collectie (list, tuple, dict_values, set, etc.). Geeft True als het niet in die collectie zit

# title() maakt de eerste letter van een string uppercase.