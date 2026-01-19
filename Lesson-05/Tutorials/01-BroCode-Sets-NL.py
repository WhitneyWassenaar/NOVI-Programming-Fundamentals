# Een set is een collectie die ongeordend en geen index heeft. Het accepteert geen duplicaten waarden.
# Als je een set print dan zal het in willekeurige volgorde geprint worden. Elke keer als je het opnieuw print zal het in een andere volgorde weergegeven worden.
# Een set is daarom sneller dan een list als je wil checken of een item in een set aanwezig is.
utensils = {"fork", "spoon", "knife"}

#for x in utensils:
#    print(x)

# Je zult zien dat als je duplicaten in een set hebt dat je maar 1 exemplaar te zien krijgt.
#utensils = {"fork", "spoon", "knife","knife","knife"}

#for x in utensils:
#    print(x)

# -----------------------------------------------------------------------------------------------------
bestek = {"vork", "lepel", "mes"}
servies = {"kopje", "schaaltje", "bord"}
#bestek.add("servet")                #| Voeg item toe aan set
#bestek.remove("vork")               #| Verwijder item van set
#bestek.clear()                      #| Verwijder alle items in een set
#bestek.update(servies)              #| Voeg set(servies) bij set(bestek)
#eet_tafel = bestek.union(servies)   #| Maakt een nieuwe set door sets samen te voegen

#print(bestek.intersection(servies)) #| Print de items die bestaan in beide sets.

#for x in bestek: # Als je bestek + command gebruikt
#    print(x)

#for x in eet_tafel: # Als je eet_tafel = bestek.union(servies) gebruikt
#    print(x)

# -----------------------------------------------------------------------------------------------------

symbolen = {"leeuw", "ster", "maan", "oog"}
sterrenbeeld = {"stier", "leeuw", "maagd", "vissen"}

# Ik wil weten wat set(symbolen) wel heeft maar set(sterrenbeeld) niet

print(symbolen.difference(sterrenbeeld))
# OUTPUT: {'maan', 'oog', 'ster'}
# -----------------------------------------------------------------------------------------------------