studentNamen = {'Gokmen': 8.5, 'Ozgur': 5.5, 'Hassan': 6.7, 'Abi': 7,
                 'Jan': 20, 'gokmen': 22 }


for (key,value) in studentNamen.items():
    if value >= 9:
        print('Student {} heeft cijfer: {}' .format(key,value))

