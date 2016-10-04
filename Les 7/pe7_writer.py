import csv
with open("namen", 'a', newline='\n') as namen:
    writer = csv.writer(namen, delimiter=';')

    while True:
        name = input("Naam?")

        if name == '':
            break
        age = input("age?")
        job = input("Job?")

        writer.writerow((name,job,age)) # tuple
