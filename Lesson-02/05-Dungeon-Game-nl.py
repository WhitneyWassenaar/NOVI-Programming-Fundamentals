# === SCENES ===


def scene_Thor(naam):

    while True:
        print("Het Eiland van Thor is erg groot. Aan de andere kant van het eiland is er een haven. Daar staat een oud vrouwtje die jou belooft om jou te helpen zoeken naar de Drie Zielen Scarabee. \n"
              "Je kunt er ook voor kiezen om met een onderzeeër verder te reizen of je kiest er voor om lekker bij een café bij te komen.")
        print()
        try:
            keuze_Thor = int(input(f"Waar zal {naam} voor gaan? \n"
                                   "[1] Onderzeeër\n"
                                   "[2] Oud vrouwtje\n"
                                   "[3] Café\n"
                                   "\n"
                                   f"{naam} gaat voor keuze nummer: "))
            if keuze_Thor == 1:
                vis = input("De kapitein van de onderzeeër heeft een vraag voor jou: 'Wat is jouw lievelings vis?': ")
                print()
                print(f"Na een korte kennismaking reist {naam} in een onderzeeër met de kapitein die wel de weg weet... Hey, zag ik daar niet jouw lievelings vis? De {vis}?\n"
                      f"Je geeft toe dat je die lievelings vis hebt gezien. De kapitein stelt voor om achter een school {vis} te varen.\n"
                      f"NAAANUUNAANUUU\n"
                      f"Wat was dat? Worden we aangevallen?\n"
                      f"{naam} pakt gauw de enige duikuitrusting die nog over is en verlaat de onderzeeër.. en laat de kapitein verdrinken.\n"
                      f"Eenmaal op het land rent {naam} gauw naar het bewoonde deel van het land, maar plotseling valt {naam} door een diepe kuil..\n"
                      f".."
                      f"Het is erg donker...")
                resultaat = scene_Basilisk(naam)
                return resultaat


            elif keuze_Thor == 2:
                print()
                print(f'Je loopt naar de haven, richting het vrouwtje die jou belooft mee te zoeken met het vinden van de Drie Zielen Scarabee. "Kom maar mee naar mijn huis" zegt het oude vrouwtje..{naam} loopt zonder na te denken achter haar aan\n'
                      f'Het huis van het oude vrouwtje was niet echt schoon. Er stonden allemaal brouwseltjes op tafel, het aanrecht en zelfs op de grond. Er brandde maar een paar kaarsen in het huis. In het midden van het huis stond er een grote ketel\n'
                      f'"Als jij mij een zak goud geeft breng ik jou naar de plek van de Drie Zielen Scarabee" zegt het vrouwtje. {naam} geeft een zak met goud. Het vrouwtje gooit een bot van de Cerberus, nachtmos en een fluisterveer in de grote ketel.\n'
                      f'Het vrouwtje giet het brouwsel van de ketel in een flesje. "Als dit flesje opdrinkt, brengt het jou naar de plek van de Drie Zielen Scarabee. {naam}  drinkt het brouwsel in één slok weg.. {naam} voelt zich duizelig en valt flauw.\n'
                      f'\n'
                      f'{naam} wordt wakker, maar niet op een plek wat {naam} had gedacht...')

                resultaat = scene_Cerberus(naam)
                return resultaat

            elif keuze_Thor == 3:
                print()
                print(f"{naam} heeft besloten om even bij te komen in het café. daar krijgt {naam} een drankje aangeboden. {naam} drink het drankje op en is een beetje dronken.\n"
                      f"{naam} besluit weer verder te gaan varen richting een oude schip.")
                resultaat = scene_Kraken(naam)
                return resultaat
            else:
                print("=== JE MOET EEN KEUZE MAKEN. VOER 1, 2 OF 3 IN! ===")
        except ValueError:
            print("=== JE MOET EEN KEUZE MAKEN. VOER 1, 2 OF 3 IN! ===")


