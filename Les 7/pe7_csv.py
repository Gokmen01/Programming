import csv

with open('namen', 'r') as namen:
    reader = csv.reader(namen, delimiter=';')

    for row in reader:
        print('{} heeft als beroep {}' .format(row[0], row[1]))


