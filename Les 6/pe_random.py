import random
lijst = ['Gokmen', 'Ozgur', 'Hassan','Kishan']

spel_is_klaar = False

while not spel_is_klaar:
    naam = random.choice(lijst)
    print("de beurt is aan {}" .format(naam))
    gekozen = int(input("Geef een getal onder 10:"))
    getal = random.randrange(1,11)

    if gekozen == getal:
        print('De winaar is {}' .format(naam))
        break
    else:
        print('Helaas, op naar de volgende ronde')

print('Einde spel')
