# EdHub 
# Programming Fundamentals Opgaven Hoofdstuk 5 en 6

De repository bevat een verzameling van opgaven uit de EdHub en lesvoorbereiding.

## Inhoud
Er wordt geoefend met if/else-statements.

### Rekenmachine
Je gaat een simpele rekenmachine maken die 2 getallen als input wilt en een operator ( + - / * ) hieruit ga jij zorgen dat de juiste berekening wordt gedaan.

### Pizza_Plaza
Je werkt in een pizzeria, hier hebben ze alleen geen handig systeem om uit te rekenen hoeveel een pizza kost. Daar ben jij als programmeur voor ingehuurd. Je moet rekening houden naar de maat van de pizza en de extra toppings.

### Treasure
Je bent op een eiland aangekomen waar je telkens keuzes kan maken. elke keuze leidt weer naar een andere plek. het is mogelijk dat je niet meer verder kan spelen na het vallen in een gat oid.

### Password
Schrijf een programma dat een gebruiker om een wachtwoord vraagt. De gebruiker heeft maximaal 3 pogingen om het juiste wachtwoord in te voeren. Als het juiste wachtwoord is ingevoerd, print je een succesbericht en beëindig je de loop. Als de gebruiker 3 pogingen fout invoert, geef je een bericht dat de toegang is geweigerd.

### Random number
 In deze opdracht ga je een script schrijven waarbij de gebruiker een geheim getal moet raden.

### Wisselgeld
Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent, en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.


## Korte samenvatting van wat ik heb geleerd
### Rekenmachine :heavy_plus_sign::heavy_minus_sign:
- Ik heb geleerd dat exception handling overbodig is bij string-inputs. Bij een int of float input heb je meer kans op ValueError dus is het wel handig om daarvoor exception handling te gebruiken. Wel zo handig om dat in een while loop te doen omdat je graag wil dat de input opnieuw beschikbaar gesteld wordt om in te voeren als de vorige invoer incorrect was.
___
### Pizza plaza :pizza:
De grootste uitdaging voor mij was om de code zo kort en efficiënt mogelijk op te kunnen schrijven.  Ik begon vaak te groot en uitgebreid terwijl dat niet nodig was, daardoor werd de code foutgevoeliger. 
  
Ik had dus geprobeerd om tot een zo kort maar efficiënte code te komen waar ik te tevreden mee was. Want al gauw merkte ik dat ik weer wat extra's wilde toevoegen om de code mooier te laten lijken. Ik was uiteindelijk tot de zesde versie gekomen. Korter dan de zesde versie wilde ik het niet maken omdat het voor mij niet meer logisch werkte. 

Bijvoorbeeld: Je kan pepperoni en kaas bestellen zonder de pizza. 

Ik vond dat niet kunnen, dus ik had er voor gezorgd dat dit niet kon.

- Ik moest goed opletten dat als ik wil dat de print statement uitgevoerd wordt, dat ik ``and`` gebruik in plaats van ``or``. Je zou denken als je geen 'S' of 'M' of 'L' invoert > print dan deze tekst. Maar stel je kiest bijvoorbeeld voor 'M', die heb je dus wel gekozen maar 'S' en 'M' niet. Dat betekent dat voor  ``formaat != 'S'`` en ``formaat != 'L' `` is ``True``, en juist omdat het een ``or`` is zal als 1 van de 3 waarden als ``True`` is,  de tekst printen, en dat klopt niet. Vandaar dat je ``and`` gebruikt en geen ``or``.

```python
if formaat != 'S' and formaat != 'M' and formaat != 'L':
    print('Je had blijkbaar geen zin om een pizza te bestellen')
```

- Ik heb geleerd dat je een lijst ter plekke kunt aanmaken. Je hoeft het dus niet per se van te voren te definiëren.
```python
if formaat in ['S', 'M', 'L']:
    print(f'Pizza {formaat}, rekening €{rekening}')
else:
    print('Je hebt geen pizza gekozen') 
```
___
### Treasure :lock:
- Voor het eerst weet ik wat ASCII art is. Voor de opdracht heb ik een image to ASCII converter website gebruikt https://www.asciiart.eu/image-to-ascii om snel ASCII art te creëren. Ik heb Code page 437 gekozen als ASCII gradient.

- Ik heb een input na de laatste print statement geplaatst voor het geval je de code opent in python.<br>Als het programma eindigt zou je de laatste print statement niet zien, dus vandaar een extra input: ```input("Press enter to quit the game")```
___
### Password :closed_lock_with_key:
- Ik merkte dat ik te lang bleef hangen bij de conditie van de while loop. Vaak was er een fout in de code waarbij er een foutmelding kwam als het antwoord bij de 3de poging goed was ingevoerd. Ik maakte het daardoor te moeilijk voor mijzelf. Moest ik de while loop starten met de hoeveelheid pogingen of zolang er geen juiste wachtwoord werd ingevoerd? Er was ook een geval dat een variabele geel onderstreept was, dan was het dus niet gedefinieërd, willen we dat vermijden of is een enkele keer geen probleem?

- In deze opgave was het belangrijk om te snappen welke factor de grootste prioriteit heeft. Wat weegt zwaarder? Het aantal pogingen om een wachtwoord te kunnen invoeren of wanneer het juiste wachtwoord wordt ingevoerd? Volgorde maakt heel veel uit.
___
### Random number :1234:
- In python werkt 'random.randInt(1,10)' en 'random.randomInt(1,10)' NIET!
- In python werkt 'random.randint(1,10)' WEL!
- De 1 en 10 tellen mee in random.randint(1,10)

___
### Wisselgeld
- Als we een variabele meerdere keren gebruiken in if-statements, dan kan de waarde van die variabele veranderen (of worden overschreven), afhankelijk van welke voorwaarde wordt uitgevoerd.
- Ik weet nu hoe je een tuple kunt gebruiken in combinatie met functies.
- De parameter van een functie mag je vrijwel elke naam geven, en je kunt bij het aanroepen van de functie een bestaande variabele meegeven als argument.

## Informatie over het project
Dit is deels een EdHUb opdracht en lesvoorbereiding uit de leerlijn Programming Fundamentals uit de bootcamp Web-development van Hogeschool NOVI.