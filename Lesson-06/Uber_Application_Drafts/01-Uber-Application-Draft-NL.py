# Dit vond ik echt een lastige opdracht, ik ga deze opdracht zeker vaker opnieuw proberen te maken
# Dit was niet helemaal volgens de opdracht. Er moest voordat er een rit geboekt ging worden nog gevraagd worden of je wil kiezen uit voorkeursdienst of andere dienst.
diensten =  {
    '1':'Uber Van',
    '2':'Uber Black',
    '3':'Uber X'
}

uber = {
    'Uber Van':3.50,
    'Uber Black':2.00,
    'Uber X':1.50
}

USER = {
    'Preference':'',
    'history':[]
}

def calculate_cost(kilometer,prijs):
    return kilometer * prijs

def get_user_choice(dienst,kilometer):
    prijs = uber[dienst]
    totaal = calculate_cost(kilometer,prijs)
    print(f'U heeft gekozen voor {dienst}. Totale kosten zijn: €{totaal:.2f}\n')
    USER['history'].append({'dienst': dienst, 'km': kilometer, 'prijs': totaal})

print('Welkom bij Choose Your Uber!')
while True:


        start_keuze = input('\n---Start---\n'
                            '\n'
                            'Wat wilt u doen?\n'
                            '[1] Voorkeursdienst gebruiken\n'
                            '[2] Andere dienst kiezen\n' 
                            '[3] Voorkeursdienst instellen\n'
                            '[4] Ritgeschiedenis bekijken\n'
                            '[5] Afsluiten\n'
                            '\n'
                            'Maak een keuze door het nummer in te voeren: ')
        if start_keuze == '1':
            if USER['Preference'] == '':
                print('Er is nog geen voorkeursdienst gekozen, kies eerst een dienst')
            else:
                dienst = USER['Preference']
                print(f"U gebruikt uw voorkeursdienst: {USER['Preference']}")
                while True:
                    try:
                        km = int(input('Voer aantal kilometers in: '))
                        if km <= 0:
                            print('Je moet wel kilometers invullen, anders kan de dienst niet geboekt worden\n')
                        elif 0 < km <= 5:
                            print('Afstanden korter dan 6 kilometer worden niet geaccepteerd\n')
                        else:
                            print('\nDankjewel voor het invullen!\n')
                            break
                    except ValueError:
                        print('Voer hele getallen in!\n')

                get_user_choice(dienst, km)


        elif start_keuze == '2':
            while True:
                dienst_optie = input(
                    '\n----Diensten---\n'
                    '\n'
                    'Welke dienst wilt u gebruiken?\n'
                    '[1] Uber Van   | € 3.50 per km\n'
                    '[2] Uber Black | € 2.00 per km\n'
                    '[3] Uber X     | € 1.50 per km\n'
                    '\n'
                    'Maak een keuze door het nummer in te voeren: ')

                if dienst_optie not in diensten:
                    print('\nOngeldige keuze probeer het nog eens\n')
                else:
                    dienst = diensten[dienst_optie]
                    break

            while True:
                try:
                    km = int(input('Voer aantal kilometers in: '))
                    if km <= 0:
                        print('Je moet wel kilometers invullen, anders kan de dienst niet geboekt worden\n')
                    elif 0 < km <= 5:
                        print('Afstanden korter dan 6 kilometer worden niet geaccepteerd\n')
                    else:
                        print('\nDankjewel voor het invullen!\n')
                        break
                except ValueError:
                    print('Voer hele getallen in!\n')

            get_user_choice(dienst, km)

        elif start_keuze == '3':
            print('\n---Voorkeurdienst instellen---\n'
                  '\n'
                  'Beschikbare diensten')
            for key,dienst in diensten.items():
                prijs = uber[dienst]
                print(f'[{key}] {dienst}: €{prijs:.2f} per km')

            voorkeur = input('\nKies een voorkeursdienst door het nummer in te voeren: ')

            if voorkeur in diensten:
                USER['Preference'] = diensten[voorkeur]
                print(f'Uw voorkeur is ingesteld op {USER['Preference']}')

            else:
                print('Ongeldige keuze, probeer opnieuw')

        elif start_keuze == '4':
            print('\n---Ritgeschiedenis bekijken---\n')
            if not USER['history']:
                print('Geen ritten gemaakt')
            else:
                print(f'\n---Ritgeschiedenis---\n')
                for rit in USER['history']:
                    print(f"{rit['dienst']} | {rit['km']} kilometer | €{rit['prijs']:.2f}")
        elif start_keuze == '5':
            print('Afgesloten')
            break
