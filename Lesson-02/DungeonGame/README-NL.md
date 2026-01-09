# DungeonGame
Jij bent een avonturier die op zoek is naar de Drie Zielen Scarabee!

# Wat kan je in het spel?
Dit is een tekstgebaseerde avontuur spel. Het wordt ook wel een command-line game of text adventure game genoemd.

Voor elke situatie maak je een keuze, en dat heeft weer invloed op jouw verhaallijn. Uiteindelijk is het de bedoeling dat je de Drie Zielen Scarabee vind. Als je die hebt gevonden dan heb je gewonnen.

# Aan de slag
## Installatie
1. Zorg dat je een IDE hebt geïnstalleerd zoals PyCharm of VisualStudio
2. Clone de repository via de terminal
3. Klik op "RUN" om het spel te spelen

## Hoe speel je het spel?
Tenzij er wordt gevraagd om een woord in te voeren zal je altijd een nummer moeten invoeren. Meestal heb je een keuze tussen de 2 of 3  opties. Je voert dan het getal in de terminal om verder te spelen.
Als het spel geëindigd is, stopt het programma en zal je dus opnieuw op "RUN" moeten klikken

# Informatie over het project
Dit is een huiswerk opdracht van les 2 uit de leerlijn Programming Fundamentals uit de bootcamp Web-development van Hogeschool NOVI.

---
# Documentatie
Leerlijn: Hogeschool Novi Programming Fundamentals
Les 2
# Wat kan je in het spel?
Dit is een tekstgebaseerde avontuur spel. Het wordt ook wel een command-line game of text adventure game genoemd.

Voor elke situatie maak je een keuze, en dat heeft weer invloed op jouw verhaallijn. Uiteindelijk is het de bedoeling dat je de Drie Zielen Scarabee vindt. Als je die hebt gevonden dan heb je gewonnen.

## Flowchart: Structuur van het spel
<img src="Images/DungeonGame_Afbeelding3.png"></img>





## Nieuwe lege regel onder elkaar printen
Dit is het begin van het spel. Je voert jouw naam in en het spel zal jouw naam gebruiken in de events die gaan plaatsvinden.
Ik wilde graag de opties onder elkaar weergeven. Maar zoals je ziet, lukte dat niet. Natuurlijk wist ik wel dat dit mogelijk moest zijn. 
Hoe ik dacht dat ik het moest schrijven:``` /n ```

<img src="Images/DungeonGame_Afbeelding4.png"></img>

<b>Output</b>

<img src="Images/DungeonGame_Afbeelding5.png"></img>
 

## Waar ging het mis?
Ik had het bijna goed. Het moest zijn: 

``` \n ``` 

Bron: https://www.datacamp.com/tutorial/python-new-line
En nu ziet het er zo uit

<img src="Images/DungeonGame_Afbeelding6.png"></img>

 <img src="Images/DungeonGame_Afbeelding7.png"></img>

## Een variabele in brackets weergeven als UPPERCASE
Ik wil graag dat de variabele: naam wordt geprint in UPPERCASE. Ik wist niet hoe dat moest dus ik had dat opgezocht. Zo ziet het er eerst uit.

<img src="Images/DungeonGame_Afbeelding9.png"></img>

Bron: https://www.w3schools.com/python/ref_string_upper.asp
Gebruik “.upper()” om de string in uppercase te laten weergeven.

<img src="Images/DungeonGame_Afbeelding8.png"></img>

## Een scene herhalen
Al hoewel de keuzes vaak verschillend kunnen zijn, zullen sommige scenes zich moeten herhalen. Ik wil bijvoorbeeld dat keuze 1 overgaat naar de basilisk scene. 
 <img src="Images/DungeonGame_Afbeelding10.png"></img>

<b>Basilisk scene</b>

<img src="Images/DungeonGame_Afbeelding11.png"></img>

Maar omdat ik elke input van de scene met dezelfde variabele naam: ‘optie’ heb gegeven. Is het niet duidelijk welke scene herhaald moet worden.

Helaas werd het te onoverzichtelijk voor mij. Ik heb het project opnieuw gestart.
Dit keer had ik moeite met het spel opnieuw op te starten wanneer de speler dood was. Het kwam ook voor dat het spel terug ging naar een vorige input, maar niet helemaal aan het begin van het spel.

Er was ook sprake van veel herhaling. Ik heb toen gekeken welke scenes meerdere keren voorkwamen.

| Scene                    | Aantal |
|--------------------------|--------|
| Leeuwengrot van Sechmet  | 1      |
| Slagveld van Teutates    | 1      |
| Basilisk                 | 2      |
| Kraken                   | 2      |
| Eiland van Thor          | 3      |
| Cerberus                 | 3      |