def scene_Basilisk(naam):
    while True:
        print(
            f'{naam} doet de deur open. Er klinkt een gorgelend geluid door de ruimte, daarna volgt er een "Hisssssss....."\n'
            f'Er kruipt een natte Basilisk richting {naam}! Het heeft een bek vol scherpe tanden en probeert {naam} aan te vallen!\n')
        volgende = input("Druk op enter om te kijken wat je kunt doen!")

        try:
            keuze_Basilisk = int(input("De Basilisk is een groot slangachtige wezen..Je kijkt snel om je heen. Overal zie je skeletten van mensen en dieren liggen.\n"
                    "Je ziet ook een skelet van een soldaat liggen. Zijn zwaard en schild liggen nog in goede conditie bij het skelet. \n"
                    "Aan de overkant hangt een touw. Je zou het touw kunnen beklimmen maar de Basilisk heeft een lange nek dus die kan jou snel te pakken krijgen\n"
                    "\n"
                    "Kies je voor het zwaard met schild of ren je toch richting het touw aan de overkant?\n"
                    "\n"
                    "[1] Zwaard en schild\n"
                    "[2] Touw beklimmen"))
            if keuze_Basilisk == 1:
                print()
                print(
                f"{naam} pakt snel het zwaard en het schild. Eerst snijdt {naam} een stuk staart van de Basilisk af. De Basilisk reageert snel en beweegt zicht rihting {naam}.\n"
                f"{naam} probeert zich te beschermen tegen de Basilisk met het schild.. Maar tevergeefs lukt het {naam} niet meer om het beest tegen te houden.\n"
                f"De Basilisk grijpt {naam} bij de benen. \n"
                f"{naam} schreeuwt het uit en probeert kruipend weg te komen van het beest.. maar waar naar toe? Er is geen uitweg.. \n"
                f"{naam} wordt levend opgegeten en zal nooit de Drie Zielen Scarabee vinden.\n"
                f"\n"
                f"RIP {naam}")
                return "dood"
            elif keuze_Basilisk == 2:
                print()
                print(f"{naam} rent naar het touw en ontsnapt net aan de Basilisk! Eenmaal naar boven geklommen neemt {naam} een hele diepe zucht en kijkt om zich heen.\n"
                 f"Alweer bevind {naam} zich in een andere kamer, maar dit keer vol met schatten! {naam} kan het niet geloven... de Drie Zielen Scarabee ligt er voor het oprapen!\n"
                      f"{naam} zal eeuwig leven...\n")
                return "kroon"
            else:
                print("=== JE MOET EEN KEUZE MAKEN. VOER 1 of IN! ===")
        except ValueError:
            print("=== JE MOET EEN KEUZE MAKEN. VOER 1 of IN! ===")


def scene_Cerberus(naam):
    while True:
        print()
        print(f"{naam} begint te zweten.. het is erg warm hier! {naam} kijkt goed om zich heen. Het is donker, maar de lava verlicht de duisternis in deze grot. {naam} doet snel alle kleding uit, de warmte is niet uit te houden!\n"
              f"Poedelnaakt probeert {naam} een uitweg te vinden. het lijkt wel een labyrint! {naam} hoort opeens het geluid van hijgende honden maar denkt op dit moment alleen maar aan een uitweg naar een verkoelende plek.\n")
        volgende = input(f"Druk op enter om er achter te komen welke eigenaardigheden in deze labyrint plaats gaat vinden...")
        try:
            keuze_Cerberus = int(input(f"{naam} dacht de uitgang gevonden te hebben. Maar dan komt er een beest tevoorschijn...Het is een CERBERUS! Een driekoppige monsterlijke hond met een lange slangenstaart!. \n"
                                       f"Cerberus komt steeds dichterbij.. hij wilt {naam} gaan OPETEN!\n"
                                       f"Wat gaat {naam} doen?\n"
                                       "\n"
                                       f"[1] {naam} Terug het labyrint in rennen en hopen dat Cerberus {naam} niet vind\n"
                                       f"[2] {naam} ziet geen uitweg meer en offert zichzelf op\n"
                                       f"[3] {naam} gooit een steen naar Cerberus\n"
                                       "\n"
                                       f"{naam} kies voor keuze nummer: "))

            if keuze_Cerberus == 1:
                print()
                print(
                    f"{naam}  rent terug het labyrint in.. maar Cerberus komt al gauw bij {naam} in de buurt. {naam} glijdt uit en Cerberus verscheurt {naam} in stukken..{naam} heeft de aanval niet overleeft..")
                return "dood"

            elif keuze_Cerberus == 2:
                print()
                print(
                    f"{naam} ziet geen uitweg meer in deze lavagrot labyrint...{naam} is super bang en offert zichzelf uit wanhoop op. Cerberus loopt op {naam} af. 6 ogen kijken {naam} aan. Maar Cerberus doet helemaal niets, het is een lieve 3 koppige hond\n"
                    f"{naam} voelt zich opgelucht maar wilt nu wel graag uit deze lavagrot. Cerberus leid {naam} de weg naar de uitgang. {naam} zet weer een stap op het oppervlak. Overal is zand.. Het lijkt wel een woestijn. {naam} ziet een oase en loopt er op af\n"
                    f"{naam} drinkt wat water uit de oase en opeens ligt er een sarcofaag half begraven. {naam} opent de sarcofaag en vind een artefact. mmm.. dat lijkt op een scarabee?.. \n"
                    f"\n"
                    f"{naam} bekijkt de artefact goed.\n"
                    f"HET IS DE DRIE ZIELEN SCARABEE!! ")
                print()
                print(f"{naam} springt in het rond! {naam} is zo blij dat de Drie Zielen Scarabee is gevonden.. of was het een illusie?")
                return "kroon"
            elif keuze_Cerberus == 3:
                print()
                print(f"{naam} gooit een steen naar Cerberus. Maar helaas werkt dat niet. Cerberus  verscheurt Cerberus {naam} in stukken..{naam} heeft de aanval niet overleeft..")
                return "dood"
            else:
                print("=== JE MOET EEN KEUZE MAKEN. VOER 1, 2 of 3 IN! ===")
        except ValueError:
            print("=== JE MOET EEN KEUZE MAKEN. VOER 1, 2 of 3 IN! ===")


