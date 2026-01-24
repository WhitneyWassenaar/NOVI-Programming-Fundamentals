"""
libraries
- menukeuze: uber-dienst
- uber-dienst: prijs


menu
gebruiker kiest 1 van de 3 diensten
- keuze 1
- keuze 2
- keuze 3

km
Gebruiker geeft aan hoeveel km gereden moet worden
invoer km

totale kosten bereken
uber-dienst prijs * km

gebruiker ziet totale kosten
print statement


---BONUS---

start()
[1] Voorkeur dienst aanpassen ✔
[2] Geschiedenis zien ✔
[3] rit boeken 

preference() 
- kies een dienst✔
- werk USER dict bij ✔
- terug naar start() ✔

history()
- check of history dict is gevuld ✔
- Zo niet, ga terug naar start ✔
- Zo ja, print history dict en ga terug naar start() ✔

rit_boeken()
- vraag of gebruiker voorkeursdienst wil gebruiken of een andere dienst wil kiezen ✔
- als gebruiker kies voor voorkeurdienst gebruiken, check of USER een preference heeft ✔
- zo ja, gebruiker USER["preference"] als keuze ✔
- Zo niet, dan gaat gebruiker terug naar rit_boeken()

- als gebruiker andere dienst kiest
- kiest gebruiker een dienst en vraagt km

total_price()
- na km, berekent total_price() de totale prijs
- Ga terug naar start()



start()


preference()
- {USER["preference]}

history()
- {USER["history]}

book_a_ride()
heeft nodig
- ride_option waarde van preference() > doet niets, alleen voor gebruiker print() om te laten zien of preference_service aanwezig is of niet
- ride_option waarde van eigen invoer > different_service()

different_service()
heeft nodig
- preferred_service, als het bestaat
- eigen invoer welke service
- km

geeft resultaat van deze waarden ((preferred_service of eigen invoer) ,km)

total_price()
heeft nodig
invoer: preferred_service, als het bestaat of eigen invoer welke service
- km
geeft resultaat van invoer * km om totaal te berekenen


BUGS
- After booking a ride, the booked ride was not added to the history
    > Create dictionary for booked rides to save each ride
    > booked_rides dictionary placed as a dict-item in USER['history']

- The program crashes if you enter a number that is not in the menu in ---Services---
    > Add while loop
    > if input not in (1,2,3)

- The program crashes if you enter a number that is not in the menu in ---Services---
    > Add while loop
    > if input not in (1,2,3)

- After [3] Book a ride in Start, if you enter a number that is not to choose from, it asks again without a warning
    > Add while loop
    > if input not in (1,2)

NOTE
- the keys from booked_ride are marked with a yellow line, it means that the IDE does not know if the keys that are added, are all dicts
"""