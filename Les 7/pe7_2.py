import datetime
import csv

while True:
    print('Wat is je naam?\nVoer \'einde\' in om te stoppen')
    naam = input()
    if naam == 'einde':
        break

    voorletters = input('Wat is je voorletter?')
    gebDatum = input('Wat is je geboortedatum')
    email = input('Wat is je email')

    formatted_time = datetime.datetime.now().strftime('%a %d %B %Y at %I:%M')
    try:
        with open('inloggen', 'a', newline='') as inlogFile:
            wr = csv.writer(inlogFile, delimiter=';')
            wr.writerow((formatted_time, naam, voorletters, gebDatum))
    except IOError:
        print('IO error')
