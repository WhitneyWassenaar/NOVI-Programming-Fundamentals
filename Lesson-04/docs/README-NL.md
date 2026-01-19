# EdHub 
# Programming Fundamentals Opgaven Hoofdstuk 6 en 7

## Inhoud
Er wordt geoefend met lists, slicing, dictionaries en tuples

## Korte samenvatting van wat ik heb geleerd

### Lists
- Wijzigen tijdens een loop: Als je een lijst in een for-loop wilt wijzigen (bijv. items verwijderen), maak dan een kopie van de lijst voor de loop. Dit voorkomt verschuivingen van indexen en fouten. Wijzigingen doe je aan de originele lijst.

- enumerate: Maakt van elk item in de lijst een tuple (index, item). Handig als je het item en de positie tegelijk nodig hebt.

- Startnummer bij enumerate: Je kunt zelf het startnummer bepalen (bijv. enumerate(lijst, 1)), zodat de eerste index 1 is in plaats van 0.

### For loop
- Print binnen vs buiten de loop:
  - Binnen: Elke iteratie wordt apart geprint. 
  - Buiten: De hele lijst wordt in één keer geprint.

### List comprehension
- Je kunt range() gebruiken in combinatie met len() om over een lijst te itereren op basis van de index, bijvoorbeeld:
  - ``[lijst[i] for i in range(len(lijst))]
``

### Tuple
- Immutable: Een tuple kan je niet wijzigen of bewerken.

- Om een nieuwe tuple te maken of “aan te passen”, gebruik je de tuple() functie of combineer slices en nieuwe waarden om een nieuwe tuple te maken.
-  Om een tuple te sorteren gebruik je sorted() en niet sort()

### Dictionary
- Bestaat uit key-value pair.
- Als je een key in een print statement plaatst, dan wordt de value weergegeven.

# sorted()
- Je kunt op key of op value sorteren. Bijvoorbeeld:  ```studenten = sorted(studenten, key=lambda x: x[1], reverse=True)```
## Informatie over het project
Dit is een EdHUb opdracht uit de leerlijn Programming Fundamentals uit de bootcamp Web-development van Hogeschool NOVI.