def scene_Kraken(naam):
    while True:
        print()
        print(f"Na een lange tocht komt {naam} aan bij een oude schip. {naam} betreedt het schip. {naam} heeft het gevoel dat er iemand aanwezig is.\n"
              f"Opeens beweegt het oude schip! {naam} wordt bang en probeert te vluchten, maar het is te laat. \n"
              f"Grote tentakels bewegen zich om het schip heen. {naam} kan geen kant op.")
        print()
        volgende = input("Druk op enter om te kijken wat je kan doen")
        print()
        try:
            keuze_Kraken = int(input(f"{naam} had toevallig een toverstaf bij zich, en kent 2 spreuken. {naam} weet alleen niet meer welke spreuk wat doet\n"
                                     f"{naam} moet maar gaan gokken en kan dus kiezen uit 2 spreuken: \n"
                                     "[1] Abyssus Ignis!!!\n"
                                     "[2] Tentaculi Vinculum!!!\n"
                                     "\n"
                                     f"{naam} kiest voor spreuk nummer: "))
            if keuze_Kraken == 1:
                print()
                print(f"{naam} roept: ABYSSUS IGNIS!!. In plaats van dat {naam} de Kraken wegtovert, tovert {naam} zichzelf weg.\n"
                      f"{naam} heeft zichzelf in de maag van de Kraken getoverd... Dat is niet slim.. {naam} verstikt in de maag van de Kraken..")
                return "dood"
            elif keuze_Kraken == 2:
                print()
                print(f"{naam} roept: TENTACULI VINCULUM!!. De Kraken verslapt en zinkt het water in.. Nu kan {naam} rustig het oude schip onderzoeken. \n"
                      f"Verder op het dek vind {naam} een schatkist en opent het..{naam} pak de Drie Zielen Scarabee uit de kist! Wat een vondst!")
                return "kroon"
            else:
                print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
        except ValueError:
            print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")

# == CHECK DOOD OF GEWONNEN
def check_Resultaat(resultaat):
    if resultaat == "dood":
        print("Je bent dood")
        return True
    elif resultaat =="kroon":
        print("Gefeliciteerd! Je hebt gewonnen!")
        return True
    return False

