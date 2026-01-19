#Doe een functieaanroep van bereken_inhoud_cilinder() waarbij alleen de waarde van de hoogte als argument wordt meegegeven en voor de straal de defaultwaarde wordt gebruikt.
PI = 3.14159
def bereken_inhoud_cilinder(straal=1,hoogte=1):
    inhoud = PI * hoogte * straal ** 2
    return inhoud
print(bereken_inhoud_cilinder(hoogte=2))

