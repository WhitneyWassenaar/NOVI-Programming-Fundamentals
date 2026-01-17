# ---Je gaat boeken toevoegen in de lege dictionary: bibliotheek---
bibliotheek = {}
genre = {
            "1":"Avontuur",
            "2": "Biografie",
            "3":"Detective",
            "4":"Dieren",
            "5":"Thriller",
            "6":"Fantasy",
            "7":"Science Fiction",
            "8":"Horror",
            "9":"Zelfhulp",
            "10":"Kinderboeken"
        }
print('\nWelkom bij de bibliotheek!')
# ---Menu---
while True:

    menu = input('\n'
          '---Menu---\n'
          '\n'
          '[1] Boeken toevoegen\n'
          '[2] Boekenlijst weergeven\n'
          '[3] Zoek boek op genre\n'
          '[4] Programma afsluiten\n'
                 '\n'
                 'Maak een keuze: ')

    if menu == "1":
        # ---Boeken toevoegen---
        # Na elke ronde wordt er gevraagd of je nog een boek wil toevoegen. Daarom zet je de inputs in een while loop---
        while True:

            # ---Vul boek gegevens in---
            titel_boek = input('\nVoer titel van boek in: ')
            auteur_boek = input('Voer auteur in: ')
            while True:

                genre_boek = input('Voer genre in: ').lower()
                if genre_boek not in [genre_type.lower() for genre_type in genre.values()]:
                    print(f'\n{genre_boek} is ongeldig, probeer opnieuw')
                    print(f'\nGeldige genres zijn:\n')
                    for genre_type in genre.values():
                        print(f'{genre_type}')
                    print('')
                else:
                    for genre_type in genre.values():
                        if genre_boek.lower() == genre_type.lower():
                            genre_boek = genre_type
                            break
                    break

            while True:

                publicatiejaar_boek = int(input('Voer publicatiejaar in: '))
                if publicatiejaar_boek <1800  or publicatiejaar_boek > 2026:
                    print(f'\n{publicatiejaar_boek} is ongeldig')
                else:
                    break


            # ---Boek gegevens worden opgeslagen in een dictionary---
            boek_gegevens = {
                "Auteur": auteur_boek,
                "Genre": genre_boek,
                "Publicatiejaar": publicatiejaar_boek
            }

            # ---Boektitel en de boekgegevens worden in de dictionary van bibliotheek toegevoegd---
            bibliotheek[titel_boek] = boek_gegevens

            optie = input('Nog een boek toevoegen? (ja/nee)\n'
                          '')
            if optie.lower() != "ja":
                print('Boeken zijn toegevoegd!\n'
                      '\n'
                      'Je gaat nu terug naar het menu.')
                break

    elif menu == "2":
        for titel_boek, boek_gegevens in bibliotheek.items():
            print(f'\n'
                  f'Titel: {titel_boek}\n'
                  f'Auteur: {boek_gegevens["Auteur"]}\n'
                  f'Genre: {boek_gegevens["Genre"]}\n'
                  f'Publicatiejaar: {boek_gegevens["Publicatiejaar"]}\n'
                  f'\n')

    elif menu == "3":

        genre_keuze = input('\n---Genre---\n'
                            '[1] Avontuur\n'
                            '[2] Biografie\n'
                            '[3] Detective\n'
                            '[4] Dieren\n'
                            '[5] Thriller\n'
                            '[6] Fantasy\n'
                            '[7] Science Fiction\n'
                            '[8] Horror\n'
                            '[9] Zelfhulp\n'
                            '[10] Kinderboeken\n'
                            '\n'
                            'Maak een keuze (Vul nummer in): ')


        if genre_keuze in genre:
            gekozen_genre = genre[genre_keuze]



            gevonden_boeken = []


            for titel_boek, boek_gegevens in bibliotheek.items():
                if boek_gegevens["Genre"] == gekozen_genre:
                    gevonden_boeken.append((titel_boek, boek_gegevens))


            if len(gevonden_boeken) == 0:
                print("Geen boeken gevonden")

            else:
                if len(gevonden_boeken) == 1:
                    woord = "boek"
                else:
                    woord = "boeken"
                print(f'\n{len(gevonden_boeken)} {woord} gevonden')

            for titel_boek, boek_gegevens in gevonden_boeken:
                print(f'\n'
                      f'Titel: {titel_boek}\n'
                      f'Auteur: {boek_gegevens["Auteur"]}\n'
                      f'Publicatiejaar: {boek_gegevens["Publicatiejaar"]}\n')

    elif menu == "4":
        print('\nProgramma wordt afgesloten\n')
        break

    else:
        print('\nOngeldige keuze')



print('Tot ziens!')

