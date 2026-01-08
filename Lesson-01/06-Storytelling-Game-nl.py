# === LESSON 1: STORYTELLING GAME ===
# This is an exercise made during the lesson. The story and code is in Dutch to be understan
naam = input("Wat is je naam?: ")
naam_vriend = input("Hoe heet jouw beste vriend of vriendin?: ")
hoeveelheid = int(input("Kies een getal tussen 1 en 10: "))

while hoeveelheid < 1 or hoeveelheid > 10 :
    print("Je MOET een getal tussen 1 en 10 kiezen!")
    hoeveelheid = int(input("Kies een getal tussen 1 en 10: "))

ingrediënt = input("Wat vind jij een heerlijk ingrediënt om te gebruiken in een gerecht?: ")
pizza_prijs = 12.00
totale_bedrag = pizza_prijs * hoeveelheid
fav_place = input("Vul een locatie in (Vul in met een voorzetsel!): ")
korting_totale_bedrag = totale_bedrag * 0.85
emotie = input("Vul een emotie in: ")
voedseltoestand = input("Vul een voedseltoestand in. Bijvoorbeeld: rauw, vers, bedorven etc.: ")


print(f"{naam} is van plan om samen met {naam_vriend} {hoeveelheid} pizza's te bestellen met heerlijke {ingrediënt} topping {fav_place} ! ")
print(f"Een enkele pizza kostte €{pizza_prijs:.2f} dus uiteindelijk hebben zij €{totale_bedrag:.2f} betaald")
print(f"Onderweg vonden zij een kortingsbon van 15% op de grond. Zij bestelden opnieuw {hoeveelheid} pizza's en hoefden dit keer maar €{korting_totale_bedrag:.2f} te betalen. ")
print(f"Achteraf waren {naam} en {naam_vriend} erg {emotie}. De pizza's waren {voedseltoestand}.")