def start_DungeonGame():

    while True:
        print("Welkom bij de Dungeon Game!")
        naam = input("Beste avonturier, wat is jouw naam?: ")
        print()
        print(f"Hallo {naam}! Welkom bij het begin van je reis! \n"
              f'Jij hebt besloten om op zoek te gaan naar de "Drie Zielen Scarabee"! Dit is een groot artefact van glanzend obsidiaan, vleugels van vuur met zandige gouden accenten. Het symboliseert de zielen van Anubis, Medusa en Muspel.\n'
              f'De artefact kan gebruikt worden om jezelf te beschermen tegen vijanden. Jij vind dit artefact zo bijzonder, dat je daarvoor op wereldreis gaat.\n'
              f"Dit wordt geen makkelijke reis. Er is een kans dat je het niet overleeft. Dus denk goed na welk pad jij bewandelt.")
        print()
        volgende = input("Druk op enter om te beginnen met jouw reis!")
        print()

        while True:
            try:

                keuze_Boot = int(input(f"Het is een mooie zonnige dag. {naam} is aangekomen op de haven en loopt langs een paar boten.\n"
                                           f"\n"
                                           f"De eerste boot is een papyrusboot, die gaat richting het Rijk van Anubis.\n"
                                           f"De tweede boot is een Trireem, een Grieks oorlogsschip die jou naar de Tempel van Medusa vervoert.\n"
                                           f"De derde boot is de Knarr, een grote vikingship die rechtstreeks naar Vlamland van Muspel vaart\n"
                                           f"\n"
                                           f"Welke boot kies je?\n"
                                           f"\n"
                                           f"[1] Rijk van Anubis \n"
                                           "[2] Tempel van Medusa \n"
                                           "[3] Vlamland van Muspel\n"
                                           "\n"
                                           f"{naam} kiest voor boot nummer:  "))
                if keuze_Boot == 1:
                    print()
                    print(f"{naam} heeft gekozen voor de reis naar het Rijk van Anubis...\n")
                    volgende = input("Druk op enter om te kijken wat er gaat gebeuren...\n")
                    print(
                        f'"{naam.upper()}! HOUD JE VAST!" Roept de kapitein. De papyrusboot wordt aangevallen door zeemonsters.\n'
                        f'Er moeten wapens liggen in de kist. Je rent gauw naar de kist en je ziet een harpoen en ... de vangst van de dag: Een hele dikke vette zeemeermin. Voor de rest ligt er niets meer...\n'
                        f'\n'
                        f'Hoe zorg jij dat de zeemonsters de papyrusboot met rust laten?\n')
                    volgende = input("Druk op enter om jouw keuze te maken\n")
                    while True:
                        #try:
                            keuze_Item = int(input(f"Wat zal {naam} doen?\n"
                                                   "[1] De harpoen richting de zeemonsters gooien...\n"
                                                   "[2] Een poging doen om de dikke vette zeemeermin de zee in te gooien...\n"
                                                   "\n"
                                                   f"{naam} kiest voor keuze nummer: "))
                            if keuze_Item == 1:
                                print()
                                print(f"{naam} gooit gauw de harpoen richting de zeemonsters. De zeemonsters blijven nog steeds aan de boot hangen. Er breek een stuk van de boot af.\n"
                                            f"Omdat de boot nu niet meer in evenwicht vaart, is de boot bij de Leeuwengrot van Sechmet gestrand. De kapitein is heel erg boos. Hij kan nu niet meer van dit stuk land af.\n"
                                            f"Hij probeert jou aan te vallen, maar al gauw ren je de grot in zodat hij jou niet meer kan vinden.\n"
                                            f"\n")
                                volgende = input("Druk op enter om te kijken wat er gebeurt als je verder de grot in loopt...\n"
                                                 "\n")
                                print(
                                    f"{naam} ziet een trap en loopt in een spiraal naar beneden. Er zijn 2 gesloten kelderdeuren. De linkerdeur heeft een symbool met een slangachtige wezen.\n"
                                    f"en de rechterdeur heeft een symbool met een hondachtige wezen.\n"
                                    f"\n")

                                volgende = input("Druk op enter om een deur te kiezen...\n")
                                while True:
                                    try:
                                        keuze_dier = int(input(f"Welke deur kiest {naam}?\n"
                                                                      f"[1] Deur met het symbool van een slangachtige wezen\n"
                                                                      f"[2] Deur met het symbool van een hondachtige wezen\n"
                                                                      f"\n"
                                                                      f"{naam} kiest voor deur nummer: "))
                                        if keuze_dier == 1:
                                            print()
                                            print("Je kiest voor de deur met het symbool van een slangachtige wezen")
                                            resultaat = scene_Basilisk(naam)
                                            if check_Resultaat(resultaat):
                                                return
                                        elif keuze_dier == 2:
                                            print()
                                            print("Je kiest voor de deur met het symbool van een hondachtige wezen")
                                            resultaat = scene_Cerberus(naam)
                                            if check_Resultaat(resultaat):
                                                return
                                        else:
                                            print("Kies een symbool!")
                                    except ValueError:
                                        print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
                            elif keuze_Item == 2:
                                print(
                                    f"{naam} kiest er voor om de vangst van de dag: de dikke vette zeemeermin in het water te gooien, zodat de zeemonsters daar achteraan gaan om op te eten\n"
                                    f"De boot is gelukkig niet beschadigt, maar al gauw ziet de kapitein donkere wolken in de lucht hangen. Het gaat onweren en de kapitein besluit om te stoppen bij het Eiland van Thor "
                                    f"\n")

                                resultaat = scene_Thor(naam)
                                if check_Resultaat(resultaat):
                                    return
                            else:
                                print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
                        #except ValueError:
                            #print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
                elif keuze_Boot == 2:
                    print("Je vaart richting de Tempel van Medusa. De kapitein van het Griekse oorlogsschip adviseert om niet te stoppen bij de tempel.\n"
                          "Medusa kan elk moment aanwezig zijn. Als je haar aankijkt verander je in steen! \n"
                          "Er wordt dus besloten om door te varen naar het Eiland van Thor")
                    resultaat = scene_Thor(naam)
                    if check_Resultaat(resultaat):
                        return

                elif keuze_Boot == 3:
                    print()
                    print("Je vaart naar Vlamland van Muspel")
                    print()
                    while True:
                        try:
                            keuze_drankje = int(input("Eenmaal op Vlamland van Muspel aangekomen, merk je dat het er.. 'verbrand' ruikt.\n"
                                                      "Opeens loopt er een vlamtrol op je af. Hij geeft jou 2 drankjes. Een smerig drankje en een lekker drankje \n"
                                                      "\n"
                                                      f"Welk drankje kiest {naam}?\n"
                                                      "\n"
                                                      "[1] Smerig drankje\n"
                                                      "[2] Lekker drankje\n"
                                                      "\n"
                                                      f"{naam} kiest voor drankje nummer: "))
                            if keuze_drankje == 1:
                                print("Je drinkt het smerige drankje.. Oef.. dat valt verkeerd, je voelt dat je moet kotsen en nodig naar de wc moet.. De kapitein stelt voor om naar het Eiland van Thor te gaan om jou daar af te zetten \n"
                                      "De kapitein heeft geen behoefte aan kots of stront op het schip.")
                                resultaat = scene_Thor(naam)
                                if check_Resultaat(resultaat):
                                    return

                            elif keuze_drankje == 2:
                                print("Je drinkt het lekkere drankje. Dat was lekker! Je besluit om verder te varen naar het Slagveld van Teutates.")
                                while True:
                                    try:
                                        keuze_fee = int(input("Het slagveld is nog 'vers'. Hier was nog net oorlog gevoerd. Er liggen heel veel slachtoffers op het veld. \n"
                                                                "Sommige leven nog en sommige zijn al dood.\n"
                                                                "\n"
                                                                f"Opeens vliegt er een kleine fee op {naam} af. Ze lijkt wel op Tinkerbell!\n"
                                                                f"De kleine fee is erg vedrietig en is op zoek naar een huisje.\n"
                                                                f"\n"
                                                                f"Wat bied {naam} aan?\n"
                                                                f"[1] {naam} stelt voor dat de fee mee gaat op reis\n"
                                                                f"[2] {naam} stelt voor dat de fee in een grote bloem gaat wonen\n"
                                                              f"\n"
                                                              f"{naam} kiest voor optie nummer: "))
                                        if keuze_fee == 1:
                                            print(f"De fee gaat met {naam} mee op reis. Tijdens het varen vraagt {naam} aan de fee welke kant ze nu op moeten.\n"
                                                  f"de fee wijst een eilandje aan. Er komt wel rook van het eiland maar dat maakt niet uit.\n"
                                                  f"Eenmaal op het eiland aangekomen vliegt de fee weer weg.\n"
                                                  f"{naam} loopt op het eiland, maar dan opeens valt {naam} door een gat in de diepe duisternis..")
                                            resultaat = scene_Cerberus(naam)
                                            if check_Resultaat(resultaat):
                                                return
                                        elif keuze_fee == 2:
                                            print("Je laat de fee in een grote bloem wonen. Dat is een mooi huisje voor de fee.\n"
                                                  f"{naam} wil graag verder varen, richting een oude verlaten schip")
                                            resultaat = scene_Kraken(naam)
                                            if check_Resultaat(resultaat):
                                                return

                                        else:
                                            print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
                                    except ValueError:
                                        print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
                            else:
                                print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")
                        except ValueError:
                            print("=== JE MOET EEN KEUZE MAKEN. VOER 1 OF 2 IN! ===")




                else:
                    print()
                    print("=== JE MOET EEN BOOT KIEZEN: VOER 1, 2 of 3 IN! ===")
                    print()
            except ValueError:
                print()
                print("=== JE MOET EEN BOOT KIEZEN: VOER 1, 2 of 3 IN! ===")
                print()


#Start spel
start_DungeonGame()