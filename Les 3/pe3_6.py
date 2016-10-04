lijst = ['a', 'b', 'c']
def wijzig(letterlijst):
    print(lijst)
    lijst.clear()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')
    print(lijst)

wijzig(lijst)

#Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven? lijst is buiten de functie al in gebruik.
#Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
#Dit werkt niet, strings zijn niet mutable.
#Welke rol speelt (im)mutabiliteit in deze vraag? Het is met wijzigen van waardes van belang of een object mutable of immutable is.