Ik moet dus een functie schrijven voor elke scene die herhaald wordt. Op deze manier hoef ik niet stukken code opnieuw te schrijven voor elke optie die uitkomt op de aangewezen scene.

<img src="Images/DungeonGame_Afbeelding12.png"></img>

## Structuur
Ook kwam ik later achter dat ik structuur miste in mijn code. Aangezien ik het spel vaker wil spelen zal het spel zelf ook als functie geschreven moeten worden om het opnieuw aan te roepen als de speler dood is gegaan of heeft gewonnen.

## Houd het simpel
Ik heb serieus bijna een halve dag aan de code gezeten. Ik ben te lang in te veel code blijven hangen. Ik heb uiteindelijk de code weten te schrijven, maar niet zonder enige frustratie.
Ik dacht serieus dat ik bij elke keuzemogelijkheid een while loop moest gebruiken. Dat zag er dan ongeveer zo uit:

<b>Schematisch</b>

<img src="Images/DungeonGame_Afbeelding13.png"></img>
 
## In code
Hier kan je goed zien dat ik meerde while loops in mijn code heb verwerkt. Het heeft even geduurd want ik ben 2 keer van mening veranderd of al die while loops wel of niet nodig waren. Maar nu weet ik na trial en error dat while loops wel degelijk nodig zijn.

<img src="Images/DungeonGame_Afbeelding14.png"></img>

## Wanneer zijn while loops nodig?
While loops zijn nodig als je wil dat de code zich herhaald, maar je weet niet hoe vaak.  Bijvoorbeeld als er een int(input()) wordt gevraagd, zoals: 
```python
int(input('Maak een keuze tussen 1, 2 en 3'))
```

Dan wil je dat de speler het getal 1, 2 of 3 invoert. Als de speler dat niet doet en bijvoorbeeld een 4 invoert, dan zal je (als je netjes een if, elif en else statement hebt geschreven) éénmaal de else statement als output te zien krijgen en dan is de code gestopt.
Maar je wilt juist dat de speler opnieuw een poging kan doen om een getal te kiezen, dus als je de statements in een while loop doet dan wordt de input opnieuw gevraagd totdat de gewenste input wordt ingevoerd. Dit geldt dus voor while True
Elke input heb ik in een while True gezet.

<img src="Images/DungeonGame_Afbeelding15.png"></img>
 
## Try except
Vooral bij inputs waar een getal ingevoerd moet worden, is het belangrijk dat dit ook wordt gedaan. Wanneer er een enter of een woord wordt ingevoerd, dan ontstaat er een ValueError en dan crasht het programma.
Dit gebeurt er bij de eerste input. Zonder try except geeft pyhton terecht een error, want python probeert een string om te zetten naar een integer, en dat lukt niet. Als je try except toepast dan gaat de code terug naar de input om opnieuw ingevuld te worden.
Dit heb ik dus bij elke input toegepast.

<img src="Images/DungeonGame_Afbeelding16.png"></img>

Bron: https://www.youtube.com/watch?v=j_q6NGOwDJo

## De problematiek bij het Eiland van Thor
Het viel mij op dat wanneer ik het einde had bereikt (maakt niet uit of speler wel of niet had gewonnen) dat bij sommige routes voorkwam dat de speler terug ging naar een keuzemenu van een stap ervoor. Ik had toen bijna alle routes getest. Dit deed ik door lijnen te trekken over mijn flowchart.

<img src="Images/DungeonGame_Afbeelding17.png"></img>
 
## Wat valt je op?
Elke keer wanneer de route via het Eiland van Thor ging, belandde ik dus in de situatie dat ik na het einde terug ging naar de vorige scene (ergens tussen Eiland van Thor en een ander daaropvolgende scene). 
Dus het probleem ontstond bij de Eiland van Thor scene.


## Even een stap terug
Voordat ik verder ga met het bespreken wat er mis gaat op Eiland van Thor moet ik eerst uitleggen welke functie ik nog meer gebruikt heb in de code. Een ander onderdeel dat vaak terugkomt, is of de speler “dood” is of “de Drie Zielen Scarabe” heeft gevonden.
Dit doe ik met deze functie:

<img src="Images/DungeonGame_Afbeelding1.png"></img>

Deze functie checkt of het klopt dat de speler na het maken van een keuze, “dood” of “gewonnen” heeft 
(in het voorbeeld wordt kroon gebruikt omdat dit eerst het idee was van het spel (dit staat dus voor “gewonnen”), ik heb het gewoon gelaten in de code, in het verhaal heb ik kroon verandert naar de Drie Zielen Scarabee.)
Dit checkt de functie met een “return” statement. Als def check_Resulaat(resultaat): True terugkrijgt dan stopt het hele spel, en als het False krijgt dan blijf de functie draaien totdat het True terugkrijgt.


