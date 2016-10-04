invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
nr_integers = []
nummers = invoer.split('-')

for nr in nummers:
    nr_integers.append(int(nr))
nr_integers.sort()
grootsteGetal = max(nr_integers)
kleintsteGetal = min(nr_integers)
som = sum(nr_integers)
lengte = len(nr_integers)
gemiddelde = som / lengte
print('Gesorteerde list van ints: {} \nGrootste getal: {} en Kleinste getal: {}' .format(nr_integers, grootsteGetal, kleintsteGetal))
print('Aantal getallen: {} en Som van de getallen: {} \nGemiddelde: {}' .format(lengte, som, gemiddelde))
