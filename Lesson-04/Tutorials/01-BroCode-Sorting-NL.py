# === BROCODE ===
# Om sort()/sorted() bij lists, tuples en dictionaries beter te begrijpen heb ik de video van Tutorials gebruikt om aantekeningen te maken.
# Bron: https://www.youtube.com/watch?v=cd-vtiO5chk&t=503s

# === LISTS ===
fruits = ["banana", "orange", "apple", "coconut"]

fruits.sort() # sort() zet strings in alfabetische volgorde
print(fruits)

nummers = [5,7,2,99,55,3,1]

nummers.sort() # sort() zet nummers in volgorde van klein naar groot
print(nummers)

nummers.sort(reverse=True) # sort(reverse=True) zet items in tegengestelde volgorde. Voor de lijst nummers is dat van groot naar klein
fruits.sort(reverse=True) # Voor een lijst met strings is dat omgekeerde-alfabetische volgorde.

print(nummers)
print(fruits)

# === TUPLES ===

dieren = ("Hond", "Kat", "Konijn", "Hamster")
# dieren.sort()
# print(dieren) # Dit geeft een error omdat tuples geen sort() attribuut gebruikt, lists kunnen wel sort() gebruiken.


dieren = sorted(dieren)
print(dieren)

# sorted() is case-sensitive, hoofdletters gaan voor kleine letters.
# resultaat: ['A', 'B', 'C', 'a', 'b', 'c']
alfabet = ("a", "A", "c", "C", "B", "b")

alfabet = sorted(alfabet)
print(alfabet)

# Voor alfabetische volgorde ongeacht of de string Hoofdletter heeft of niet.
alfabet = sorted(alfabet, key=str.lower)
print(alfabet)

# === DICTIONARIES ===
# In de boekenkast staan boeken van verschillende categorieën, de hoeveelheid boeken is aangegeven in nummers per categorie
# Een dictionary bevat een 'key-value pair' dus een key en een waarde. Hier is "roman" de key en '4' de waarde.

boekenkast = {"roman": 4,
              "thriller": 10,
              "avontuur": 2,
              "komedie": 5}

#boekenkast = sorted(boekenkast) # Als je sorted() gebruikt bij een dictionary dan verdwijnen de waarden en wordt alleen de keys weergegeven in een lijst

# Als je de dictionary op deze manier print, dan wordt alleen de keys geprint in alfabetische volgorde, en de waarden verdwijnen. De dictionary is geconverteerd naar een list.
boekenkast = sorted(boekenkast)
print(boekenkast)

# === ITEMS ===
# Dit is een dictionary van fruit. De key is de naam van een fruitsoort en de value is de hoeveelheid kcal
fruit = {"banaan": 100,
         "sinaasappel": 73,
         "appel": 72,
         "aardbei": 30}

# De items() method geeft een tuple terug. Voor elke key-value pair geeft de items() method een tuple terug.
# Dus de tuples die teruggegeven worden zijn: ("banaan", 100), ("sinaasappel", 75) etc.
fruit = sorted(fruit.items())
print(fruit)

# === TYPECASTEN ===
# Dit is een dictionary van gespotte vogels. De key is de vogelsoort en de value is de aantal keren dat de vogel is gespot
vogelspotter = {"spreeuw": 4,
                "roodborstje": 10,
                "kraai": 2,
                "meeuw": 20}

# Bij de vorige dictionary heb ik de items() method gebruikt.
# Nu wil ik dat de dictionary in alfabetische volgorde wordt geprint. Dit doe ik door dict() method te gebruiken zodat de dictionary daadwerkelijk als een dictionary wordt weergegeven.
# Dit is typecasten
vogelspotter = dict(sorted(vogelspotter.items()))
print(vogelspotter)

# Dit is een dictionary voor katten. De key is de kleur van de kat en de value is de aantal.
katten = {"rood": 4,
          "zwart": 1,
          "wit": 2,
          "bruin": 2}

# Ik wil graag de dictionary printen in omgekeerde alfabetische volgorde
katten =dict(sorted(katten.items(), key=lambda item: item[0], reverse=True))

#Ik wil graag de dictionary printen op value
katten =dict(sorted(katten.items(), key=lambda item: item[1]))
print(katten)