Dit is een functie van de Eiland van Thor scene: def scene_Thor(naam):
Wanneer de speler een keuze maakt in deze scene zal afhankelijk van de keuze de speler naar een volgende scene gaan. Dat zal dus de scene van Basilisk, Cerberus of Kraken zijn. Omdat deze scenes ook meerdere malen voorkomen in de code heb ik dus voor die scenes ook functies aangemaakt. Die staan onder de comment:

``` # === SCENES ===```

Ik neem dus het voorbeeld van keuze 1. Die brengt de speler naar de Basilisk scene. Bij de Basilisk scene (en ook bij Cerberus en Kraken scenes) zal de speler de laatste keuze gaan maken die bepaalt of de speler dood of gewonnen heeft.

Eerder had ik al laten zien dat ik een functie def check_Resultaat(resultaat): had aangemaakt om te checken of speler dood of gewonnen heeft en daarmee het spel eindigt als het True is. 

Omdat de scene van Eiland van Thor een while True bevat zal, nadat de speler dood of gewonnen heeft in de laatste scene terug gaan naar de while Loop die nog bezig is. 
En dat komt omdat de while loop niet vanzelf wordt stopgezet. Die moet je dus op een andere manier stopzetten.


## En hoe zorgen we er voor dat de code stopt? 
Daarvoor hebben we de functie: def check_Resultaat(resultaat): voor gemaakt. We moeten dus zorgen dat het resultaat ook terugkomt in de keuzes die in scene van Thor wordt gemaakt.

```resultaat =  scene_Basilisk(naam):```

De scene basilisk zal uiteindelijk eindigen met een return-statement. Dit zal altijd True zijn omdat ik dat zelf heb aangegeven in de def check_resultaat(resultaat) functie.

```return resultaat```

Het return-statement zal dus teruggeven wat de scene_Basilisk(naam) uiteindelijk zal teruggeven. Dus dat zal True zijn en daarmee stop je dus het keuzemenu van Eiland van Thor. . Ik heb daarvoor de variabele: resultaat voor aangemaakt.

<img src="Images/DungeonGame_Afbeelding2.png"></img>

 

## Wat heb ik van dit project geleerd?

1. Maak het idee concreet door het uit te tekenen in een flowchart

2.	Begin eerst met een klein idee. Je kan het later altijd nog uitbreiden.

3. Begin niet gelijk met het schrijven van code, maar schrijf het eerst uit in pseudocode.

4.	Als er iets mis gaat, teken dat ook uit of maak aantekeningen in je flowchart om het probleem beter in kaart te brengen.

5.	Probeer goed te begrijpen waarom je welke statement gebruikt. Je moet op een simpele manier kunnen uitleggen waarom je bepaalde code gebruikt. Kan je dat niet dan begrijp je eigenlijk niet zo goed wat de code doet. Ga dan terug naar de basis en oefen eerst met simpele code.

6.	Merk je dat je bepaalde stukken code vaak moet herhalen? Probeer dat te voorkomen door functies aan te maken voor de betreffende code zodat het je veel knippen/plakken bespaart en maakt je code overzichtelijker.

7.	Blijf niet te lang hangen als je het niet weet. Begin dan opnieuw, ga terug naar jouw pseudocode en doe research als je iets niet begrijpt of vraag het aan iemand die het wel weet.

8.	Begin gelijk met documenteren. Als je elk probleem vastlegt in je documentatie op het moment dat het gebeurt, dan ben je actief bezig met het oplossen van het probleem. En als je het dan terugleest, begrijp sneller hoe je dat hebt gedaan.

## Als ik meer tijd had wat had ik dan nog veranderd aan het project?

1.	Ik had waarschijnlijk het resultaat: “kroon” veranderd naar “gewonnen”

2.	Als de speler verloren of gewonnen had de keuze kunnen geven of ze het spel opnieuw willen spelen of willen stoppen. Nu stopt het spel altijd nadat je gewonnen of verloren hebt.

3.	Meer aandacht besteden aan personaliseren tijdens het spelen. Dus bijvoorbeeld dat jouw invoer (als dat een woord is) invloed heeft hoe de speler het spel ervaart. Nu heb ik alleen 1 input die vraagt wat jouw lievelingsvis is. Nog niet heel erg creatief.

4.	Ik had misschien nog een puntenteller kunnen implementeren. Maar ik vind dat het spel daar te kort voor duurt, maar het zou wel handig zijn om mee te testen.

5.	Of nog leuker, geld systeem implementeren. Dat je in het spel items kan kopen met het geld wat je tijdens het spelen verdient.





