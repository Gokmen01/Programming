studentNamen = {}
# toevoegen dict_naam[naam] = key
invoer = input("Voer naam in")


while invoer is not '':
    if invoer  not in studentNamen:
        studentNamen[invoer] = 1
    else:
        studentNamen[invoer] += 1
    invoer = input("Volgende naam:")
for (key, value) in studentNamen.items():
    if value == 1:
        print('Er is {} student met de naam {}'.format(value, key))

for (key, value) in studentNamen.items():
    if value > 1:
        print("Er zijn {} studenten met de naam {}".format(value,key))
  #fds
