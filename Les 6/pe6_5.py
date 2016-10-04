import random

def monoplyworp():
    aantal_dubbel = 0
    eindeRonde = False
    while not eindeRonde:
        eersteWorp = random.randrange(5, 7)
        tweedeWorp = random.randrange(5, 7)
        totaal = eersteWorp + tweedeWorp
        if eersteWorp != tweedeWorp:
            print('{} + {} = {}'.format(eersteWorp, tweedeWorp, totaal))
            eindeRonde = True
        elif eersteWorp == tweedeWorp:
            aantal_dubbel += 1
            print('{} + {} = {} (dubbel)'.format(eersteWorp, tweedeWorp, totaal))
            if aantal_dubbel == 2:
                print('{} + {} = direct naar gevangenis'. format(eersteWorp, tweedeWorp))
                eindeRonde = True

monoplyworp()
