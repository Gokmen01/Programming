bestand = open('C:/Users/Gokmen/Documents/kaartnummers.txt', 'r')

for lijn in bestand:
    nummer = (lijn[:6])
    naam = (lijn[7:].strip())
    print('{} heeft kaartnummer: {}' .format(naam, nummer))
bestand.close()
